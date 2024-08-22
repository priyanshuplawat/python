import string
text = "HII my name is priyanshu plawat i m from Ghaziabad 134 %#hy5$3"
letter_count = 0
digit_count = 0
special_symbol_count = 0
for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char in string.punctuation or not char.isspace():
        special_symbol_count += 1
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Special Symbols: {special_symbol_count}")
