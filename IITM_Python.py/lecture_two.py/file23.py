with open("name.txt", "r") as name_file:
  names = name_file.readlines()
  print(names)
  print(len(names))
count =0
for char in names:
    if char == ",":
      count+=1
      
print(len(names))