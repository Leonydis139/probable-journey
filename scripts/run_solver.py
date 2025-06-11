from core.agents.topological_agent import TopologicalAgent
from core.agents.export_utils import export_json, export_csv

if __name__ == "__main__":
    agent = TopologicalAgent()
    results = agent.analyze_all()
    export_json(results, "results/analysis.json")
    export_csv(results, "results/analysis.csv")
    print("Analysis complete. Results exported.")
