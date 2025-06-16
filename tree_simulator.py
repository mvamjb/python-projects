fs = {
  "root": {
    "folderA": {
      "file1.txt": None,
      "file2.txt": None
    },
    "folderB": {
      "subfolder": {
        "file3.txt": None
      }
    },
    "readme.md": None
  }
}


def print_tree(node : dict[str,any],level : int = 0) -> None:
    for name, subnode in node.items():
        if subnode is None:
            print('  '*level,name)
        else:
            print("  " * level,name+'/')
            print_tree(subnode,level+1)


print_tree(fs,0)