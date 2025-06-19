files = ["img_001.jpg", "img_002.jpg", "notes.txt"]
import re

def rename_files(pattern,replacement,file_list):
    dic = {}
    for file in file_list:
        if pattern in file:
            temp = re.sub(pattern,replacement,file)
            print("Renamed:",file,"->",temp)
            dic.update({file:temp})
        else:
            print("Unchanged:",file)
            dic.update({file:file})
    return dic

data = rename_files("img",'pic',files)
print(data)