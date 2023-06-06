#!/usr/bin/python3

output = ""
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) not in ['q', 'e']:
        output += chr(char_code)

print(output)
