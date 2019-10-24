#rot13
OFFSET_LOWER = ord('a')
OFFSET_UPPER = ord('A')

def rot13(text):
  rot13_text = ''
  for i in range(len(text)):
    ch = text[i]
    if ch.isalpha():
      if(ch.islower()):
        offset = OFFSET_LOWER
      else:
        offset = OFFSET_UPPER
      rot13_text += chr(((ord(ch)-offset+13)%26+offset))
    else:
      rot13_text += ch
  return rot13_text

plain_text = input("Enter the string: ")
print(rot13(plain_text))
print(rot13(rot13(plain_text)))
