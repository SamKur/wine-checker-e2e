import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

''' In terminal log should look like - 
[2025-09-07 13:32:11, 261]: Creating empty file: templates\index.html
[2025-09-07 13:32:11, 261]: Creating empty file: app.py
'''

project_name = "datascience"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py",
    "requirements.txt",
    "README.md"
]

for file in list_of_files:
    filepath = Path(file)

    # Create parent directory
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # Create file if not exists or empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        logging.info(f"Creating empty file: {filepath}")
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"{filepath.name} already exists")
