
filename = 'E:/COLDDEMO/Python/src/FirstDay/文件读取/aa.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


filename1 = 'E:/COLDDEMO/Python/src/FirstDay/文件读取/bb.txt'
with open(filename1, 'a') as file_object:
 file_object.write("\n我是附加的1234")


 import json
numbers = [2, 3, 5, 7, 11, "ddd"]
filename = '/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)