#with open(r"C:\Users\LENOVO\Desktop\IRIS.csv", "r") as iris_file:
#    iris_data = iris_file.read().split("\n")
    
#print(iris_data)


with open(r"C:\Users\LENOVO\Desktop\IRIS.csv", "r") as iris_file:
    iris_data = iris_file.readlines()
 
irises = []   
for row in iris_data[1:]:
    #print((row).split(","))
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    
    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }

    irises.append(iris_dict)

print(irises)


#EXERCISE
f = open("hello_world.txt", "w")
f.write("Hello, World!")
f.close()

with open("hello_world.txt", "w") as f:
    f.write("Hello, World!")
#print(f)

with open("hello_world.txt", "a") as f:
    f.write("\nHow are you")
    
print(f)
