from .search_tool import SearchTool
from .wikipedia_tool import WikipediaTool
from typing import Any, Dict, Callable

class ToolRegistry:
    def __init__(self, settings):
        # you can inspect settings to decide which tools to load
        self._tools = {
            "search": SearchTool(settings.search_api_key).run,
            "wikipedia": WikipediaTool().run
        }

    def get(self, name: str):
        if name not in self._tools:
            raise KeyError(f"No tool named {name}")
        return self._tools[name]
    






    #