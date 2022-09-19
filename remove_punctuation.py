punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Oh !!!!Sorry....#$ for the [trouble]"
clean_str = ""
for char in my_str:
    if char not in punctuations:
        clean_str += char
print(clean_str)