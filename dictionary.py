my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict.get("age"))
print(my_dict.keys())

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)