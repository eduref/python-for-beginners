import json

from os import listdir, mkdir
from os.path import isfile, join, isdir

onlyfiles_en = [f for f in listdir("./exercises") if isfile(join("./exercises", f))]
onlyfiles_de = [f for f in listdir("./aufgaben") if isfile(join("./aufgaben", f))]

import re
solution_marker = re.compile("#+ (add|write|type in) your (own )?code ((after|below) this line:?|here)")
solution_marker_german = re.compile("#+ schreibe deinen code unter dieser? zeile")

def filter_cell(cell, current_solution_marker):
    if cell["cell_type"] != "code":
        return cell
    cell["execution_count"] = 0
    cell["outputs"] = []
    code_lines = cell["source"]
    last_line = -1
    for line_number, line in enumerate(code_lines):
        folded_line = line.casefold()
        if current_solution_marker.match(folded_line):
            last_line = line_number
    if last_line == -1:
        print("Warning: Code cell does not contain a solution-marker.")
        print(cell["source"])
        return cell
    
    filtered_lines = code_lines[:(last_line + 1)]
    cell["source"] = filtered_lines
    return cell

if not isdir("./filtered"):
    mkdir("./filtered")
if not isdir("./filtered/exercises"):
    mkdir("./filtered/exercises")
if not isdir("./filtered/aufgaben"):
    mkdir("./filtered/aufgaben")

def handle_file(foldername, filename, current_solution_marker):
    print(f"Filtering {filename}")
    with open(f"./{foldername}/{filename}", encoding="UTF-8") as file:
        unfiltered = json.load(file)
        filtered = {
            "nbformat": unfiltered["nbformat"] if "nbformat" in unfiltered else None,
            "nbformat_minor": unfiltered["nbformat_minor"] if "nbformat_minor" in unfiltered else None,
            "metadata": unfiltered["metadata"] if "metadata" in unfiltered else None
        }
        filtered_cells = []
        for cell in unfiltered["cells"]:
            filtered_cells.append(filter_cell(cell, current_solution_marker))
        filtered["cells"] = filtered_cells
        with open(f"./filtered/{foldername}/{filename}", "w", encoding="UTF-8") as filtered_file:
            json.dump(filtered, filtered_file)
    print("Done!")
    print()

for filename in onlyfiles_en:
    handle_file("exercises", filename, solution_marker)

for filename in onlyfiles_de:
    handle_file("aufgaben", filename, solution_marker_german)

print("All solutions stripped successfully.")
