import os

# Change this to the root folder of your repo
root_dir = "."

# Markdown header
readme_lines = [
    "# DSA Problems Repository\n",
    "This repo contains 192 DSA problems solved in Python.\n",
    "| Problem # | Problem Name | Link |",
    "|-----------|--------------|------|"
]

# Walk through the repo folders
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.startswith("Prob") and file.endswith(".py"):
            # Extract problem number and name
            parts = file.split("_")
            prob_number = parts[0][4:]  # Prob1 -> 1
            prob_name = "_".join(parts[1:]).replace(".py", "")
            
            # Relative link
            rel_path = os.path.relpath(os.path.join(subdir, file), root_dir)
            
            # Add markdown line
            readme_lines.append(f"| {prob_number} | {prob_name} | [Link]({rel_path}) |")

# Write to README.md
with open("README.md", "w") as f:
    f.write("\n".join(readme_lines))

print("README.md generated successfully!")
