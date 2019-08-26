count = 3
answer = ("It gets wet")
user_q = input("What happens when you throw the yellow rock into the red sea?")
question = ("What happens when you throw the yellow rock into the red sea?")

answer1=input(question)

while answer1 not in "It gets wet":
    count = 3
    print(question)
    print("Try again")
    break

else: 
    print("Correct answer")