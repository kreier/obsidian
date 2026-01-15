# Compare my two Obsidian vaults: Quartz and Obsidian
# The main one to operate on is Quartz: /content
# The other is a copy in Obsidian: /vault/saiht

import os

# Define your folders
folder_quartz = "../../quartz/content/"
folder_obsidian = "../vault/saiht/"

def get_files_with_size(folder, base_folder):
    """Return a dict of relative_path -> size for all files in a folder."""
    files = {}
    for root, _, filenames in os.walk(folder):
        for f in filenames:
            path = os.path.join(root, f)
            try:
                size = os.path.getsize(path)
                rel_path = os.path.relpath(path, base_folder)
                files[rel_path] = size
            except OSError:
                pass  # skip files we can't access
    return files

# Collect files from both folders
files_quartz = get_files_with_size(folder_quartz, folder_quartz)
files_obsidian = get_files_with_size(folder_obsidian, folder_obsidian)

# Compare by filename only (not path)
names_quartz = {os.path.basename(f): f for f in files_quartz}
names_obsidian = {os.path.basename(f): f for f in files_obsidian}

same_name = set(names_quartz.keys()) & set(names_obsidian.keys())
same_name_same_size = [f for f in same_name 
                       if files_quartz[names_quartz[f]] == files_obsidian[names_obsidian[f]]]
same_name_diff_size = [f for f in same_name 
                       if files_quartz[names_quartz[f]] != files_obsidian[names_obsidian[f]]]

only_in_quartz = set(names_quartz.keys()) - set(names_obsidian.keys())
only_in_obsidian = set(names_obsidian.keys()) - set(names_quartz.keys())

# Markdown counts
markdown_quartz = [f for f in files_quartz if f.endswith(".md")]
markdown_obsidian = [f for f in files_obsidian if f.endswith(".md")]

# Print overview
print("=== Overview ===")
print("Files with same name in both folders:", len(same_name))
print("Files with same name and same size:", len(same_name_same_size))
print("Files with same name but different size:", len(same_name_diff_size))
print("Markdown files in quartz:", len(markdown_quartz))
print("Markdown files in obsidian:", len(markdown_obsidian))
print("Files only in quartz:", len(only_in_quartz))
print("Files only in obsidian:", len(only_in_obsidian))

# Print detailed lists (with relative paths)
print("\n=== Detailed Output ===")

print("\nFiles with same name but different size:")
for f in same_name_diff_size:
    q_path = names_quartz[f]
    o_path = names_obsidian[f]
    print(f"  - {f}")
    print(f"    Quartz: {q_path} ({files_quartz[q_path]} bytes)")
    print(f"    Obsidian: {o_path} ({files_obsidian[o_path]} bytes)")

print("\nFiles only in quartz:")
for f in only_in_quartz:
    print("  -", names_quartz[f])

print("\nFiles only in obsidian:")
for f in only_in_obsidian:
    print("  -", names_obsidian[f])
