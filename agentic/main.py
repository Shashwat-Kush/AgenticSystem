from agentic.config    import Settings
from agentic.planner   import Planner

def main():
    settings = Settings()
    planner  = Planner(llm_client=settings.llm_client)

    goal  = input("🔍 What’s your goal? ")
    steps = planner.generate_plan(goal)
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

if __name__ == "__main__":
    main()