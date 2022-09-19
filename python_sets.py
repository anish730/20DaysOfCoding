A = {'1', '2', '5', '7', '3'}
B = {'2', '5', '4', '6', '7'}

union = A | B
intersection = A & B
diff = A - B 
sym_diff = A ^ B
print("Union :", union)
print("Intersection :", intersection)
print("Difference :", diff)
print("Symmetric Difference :", sym_diff)