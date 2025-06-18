import pytest
import json
from agentic.planner.planner import Planner

class DummyLLM:
    """A stub LLM client that always returns the same raw_response."""
    def __init__(self, raw_response: str):
        self.raw_response = raw_response

    def generate(self, prompt: str) -> str:
        # We could also assert something about the prompt here if desired
        return self.raw_response

@pytest.mark.parametrize("raw, expected", [
    # 1) Well-formed JSON array
    ('[{"step":1,"description":"Do X"},{"step":2,"description":"Do Y"}]',
     ["Do X", "Do Y"]),

    # 2) Numbered list fallback
    ("1. First action\n2. Second action\n3. Third action",
     ["First action", "Second action", "Third action"]),

    # 3) Mixed with extra lines and noise
    ("Intro text\n1. Alpha step\nSome noise\n2. Beta step\n",
     ["Alpha step", "Beta step"]),

    # 4) Empty response → no steps
    ("", []),
])
def test_generate_plan_parsing(raw, expected):
    llm = DummyLLM(raw)
    planner = Planner(llm_client=llm)
    result = planner.generate_plan("any goal")
    assert result == expected

def test_invalid_json_fallback_to_numbered():
    # JSON-decode will fail, so we expect the fallback to process numbered list
    broken_json = '[{this is not valid JSON]'
    numbered = "1. Step A\n2. Step B"
    # combine them
    raw = broken_json + "\n" + numbered
    llm = DummyLLM(raw)
    planner = Planner(llm_client=llm)
    result = planner.generate_plan("goal")
    assert result == ["Step A", "Step B"]

def test_strip_whitespace_and_non_numeric_prefix():
    raw = "  1.  Lead space\n01. Padded number\n- Not a step\n2. Trailing space  "
    llm = DummyLLM(raw)
    planner = Planner(llm_client=llm)
    result = planner.generate_plan("goal")
    # Only lines with a dot prefix and numeric first token are kept
    assert result == ["Lead space", "Padded number", "Trailing space"]