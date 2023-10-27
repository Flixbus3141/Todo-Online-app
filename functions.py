def get_todos(filepath="ToDolist.txt"):
    """
    Read a textfile and returns the
    todo items in that file.
    """
    with open(filepath,"r") as file:
        todos = file.readlines()
    return todos

def get_theme(index, filepath="Themes.txt"):
    """
    Read a textfile and returns the
    todo items in that file.
    """
    with open(filepath,"r") as file:
        themes = file.readlines()
    return themes[index]


def write_todos(ToDolist_arg, filename="ToDolist.txt",):
    """Writes the given list into a textfile"""
    with open(filename, "w") as file:
            file.writelines(ToDolist_arg)