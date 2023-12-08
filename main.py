import os as o, shutil as s

from_dir = "D:/Downloads"
to_dir = "D:/Uploads"

list = o.listdir(to_dir)
list1 = o.listdir(from_dir)

types = {
  ".txt", ".doc", ".docx", ".pdf"
}

if list == []:
  x = "no files"
elif list != []:
  x = list 

if list1 == []:
  y = "no files"
elif list1 != []:
  y = list1 

print("Uploads folder has"+ {x} + "in it")
print("Downloads folder has"+ {y} +"in it")
for i in list1:
  name, extension =  o.path.splitext(i)
  print("name of file is "+ {name} "and its file type is" + {extension})
  if extension == "":
    continue
  else:
    for t in types:
      if extension == t:
        path1 = from_dir + '/' + name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + name
        if o.path.exists(path2):
          print("Moving " +{name})
          s.move(path1, path3)
        else:
          o.makedirs(path2)
          print("Moving "+ {name})
          s.move(path1, path3)
