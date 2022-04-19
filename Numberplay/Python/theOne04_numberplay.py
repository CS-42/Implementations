# function to add the digits together
def add_dig(m):
    if m > 9:
        mstr = str(m)
        i = 0
    out = 0
    while i < len(mstr):
        out += int(mstr[i])
        i += 1
    return out

# input validation
num = "zero"
while True:
        if num.isnumeric() == True and len(num) <= 10:
            break

        elif num.isnumeric() == False:
            num = input("Input: ")

        elif len(num) > 10:
            print("Error: Number can't exceed 10 digits.")
            num = input("Input: ")

# main
total = 0
numstr = str(num)
i = 0
while i < len(numstr):
    if i % 2 != 0:
        total += int(numstr[i])
    i += 1

while True:
    if total > 9:
        total = add_dig(total)
    else:
        print("Output:", total)
        break
