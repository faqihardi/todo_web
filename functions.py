
def get_todos(filepath="todos.txt"):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def writes_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Program ini berisi fungsi")
    print(get_todos())