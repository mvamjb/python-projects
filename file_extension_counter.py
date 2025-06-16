fs = {
  "root": {
    "folderA": {
      "file1.txt": None,
      "file2.png": None,
      "file3.jpg": None,
      "file4.png": None,
      "file5.txt": None
    },
    "folderB": {
      "subfolder": {
        "file6.jpg": None,
        "file7.jpg": None,
        "file8.txt": None
      }
    },
    "readme.md": None
  }
  
}


def count_extensions(node,counts) -> dict[str,int]:
    for name, subnode in node.items():
        if subnode is None:
            extension = name.split(".",1)[1]
            counts[extension] = counts.get(extension,0) + 1
        else:
            count_extensions(subnode,counts)
    return counts
    
  
            

count = count_extensions(fs, {})
print(count)