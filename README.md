# Smart Student Assistant

This project is a simple AI-like assistant that provides helpful suggestions based on user input.

---

## 🧠 Concept

The assistant analyzes user input using keyword matching and responds with relevant advice related to studies, stress, time management, and motivation.

---

## ⚙️ How it works

- Takes user input  
- Converts input to lowercase  
- Checks for keywords like "exam", "stress", "tired"  
- Provides appropriate suggestions  
- Runs continuously using a loop until user exits  

---

## 💻 Code

```python
# Smart Student Assistant

print("Welcome to Smart Student Assistant!")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Tell me your situation: ").lower()

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
