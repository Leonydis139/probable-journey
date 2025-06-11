import gradio as gr
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core')))
from sat_solver_interface import SATSolverInterface

solver = SATSolverInterface()

def process_input(cnf_text):
    try:
        lines = cnf_text.strip().split("\n")
        clauses = [[int(x) for x in line.split() if x != "0"] for line in lines if line.strip()]
        num_vars = max(abs(x) for clause in clauses for x in clause)
        result = solver.solver.solve(clauses, num_vars)
        return f"""Optimal order: {result['order']}
Lex steps: {result['complexity']['lex_steps']}
Topo steps: {result['complexity']['topo_steps']}
Reduction: {result['complexity']['reduction']:.1f}%
Persistence: {result['persistence']}"""
    except Exception as e:
        return f"Error: {e}"

iface = gr.Interface(fn=process_input,
    inputs=gr.Textbox(lines=6, label="SAT CNF Input (one clause per line, 0 ends clause)"),
    outputs="textbox",
    title="Topological SAT Solver"
)

if __name__ == "__main__":
    iface.launch()
