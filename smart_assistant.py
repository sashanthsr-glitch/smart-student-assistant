# Smart Student Assistant

print("Welcome to Smart Student Assistant!")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Tell me your situation: ").lower()

    # Exit condition
    if user_input == "exit":
        print("\nGood luck! Stay consistent 👍\n")
        break

    elif "exam" in user_input or "test" in user_input:
        print("\nFocus on revision, practice important questions, and avoid learning new topics now.\n")

    elif "tired" in user_input or "sleep" in user_input:
        print("\nTake proper rest. A fresh mind improves productivity.\n")

    elif "time" in user_input or "busy" in user_input:
        print("\nPrioritize important tasks and create a simple schedule.\n")

    elif "stress" in user_input or "anxiety" in user_input:
        print("\nTake a short break, breathe deeply, and focus on one task at a time.\n")

    elif "motivation" in user_input:
        print("\nStart small. Once you begin, motivation will follow.\n")

    else:
        print("\nStay consistent, keep learning, and don’t overthink.\n")

    print("----------------------------------")

