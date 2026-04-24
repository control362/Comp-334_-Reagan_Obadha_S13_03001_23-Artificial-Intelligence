import json

path = 'football_analysis/notebooks/Football_Analysis.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        for i, line in enumerate(cell['source']):
            if "df['total_goals'].max() + 2" in line:
                cell['source'][i] = line.replace("df['total_goals'].max() + 2", "int(df['total_goals'].max()) + 2")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print('Notebook fixed.')
