
text = """ Hello world!
This is a small example on slicing.
Let's see how it works"""

important_text = slice(1, 7)

sentences = text.split('\n')

for sentence in sentences:
    print(sentence[important_text])

a = [1, 2, 3, 4, 5]

a[2:4] = [9]
print(a)