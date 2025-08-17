import os

# Define the folder structure
folders = [
    "config",
    "data/raw",
    "data/processed",
    "docs",
    "notebooks",
    "src/agents",
    "src/api",
    "src/dashboards",
    "src/data_models",
    "src/etl",
    "src/genai",
    "src/nlp",
    "src/scraping",
    "src/utils",
    "tests"
]

files = {
    "requirements.txt": "",
    ".env": "",
    ".gitignore": "",
    "LICENSE": "",
    "README.md": "# HeadlineHive\n\nProject README goes here."
}


def create_folder_structure(folders, files):
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for filepath, content in files.items():
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Created file: {filepath}")

if __name__ == "__main__":
    create_folder_structure(folders, files)
