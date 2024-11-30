name = 'Yurii Solonovich'

letters = ['Y', 'u', 'r', 'i', 'i', 'S', 'o', 'l', 'o', 'n', 'o', 'v', 'i', 'c', 'h']
letters_str = "_".join(letters)
print( letters_str)

s = letters_str
su = s.upper()
print(su)

text1 = su

ascii_upper = [ord(symbol) for symbol in text1]
print(ascii_upper)

sl = s.lower()
print(sl)

text2 = sl

ascii_lower = [ord(symbol) for symbol in text2]
print(ascii_lower)

print('maximum:', max(max(ascii_upper), max(ascii_lower)))
print('minimum:', min(min(ascii_upper), min(ascii_lower)))
