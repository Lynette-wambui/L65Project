print("🔍 Finding the binary representation of a number only( Please first try with 12 and 11).")
num = int(input("🧮 Enter a number: "))

# Get binary representation (without '0b' prefix)
binary = bin(num)[2:]
print("📦 Binary is:", binary)

("Finding the reversed bits of 12 and 11")
# Reverse the binary string
reversed_binary = binary[::-1]
print("🔁 Reversed binary is:", reversed_binary)

# Convert reversed binary back to decimal
reversed_num = int(reversed_binary, 2)
print("🎉 The number from reversed binary is:", reversed_num)

# Explain clearly what the reversed bit represents
print(f"💡 So, the reversed bits '{reversed_binary}' representing the decimal number {reversed_num}.")






import random

print("Let's compare numbers!")
print("Type 'greater', 'less' or 'equal'.")

score = 0

for i in range(3):
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"\n Which is true about {a} and {b}?")
    answer = input("Your answer (greater/ less/ equal): ").lower()

    # Check the correct answer
    if a > b and answer == "greater":
        print("Yes! You're right.")
        score += 1
    elif a < b and answer == "less":
        print("Good job! That's ccorrect.")
        score += 1
    elif a == b and answer == "equal":
        print("Yay! You got it.")
        score += 1
    else:
        print("Oops! Not quite.")
        if a > b:
            print(f"The right answer is: {a} is greater than {b}")
        elif a < b:
            print(f"The right answer is: {a} is less than {b}")
        else:
            print(f"The right answer is: {a} is equal to {b}")

print(f"\n All done! You got {score} out of three correct.")














# Ask user to enter a word
word = input("Enter a word: ")

print("\n Letters that appear only one time: ")

# Go through each letter
for letter in word:
    # Count how many times the letter appears
    if word.count(letter) == 1:
        print(letter)

word = input("Enter a word: ")

print("\nLetters that appear more than once:")

# Track and avoid printing duplicates
already_printed = set()

# Check each letter
for letter in word:
    if word.count(letter) > 1 and letter not in already_printed:
        print(letter)
        already_printed.add(letter)




print("Finding odd numbers from 1 to 10")
# Create an array of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Odd numbers in the list: ")

# Check each number
for num in numbers:
    if num % 2 != 0:
        print(num)





        import random 

print("😊 Let's find the ODD numbers!")
print("🎯 Odd numbers end in 1, 3, 5, 7, 9.")

# Show 5 random numbers 
numbers = random.sample(range(1, 100), 5)

print("\n👀 Look at these numbers:")
for num in numbers:
    print(num)

# Ask one by one: Is this number odd?
print("\n🧐 Ask one by one: Is this number odd?")
score = 0
for num in numbers:
    answer = input(f"\n🤔 Is {num} an odd number? (yes or no): ").lower()
    if (num % 2 == 1 and answer == "yes") or (num % 2 == 0 and answer == "no"):
        print("✅ Correct! 😄")
        score += 1
    else:
        print("❌ Incorrect. 😕")

print(f"\n🎉 Your total score is: {score} out of 5! 🥳")
