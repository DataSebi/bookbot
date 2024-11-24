path_to_file = "books/frankenstein.txt"
print(f"--- Begin report of {path_to_file} ---")

chars = {}
with open(path_to_file) as f:
    file_contents = f.read()

word_count = len(file_contents.split())
print(f"{word_count} words found in the document")

file_contents = [char.lower() for char in file_contents]
for char in file_contents:
    char = char.lower()
    char_count = chars.get(char)
    if char_count:
        chars[char] = char_count + 1
    else:
        chars[char] = 1
    
for char in chars:
    print(f"The '{char}' character was found {chars[char]} times")
print("--- End report ---")