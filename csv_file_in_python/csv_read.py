file = open(r'csv_file_in_python/csv_data.txt', 'r')
lines = [f.strip() for f in file.readlines()]
file.close()
#print(lines)

for line in lines[1:]:
    person_data = line.split(',')
    #print(person_data)
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]
    
    print(f'{name.title()} is {age}, studying{degree} at {university}')
    
sample_csv_value = ','.join(['Rolf',25,'Mit','Computer'])
print(sample_csv_value)