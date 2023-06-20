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

    if int(i) < 0:
        print("Error: Negatives not allowed!")
        return False

    if " " in i:
        print("Error: Blank spaces found!")
        return False

    return True


def give_output(i):
    if not i[0] == "q":
        user_input_list = list(i)

        numbers = [int(n) for n in user_input_list]

        res = []

        for num in range(len(numbers)):
            if (num+1) % 2 == 0:
                res.append(numbers[num])

        sum_numbers = sum(res)

        if len(str(sum_numbers)) == 2:
            while not len(str(sum_numbers)) == 1:
                str_sum_numbers = str(sum_numbers)
                new_sum = int(str_sum_numbers[0]) + int(str_sum_numbers[1])
                sum_numbers = new_sum

        print(sum_numbers)


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
