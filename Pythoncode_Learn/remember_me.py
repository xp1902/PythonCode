import json

user_name = input("please input your name: ")
file = "user/" + user_name + ".json"
try:
    with open(file) as fp:
        user = json.load(fp)
except FileNotFoundError:
    with open(file, 'a') as fp:
        json.dump(user_name, fp)
        print("welcom you bro!!")
else:
    print("welcom you bro!!!" + user)
