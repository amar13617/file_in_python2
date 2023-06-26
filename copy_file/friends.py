friends = input('Enter three friend names {no spaces, please}').split(',')

people = open(r'copy_file/people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] #used to remove \n from strip method
print(people_nearby)

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friends}is nearby! Meet up with them')
    nearby_friends_file.write(f'{friend}\n')
    
nearby_friends_file.close()