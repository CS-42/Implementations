print("Welcome to NumberPlay.py")
print("Type a number and type 'q/quit' to quit")

# FUNCTIONS
def check_input(i):
    if i == "q" or i == "quit":
        return True

    try:
        int(i)
    except ValueError:
        print("Error: Please type numbers!")
        return False
    
    if len(i) > 10:
        print("Error: Digits must be 10 or less!")
        return False

    return True

def give_output(i):
    if not i[0] == "q":
        user_input_list = list(i)
    
        numbers = [int(n) for n in user_input_list]

        is_even = lambda n: n % 2 == 0

        numbers = [n for n in numbers if is_even(numbers.index(n) + 1)]

        sum_numbers = list(str(sum(numbers)))
        
        sum_numbers = [int(n) for n in sum_numbers]

        result = sum(sum_numbers)

        print(result)

# END USER

user_input = ""

while not user_input.lower() == "q" or user_input.lower() == "quit":
        # GETTING USER INPUT
        user_input = input("> ").lower()
        
        # PROCEEDING IF INPUT IS VALID
        if not check_input(user_input):
            continue
        else:
            give_output(user_input)

print("Good Bye!")
