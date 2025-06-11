from .spectral_ph_sat_solver import TopologicalSATSolver, parse_dimacs

class SATSolverInterface:
    def __init__(self, alpha=0.7, max_filtration=2.0):
        self.solver = TopologicalSATSolver(alpha, max_filtration)

    def run_on_file(self, cnf_path):
        clauses, num_vars = parse_dimacs(cnf_path)
        return self.solver.solve(clauses, num_vars)

    def run_on_clauses(self, clauses):
        num_vars = max(abs(lit) for clause in clauses for lit in clause)
        return self.solver.solve(clauses, num_vars)
