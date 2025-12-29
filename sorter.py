import os
import shutil

def sorter(suffixes, name, directory):
    """Sorts files in a directory into a new folder based on their extensions.

    Moves all files in `directory` that end with any of the extensions in `suffixes` 
    into a folder named `name`. Creates the folder if it does not exist.

    Args:
        suffixes (set[str]): Set of file extensions to move.
        name (str): Name of the folder to create for matching files.
        directory (str): Path to the directory containing the files to sort.

    Raises:
        PermissionError: If the program does not have permission to move files.
    """
    suffixes = {s.lower().lstrip('.') for s in suffixes}
    count = 0

    if not os.path.isabs(directory):
        directory = os.path.join(os.path.expanduser("~"), directory)
    directory = os.path.abspath(directory)

    target_dir = os.path.join(directory, name)
    os.makedirs(target_dir, exist_ok=True)

    for file in os.listdir(directory):
        src = os.path.join(directory, file)
        if os.path.isfile(src) and file.lower().split('.')[-1] in suffixes:
            dst = os.path.join(target_dir, file)
            try:
                shutil.move(src, dst)
                count += 1
            except PermissionError:
                raise PermissionError(f"Permission denied while moving: {file}")
            except Exception as e:
                raise RuntimeError(f"Failed to move {file}: {e}")

    print(f"{count} files were successfully moved")


repetitions = int(input("How many file types would you like to group together? "))
extensions = set()
for count in range(repetitions):
    extensions.add(input(f"File type {count + 1}: ").strip().lstrip('.'))

folder_name = input("What do you want to name the folder? ")
target_directory = input("What folder do you wish to sort inside? ")

sorter(extensions, folder_name, target_directory)