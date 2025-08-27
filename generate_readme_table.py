import os
import re

PROBLEM_DIR = '.'  # Update if problems are in a subfolder

pattern = re.compile(r'Prob(\d+)_([^.]+)\.py')

problems = []

for filename in os.listdir(PROBLEM_DIR):
    match = pattern.match(filename)
    if match:
        num = int(match.group(1))  # Convert to integer for proper sorting
        name = match.group(2).replace('_', ' ')
        link = f'[{filename}]({filename})'
        problems.append((num, name, link))

# Sort by problem number
problems.sort(key=lambda x: x[0])

# Markdown table header
header = '| No. | Problem Description | File Name |\n|-----|--------------------|-----------|'
rows = [f'| {num} | {name} | {link} |' for num, name, link in problems]
table = header + '\n' + '\n'.join(rows)

print(table)
