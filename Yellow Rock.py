def get_answer(prompt):
    answer = input(prompt)

    while answer not in ("It gets wet"):
        answer = input(prompt)
    return answer
    else:
        print("Incorrect try again")

print(get_answer("What happens when you throw a yellow rock into the red sea? "))
