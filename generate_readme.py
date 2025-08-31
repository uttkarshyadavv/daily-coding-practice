import os

# Define the root directory to start scanning
root_dir = "."

# Initialize the list to hold the markdown content
readme_lines = [
    "# DSA Problems Repository\n",
    "This repository contains 192 DSA problems solved in Python.\n",
    "| Problem # | Problem Name | Link |",
    "|-----------|--------------|------|"
]

# Traverse through the directory and subdirectories
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.startswith("Prob") and file.endswith(".py"):
            # Extract problem number and name
            parts = file.split("_")
            prob_number = parts[0][4:]  # Extract number from 'Prob100'
            prob_name = "_".join(parts[1:]).replace(".py", "")
            
            # Create the relative path for the link
            rel_path = os.path.relpath(os.path.join(subdir, file), root_dir)
            
            # Add the entry to the markdown content
            readme_lines.append(f"| {prob_number} | {prob_name} | [Link]({rel_path}) |")

# Write the markdown content to README.md
with open("README.md", "w") as f:
    f.write("\n".join(readme_lines))

print("README.md generated successfully!")
