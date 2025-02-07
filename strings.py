text = "Hello, World!"
print(text.lower())
print(text.replace("World", "Python"))

def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))  # Output: nohtyP

text = "apple,banana,orange"
parts = text.split(",")  # Splits by comma
print(parts[1])  # Output: "banana"

text = "Hello, World!"
substring = text[0:5]  # Extracts characters from index 0 to 4
print(substring)  # Output: "Hello"

text = "Hello, World!"
index = text.find("World")  # Finds the starting index of "World"
substring = text[index:]  # Extracts from "World" to the end
print(substring)  # Output: "World!"

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # Output: True