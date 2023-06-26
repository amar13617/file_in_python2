my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)

user_name = input('Enter your name')

my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()

write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")

write_file.close()

#Context managers for working with files.

with open("example.txt", "r") as example_file: #There is no need to close the file.
    print(example_file.read())
    
    
with open("write_example.txt", "w") as write_file:
    write_file.write("Welcome to the world, write_example.txt!")

with open("write_example.txt", "a") as write_file:
    write_file.write("\nNow you have two lines! You're growing up so fast!")
    



