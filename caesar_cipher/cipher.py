from .corpus_loader import word_list, name_list
import re


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

def crack(shells):
    # finds possible solution to scrambled eggs, i mean words...
    humpty_dumpty = []
    for i in range(26):
        humpty_dumpty.append(encrypt(shells, i))

    # code below taken and altered from demo:
    for i in humpty_dumpty:
        word_count = count_words(i)
        percentage = int(word_count / len(i.split()) * 100)
        if percentage > 50:
            return i
    return ""

# taken from demo
def count_words(text):
    # returns a count of real words
    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1
        else:
            pass
            # print('not english word or name', word)

    return word_count


