import os
import re

# Directory containing your problem files
PROBLEM_DIR = '.'  # Update if problems are in a subfolder

# Regex to match your file naming pattern
pattern = re.compile(r'Prob(\d+)_([^.]+)\.py')

rows = []
for filename in sorted(os.listdir(PROBLEM_DIR)):
    match = pattern.match(filename)
    if match:
        num = match.group(1)
        # Convert underscores to spaces and capitalize
        name = match.group(2).replace('_', ' ')
        link = f'[{filename}]({filename})'
        row = f'| {num} | {name} | {link} |'
        rows.append(row)

# Markdown table header
header = '| No. | Problem Description | File Name |\n|-----|--------------------|-----------|'
table = header + '\n' + '\n'.join(rows)

# Print or write to README.md
print(table)
# Optional: To write to file
# with open('README.md', 'a') as f:
#     f.write('\n' + table + '\n')
