from .corpus_loader import word_list, name_list


def encrypt(eggs, key):
  # encrypts a string
  key = key % 27
  text = ""
  for egg in eggs:
    unicode = ord(egg)
    shift = unicode + key

    # lowers
    if 97 <= unicode <= 122:
      if shift > 122:
        text += chr(shift-26)
      else:
        text += chr(shift)

    # upper
    elif 65 <= unicode <= 90:
      if shift > 90:
        text += chr(shift - 26)
      else:
        text += chr(shift)

    # nums and special characters
    else:
      text += egg

  return(text)

def decrypt(scrambled, key):
  # decrypts a string
  return encrypt(scrambled, 26-key)

def crack():
  # cracks an encoded string
  pass
