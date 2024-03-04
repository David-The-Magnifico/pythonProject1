sentence = input("Enter a sentence: ")

uppercase = 0
lowercase = 0

for char in sentence:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("UPPER CASE", uppercase)
print("LOWER CASE", lowercase)
