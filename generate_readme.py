import os
import re

root_dir = "."  # root folder of your repo

# Markdown header
readme_lines = [
    "# DSA Problems Repository\n",
    "This repository contains 192 DSA problems solved in Python.\n",
    "| Problem # | Problem Name | Link |",
    "|-----------|--------------|------|"
]

problems = []

# Traverse repo files
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        match = re.match(r'Prob(\d+)_([\w\d_]+)\.py', file)
        if match:
            prob_number = int(match.group(1))  # numeric problem number
            prob_name = match.group(2)
            rel_path = os.path.relpath(os.path.join(subdir, file), root_dir)
            problems.append((prob_number, prob_name, rel_path))

# Sort problems by numeric order
problems.sort(key=lambda x: x[0])

# Write to markdown
for prob_number, prob_name, rel_path in problems:
    readme_lines.append(f"| {prob_number} | {prob_name} | [Link]({rel_path}) |")

with open("README.md", "w") as f:
    f.write("\n".join(readme_lines))

print("README.md generated in numeric order successfully!")
