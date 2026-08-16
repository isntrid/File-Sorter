import os
import shutil

def move_file(directory, file, target_dir, suffixes):
    src = os.path.join(directory, file)
    if os.path.isfile(src) and file.lower().split('.')[-1] in suffixes:
        dst = os.path.join(target_dir, file)
        try:
            shutil.move(src, dst)
            return True
        except PermissionError:
            raise PermissionError(f"Permission denied while moving: {file}")
        except Exception as e:
            raise RuntimeError(f"Failed to move {file}: {e}")


def normalize_directory(dir):
    if not os.path.isabs(dir):
        return os.path.join(os.path.expanduser("~"), dir)
    return os.path.abspath(dir)


def sorter(suffixes, name, directory):
    success_count = 0
    suffixes = {s.lower().lstrip('.') for s in suffixes}

    directory = normalize_directory(directory)
    target_dir = os.path.join(directory, name)
    os.makedirs(target_dir, exist_ok=True)

    for file in os.listdir(directory):
       if move_file(directory, file, target_dir, suffixes):
           success_count += 1


    print(f"{success_count} files were successfully moved")

def main():
    repetitions = int(input("How many file types would you like to group together? "))
    extensions = set()
    for count in range(repetitions):
        extensions.add(input(f"File type {count + 1}: ").strip().lstrip('.'))

    folder_name = input("What do you want to name the folder? ")
    target_directory = input("What folder do you wish to sort inside? ")
    sorter(extensions, folder_name, target_directory)

if __name__ == '__main__':
    main()
