letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'.
new_str = ''
for letter in letters:
    if not letter.isupper():
        new_str += letter
letters = new_str
print(letters)
