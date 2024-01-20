import json

from os import listdir, mkdir
from os.path import isfile, join, isdir

onlyfiles = [f for f in listdir("./exercises") if isfile(join("./exercises", f))]

import re
solution_marker = re.compile("#+ (add|write|type in) your (own )?code ((after|below) this line:?|here)")


def filter_cell(cell):
    if cell["cell_type"] != "code":
        return cell
    cell["execution_count"] = 0
    cell["outputs"] = []
    code_lines = cell["source"]
    last_line = -1
    for line_number, line in enumerate(code_lines):
        folded_line = line.casefold()
        if solution_marker.match(folded_line):
            last_line = line_number
    if last_line == -1:
        print("Warning: Code cell does not contain a solution-marker.")
        print(cell["source"])
        return cell
    
    filtered_lines = code_lines[:(last_line + 1)]
    cell["source"] = filtered_lines
    return cell

if not isdir("./filtered_exercises"):
    mkdir("./filtered_exercises")

for filename in onlyfiles:
    print(f"Filtering {filename}")
    with open(f"./exercises/{filename}", encoding="UTF-8") as file:
        unfiltered = json.load(file)
        filtered = {
            "nbformat": unfiltered["nbformat"],
            "nbformat_minor": unfiltered["nbformat_minor"],
            "metadata": unfiltered["metadata"]
        }
        filtered_cells = []
        for cell in unfiltered["cells"]:
            filtered_cells.append(filter_cell(cell))
        filtered["cells"] = filtered_cells
        with open(f"./filtered_exercises/{filename}", "w", encoding="UTF-8") as filtered_file:
            json.dump(filtered, filtered_file)
    print("Done!")
    print()

