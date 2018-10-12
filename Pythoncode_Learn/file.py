string = ""
birthday = input("please input your birthday num as a numstring: ")
with open('pi_digits.txt') as fp:
    for line in fp:
        string += line.strip()
if birthday in string:
    print("your birthday is in the first million digits of pi")
else:
    print("regret, your birthday is not in the first million digits of pi")
