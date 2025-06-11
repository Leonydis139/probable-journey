from core.sat_solver_interface import SATSolverInterface
import os

class TopologicalAgent:
    def __init__(self, data_path="data/sat_instances"):
        self.interface = SATSolverInterface()
        self.data_path = data_path

    def list_instances(self):
        return [f for f in os.listdir(self.data_path) if f.endswith('.cnf')]

    def analyze_all(self):
        reports = {}
        for filename in self.list_instances():
            path = os.path.join(self.data_path, filename)
            result = self.interface.run_on_file(path)
            reports[filename] = {
                "order": result["order"],
                "reduction": result["complexity"]["reduction"],
                "steps": result["complexity"]
            }
        return reports
