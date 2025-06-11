from core.agents.topological_agent import TopologicalAgent

def execute_research_task():
    agent = TopologicalAgent()
    return agent.analyze_all()

if __name__ == "__main__":
    results = execute_research_task()
    print("Results:", results)
