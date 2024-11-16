#2) შექმენით სია და შეიტანეთ 10 სხვადასხვა მონაცემთა ტიპის მნიშვნელობა, შემდეგ 5 მონაცემს  შეუცვალეთ   მნიშვნელობა და შემდეგ დაპრინტეთ მთლიანი სია.

my_list = ['vashli', 'kakali', 'iogurti', 'mafani', 'atami', 'telefoni', 'leptopi', 'gitara', 'skami', 'marwyvi']

print('sia:', my_list)

my_list[0] = 'karebi'
my_list[1] = 'magida'
my_list[2] = 'pianino'
my_list[3] = 'sawoli'
my_list[4] = 'karebi'

print('ganaxlebuli sia:', my_list)

#3) სიაში ელემენტების ჯამი
#შექმენი სია, რომელიც შეიცავს რიცხვებს. დაწერე კოდი, რომელიც გამოითვლის ამ სიის ელემენტების ჯამს და დაბეჭდავს შედეგს.

num = [1, 2, 3, 4, 5]

num2= sum(num)

print("the sum of numbers : ", num2)

#4) სიის ყველა ელემენტის გაორმაგება
#შექმენი სია რიცხვებით. დაწერე კოდი, რომელიც თითოეული ელემენტის გაორმაგებულ მნიშვნელობას შეიცავს ახალ სიაში და დაბეჭდავს მას. 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

doubled = [x * 2 for x in numbers]

print(doubled)


#5) სიის ელემენტების გამრავლება
#შექმენი სია რიცხვებით და დაწერე კოდი, რომელიც გამოითვლის სიის ყველა ელემენტის ნამრავლს და დაბეჭდავს შედეგს.

numbers = [1, 2, 3, 4, 5]

product = 1
for number in numbers:
    product *= number

print(product)

 


