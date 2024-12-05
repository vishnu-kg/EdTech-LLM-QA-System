import os

def create_project_structure(base_path):
    # Define the directory structure
    dirs = [
        "assets",
        "src",
        "src/__init__.py",
        "src/logger.py",
        "src/vector_db.py",
        "src/qa_chain.py",
        "src/utils.py",
        "src/main.py",
    ]

    # Create directories and files
    for dir_path in dirs:
        full_path = os.path.join(base_path, dir_path)
        if '.' in dir_path:  # If it's a file, create it
            # Create the file if it doesn't exist
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as file:
                file.write("")  # Create an empty file
        else:
            # Create the directory if it doesn't exist
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")

    print("Project structure created successfully!")

# Set your desired project base path
base_path = os.getcwd()  # This will create the structure in the current working directory
create_project_structure(base_path)
