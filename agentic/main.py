from agentic.config    import Settings
from agentic.planner   import Planner
from agentic.tools.tool_registry import ToolRegistry
from agentic.memory.vector_memory import VectorMemory
from agentic.executor    import Executor

def main():
    settings = Settings()
    tools   = ToolRegistry(settings)
    memory  = VectorMemory(settings.mem_db)
    planner  = Planner(llm_client=settings.llm_client,memory=memory)
    executor = Executor(llm_client=settings.llm_client, tools=tools, memory=memory)
    goal  = input("🔍 What’s your goal? ")
    steps = planner.generate_plan(goal)



    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")



    results: list[str] = []
    for step in steps:
        print(f"▶️  Step: {step}")
        result = executor.run_step(step)
        # Only keep non-empty results
        if result:
            print(f"   ↪️  Got result:\n{result}\n")
            results.append(result)
            # print(result)
            memory.store(step,result)
    print("\n🎯 Final Summary:\n", executor.summarize(results))
if __name__ == "__main__":
    main()