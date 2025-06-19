from typing import Any, Dict, List, Optional

class Executor:
    def __init__(self, llm_client:Any, tools: Any, memory:Any):
        self.llm_client = llm_client
        self.tools = tools
        self.memory = memory
        
    def run_step(self, step_desc:str)->str:
        print(f"executing step: {step_desc}")
        if "search" in step_desc.lower() or "find" in step_desc.lower():
            tool = self.tools.get("search")
            result = tool(step_desc)
        if "wikipedia" in step_desc.lower() or "wiki" in step_desc.lower() or "encyclopedia" in step_desc.lower():
            topic = step_desc.split("such as")[-1] if "such as" in step_desc else step_desc
            return self.tools.get("wikipedia")(topic)
        else:
            # result = f"(no tool for: {step_desc})"
            return None 

        # result = f"(stub) completed: {step_desc}"
        print(f"   ↳ Result: {result}\n")
        return result
    
    def summarize(self, all_results:List[str])->str:
        results = "\n".join(f"{r}" for r in all_results)
        prompt  = f"""
        "You are an expert assistant.\n"
        "Given the following list of step results, write a concise, user-friendly summary paragraph under 100 words\n"
        "that explains what was done and what the key findings were.\n"
        Given the following step results (ignore any steps where no data was available)
        step_results: {results}
        "Summary:"
        """
        summary = self.llm_client.generate(prompt)
        return summary.strip()
        # return "\n".join(all_results)
