my_str = "Hello this Is an Example With cased letters"

words = [word.lower() for word in my_str.split()]

words.sort()

for w in words:
   print(w)