#  number 1
movies = ["kuninja" , 'batman' , "joker" , "spiderman"]
new_movies = ['avatar' , 'deadpool' , 'iron man' , 'hulk']

print("Old movie list :  "  , movies)
print("New movie list :  "  , new_movies)

#  number 2


num = [1, 2, 3, 4, 5]


added_numbers = num[0] + num[1] + num[2] + num[3] + num[4]


print('Sum of numbers: ' + str(added_numbers))


# number 3

large_numbers = [134242420, 9876543210, 14324244650, 5647382910]


index = int(input("Enter an index (0 to 3): "))

try:
    print(large_numbers[index])
except IndexError:
    print("Invalid index. Please enter a number between 0 and 3.")


# number 4


name = ["Sandro", "abashidze"]


print("Full name: " + name[0] + " " + name[1])
