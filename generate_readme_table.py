import os

# Path to your repo folder containing problems
folder_path = "path/to/your/problems/folder"

files = sorted(os.listdir(folder_path))  # sort alphabetically
table_lines = ["| # | Problem Title | Link |", "|---|---------------|------|"]

for idx, file in enumerate(files, 1):
    if file.endswith(".py"):  # only include Python files
        title = file.replace(".py", "").replace("_", " ").split(" ", 1)[-1]  # get readable title
        link = f"[Link]({file})"  # relative link
        table_lines.append(f"| {idx} | {title} | {link} |")

# Save table to README
with open("README.md", "w") as f:
    f.write("# DSA Problems Repository\n\n")
    f.write("\n".join(table_lines))

print("README.md generated successfully!")
