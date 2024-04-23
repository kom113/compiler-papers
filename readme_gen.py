import os

def generate_toc(root_dir):
    header = """# compiler-papers
personal collections of compiler-related papers, papers are tagged with:
- [YEAR]: the year when the paper gets published.
- [CONFERENCE/JOURNAL/PREPRINT/DEGREE]: 
    - if the paper gets publishend on a conference or journal, it is tagged with corresponding conference / journal.
    - if the paper is a preprint, it is tagged with PREPRINT.
    - if the paper is a degree thesis, it is tagged with DEGREE.

"""
    toc = header + "# Table of Contents\n\n"
    for dir_name in os.listdir(root_dir):
        if os.path.isdir(dir_name) and not dir_name.startswith('.'):
            toc += f"## {dir_name}\n\n"
            for file_name in os.listdir(dir_name):
                if file_name.endswith('.pdf'):
                    toc += f"- {file_name}\n"
            toc += "\n"
    return toc

root_dir = "."  
toc = generate_toc(root_dir)
with open("README.md", "w") as f:
    f.write(toc)