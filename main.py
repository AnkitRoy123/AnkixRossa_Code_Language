import random

secure = [
    ('A', 'α'),
    ('B', 'ß'),
    ('C', '¢'),
    ('D', 'Ð'),
    ('E', '€'),
    ('F', 'Ғ'),
    ('G', '₲'),
    ('H', '#'),
    ('I', '!'),
    ('J', 'J'),
    ('K', 'Ҝ'),
    ('L', 'Ł'),
    ('M', '₥'),
    ('N', 'И'),
    ('O', 'Ø'),
    ('P', 'Þ'),
    ('Q', 'Ҩ'),
    ('R', '®'),
    ('S', '$'),
    ('T', '†'),
    ('U', 'Ů'),
    ('V', 'Ṽ'),
    ('W', 'Ш'),
    ('X', '✘'),
    ('Y', '¥'),
    ('Z', 'Z'),
    ('a', '@'),
    ('b', 'b'),
    ('c', '¢'),
    ('d', 'd'),
    ('e', '€'),
    ('f', 'ƒ'),
    ('g', 'g'),
    ('h', 'h'),
    ('i', '¡'),
    ('j', 'j'),
    ('k', 'k'),
    ('l', 'l'),
    ('m', 'm'),
    ('n', 'n'),
    ('o', 'o'),
    ('p', 'p'),
    ('q', 'q'),
    ('r', 'r'),
    ('s', '$'),
    ('t', '+'),
    ('u', 'µ'),
    ('v', 'v'),
    ('w', 'w'),
    ('x', '×'),
    ('y', 'y'),
    ('z', 'z'),
    (' ', '__'),
    ('0', '0000'),
    ('1', '0001'),
    ('2', '0010'),
    ('3', '0011'),
    ('4', '0100'),
    ('5', '0101'),
    ('6', '0110'),
    ('7', '0111'),
    ('8', '1000'),
    ('9', '1001'),
    ('.', '|')
]
print("Type 0 for real language to ")
print("code language and type 1 for")
print("code language to real language.")
x = str(input("\nEnter what number you want: "))
password = str(input("Enter your sentences: "))
def lang_to_code(s,p):
    for a,b in s:
      p = p.replace(a,b)
    print(p)
def code_to_lang(s,p):
    for a,b in s:
     p = p.replace(b,a)
    print(p)
def generate_nine_digit_number():
    number = random.randint(10000000000, 99999999999)
    return number
print("Translation:-")
match x:
  case "0":
    lang_to_code(secure, password)
    print()
    print(generate_nine_digit_number())
  case "1": code_to_lang(secure, password)
  case _ : print("Invalid input.")
