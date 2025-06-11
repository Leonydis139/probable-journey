import json, csv, os

def export_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def export_csv(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'Reduction', 'Lex Steps', 'Topo Steps', 'Order'])
        for fname, report in data.items():
            writer.writerow([
                fname,
                report['reduction'],
                report['steps']['lex_steps'],
                report['steps']['topo_steps'],
                report['order']
            ])
