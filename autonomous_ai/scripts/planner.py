from core.agents.topological_agent import TopologicalAgent

def handle_llm_command(command, params):
    if command == "analyze_sat":
        return TopologicalAgent().analyze_all()
    return {"error": "Unknown command"}
