import sys

text = 'ю'
text_bytes = text.encode(encoding='utf-8')
real_text = text_bytes.decode(encoding='utf-8')

print(text)
print(text_bytes)
print(real_text)