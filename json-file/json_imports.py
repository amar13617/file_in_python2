import json

file = open('json-file/friends_json.txt', 'r')
file_contents = json.load(file)
print(file_contents) #read file and turns into dict.
