import os


def find_files(suffix='c', path=''):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not suffix.startswith('.'):
        suffix = '.' + suffix

    if path == '':
        path = os.getcwd()

    output_files_list = []

    find_files_recursively(suffix, path, output_files_list)

    return output_files_list

def find_files_recursively(suffix, path, output_files_list):
    directory_content = os.listdir(path)
    for entry in directory_content:
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path) and str(entry).endswith(suffix):
            output_files_list.append(entry)
        elif os.path.isdir(full_path):
            find_files_recursively(suffix, full_path, output_files_list)
    

if __name__ == '__main__':
    folder_path = os.path.join(os.getcwd(), 'testdir')

    files = find_files('.c', folder_path)
    print(files)
    #['a.c', 'b.c', 'a.c', 't1.c']

    # without dot in suffix
    files = find_files('c', folder_path)
    print(files)
    #['a.c', 'b.c', 'a.c', 't1.c']

    #without folder path
    files = find_files('.c')
    print(files)
    #['a.c', 'b.c', 'a.c', 't1.c']

    files = find_files('.h', folder_path)
    print(files)
    #['a.h', 'b.h', 'a.h', 't1.h']

    #nonexistent
    files = find_files('.jpg', folder_path)
    print(files)
    #[]