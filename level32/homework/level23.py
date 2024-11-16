#დავალება: შექმენით ფუნქცია რომელიც, გამოიტანს ლუწ რიცხვზე even, ხოლო კენტზე odd-ს.
def check_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

while True:
    user_input = input('Enter your number or type "exit" to quit: ')
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    try:
        number = int(user_input)
        print(check_odd(number))
    except :
        print("Gtxovt sheiyvanet ricxvi!.")


#დავალება: შექმენით ფუნქცია, რომელიც გამოძახებისას მომხმარებელს შემატანინებთ რიცხვს, თუ რიცხვი იყო დადებითი, დაუპრინტეთ მისი უარყოფითი ვარიანტი, ხოლო თუ იყო უარყოფითი, დაუპრინტეთ დადებითი ვარიანტი.

#მაგ: input: 6 >>> output: -6
#input: -8 >>> output: 8
#input: 0 >>> output: 0
def negate_number(num):
    if num > 0:
        return -num
    elif num < 0:
        return -num
    else:
        return num

def main():
    while True:
        user_input = input("Enter your number or type 'exit'to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        try:
            number = float(user_input)
            result = negate_number(number)
            print(result)
        except ValueError:
            print("Gtxovt sheiyvanet ricxvi!.")


main()




#დავალება: Level 30-ის დავალება ვისაც არ გქონდათ დასრულებული, დასრულეთ.

#დავალება: საკლასო სამუშაოები ვისაც არ გქონდათ შესრულებული, შეასრულეთ.