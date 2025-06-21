# from typing import Any, Dict, List, Optional

# class Executor:
#     def __init__(self, llm_client:Any, tools: Any, memory:Any):
#         self.llm_client = llm_client
#         self.tools = tools
#         self.memory = memory
        
#     def run_step(self, step_desc:str)->str:
#         print(f"executing step: {step_desc}")
#         if "search" in step_desc.lower() or "find" in step_desc.lower():
#             tool = self.tools.get("search")
#             result = tool(step_desc)
#         if "wikipedia" in step_desc.lower() or "wiki" in step_desc.lower() or "encyclopedia" in step_desc.lower():
#             topic = step_desc.split("such as")[-1] if "such as" in step_desc else step_desc
#             return self.tools.get("wikipedia")(topic)
#         else:
#             # result = f"(no tool for: {step_desc})"
#             return None 

#         # result = f"(stub) completed: {step_desc}"
#         print(f"   ↳ Result: {result}\n")
#         return result
    
#     def summarize(self, all_results:List[str])->str:
#         results = "\n".join(f"{r}" for r in all_results)
#         prompt  = f"""
#         "You are an expert assistant.\n"
#         "Given the following list of step results, write a concise, user-friendly summary paragraph under 100 words\n"
#         "that explains what was done and what the key findings were.\n"
#         Given the following step results (ignore any steps where no data was available)
#         step_results: {results}
#         "Summary:"
#         """
#         summary = self.llm_client.generate(prompt)
#         return summary.strip()
#         # return "\n".join(all_results)






import json

class Executor:
    def __init__(self, llm_client, tools, memory):
        self.llm = llm_client
        self.tools = tools
        self.memory = memory

    def run_step(self, step_desc:str)->str|None:
        resp = self.llm.chat.completions.create(
            model = self.llm,
            messages = [
            {"role":"system", "content": "You decide which tool to call."},
            {"role":"user",   "content": step_desc}
            ],
            functions = self.tools.functions_defs
        )

        msg = resp.choices[0].message
        print(msg)
        if msg.function_call:
            fname = msg.function_call.name
            print("Fname\n")
            print(fname)
            args = json.loads(msg.function_call.arguments)

            result = self.tools.get(fname)(**args)

            followup = self.llm.chat.completions.create(
                model = self.llm.model,
                messages = [
                    *resp.messages,
                    {"role":"function","name":fname,"content":json.dumps(results)}
                ]
            )
            return followup.choices[0].message.content
        return msg.content
        
