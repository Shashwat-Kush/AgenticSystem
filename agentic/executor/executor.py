from typing import Any, Dict, List, Optional

class Executor:
    def __init__(self, llm_client:Any, tools: Any, memory:Any):
        self.llm_client = llm_client
        self.tools = tools
        self.memory = memory
        
    def run_step(self, step_desc:str)->str:
        print(f"executing step: {step_desc}")
        result = f"(stub) completed: {step_desc}"
        print(f"   ↳ Result: {result}\n")
        return result
    
    def summarize(self, all_results:List[str])->str:
        return "\n".join(all_results)
