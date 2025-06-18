from agentic.config    import Settings
from agentic.planner   import Planner
from agentic.tools.tool_registry import ToolRegistry
from agentic.memory.vector_memory import VectorMemory
from agentic.executor    import Executor

def main():
    settings = Settings()
    planner  = Planner(llm_client=settings.llm_client)
    tools   = ToolRegistry(settings)
    memory  = VectorMemory(settings.mem_db)
    executor = Executor(llm_client=settings.llm_client, tools=tools, memory=memory)
    goal  = input("🔍 What’s your goal? ")
    steps = planner.generate_plan(goal)
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")
    result = []
    for step in steps:
        res = executor.run_step(step)
        result.append(res)
    print("\n🎯 Final Summary:\n", executor.summarize(result))
if __name__ == "__main__":
    main()