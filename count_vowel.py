vowel = {'a', 'e', 'i', 'o', 'u'}

string = "Hello World"

count = {}.fromkeys(vowel, 0)

for char in string:
    if char in vowel:
        count[char] += 1
print(count)