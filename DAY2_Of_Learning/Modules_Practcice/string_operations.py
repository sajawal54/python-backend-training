import string
def to_upper(text):
   return text.upper()


def to_lower(text):
  return text.lower()

def count_characters(text):
  return len(text)


def reverse_string(text):
    reverse = " "

    for letter in text:
       reverse = letter + reverse

    return reverse
  