import random
import string as st
from zxcvbn import zxcvbn
from datetime import timedelta

ascii_lowercase = list(st.ascii_lowercase)
ascii_uppercase = list(st.ascii_uppercase)
digits = list(st.digits)
punctuation = list(st.punctuation)


def convert_seconds_to_readable(seconds):
     max_seconds = 10**8
     if seconds > max_seconds:
         return "'It will outlife you'"
     
     return str(timedelta(seconds=float(seconds)))


def Passwort_generieren(length):
    Passwort_part1 = []
    Passwort_part2 = []
    mind_zahl = 0
    
    if length <= 3:
        print("your desired password length was to short, it was expanded to 4 charachters")

    if True:
        mind_lowercase = random.choice(ascii_lowercase)
        mind_zahl += 1
        Passwort_part1.append(mind_lowercase) 

    if f_uppercase:
        mind_uppercase = random.choice(ascii_uppercase)
        mind_zahl += 1
        Passwort_part1.append(mind_uppercase)

    if f_digets:
        mind_digets = random.choice(digits)
        mind_zahl += 1
        Passwort_part1.append(mind_digets)

    if f_punctuation:
        mind_punctuation = random.choice(punctuation)
        mind_zahl += 1
        Passwort_part1.append(mind_punctuation)

    if (length - mind_zahl) > 0:
        for i in range((length - mind_zahl)):
            fail_save = True

            while fail_save:
                zahl = random.randint(1,4)
                
                if zahl == 1 and True:
                   passwort_lowercase_teil = random.choice(ascii_lowercase)
                   Passwort_part2.append(passwort_lowercase_teil)
                   fail_save = False

                elif zahl == 2 and f_uppercase == True:
                    passwort_uppercase_teil = random.choice(ascii_uppercase)
                    Passwort_part2.append(passwort_uppercase_teil)
                    fail_save = False

                elif zahl == 3 and f_digets == True:
                    passwort_digets_teil = random.choice(digits)
                    Passwort_part2.append(passwort_digets_teil)
                    fail_save = False

                elif zahl == 4 and f_punctuation == True:
                   passwort_punctuation_teil = random.choice(punctuation)
                   Passwort_part2.append(passwort_punctuation_teil)
                   fail_save = False


    Passwort_list = (Passwort_part1 + Passwort_part2)

    random.shuffle(Passwort_list)
    Passwort = ''.join(Passwort_list)

    return Passwort

length_pass = int(input("Please enter your desired password length: "))

input1 = input("Would you like your Password to contain 'Uppercase'? ")
input2 = input("Would you like your Password to contain 'Digets'? ")
input3 = input("Would you like your Password to contain 'Punctuation'? ")

f_uppercase = True if input1 == "Yes" or input1 == "yes" else False
f_digets = True if input2 == "Yes" or input2 == "yes" else False
f_punctuation = True if input3 == "Yes" or input3 == "yes" else False

result = zxcvbn(Passwort_generieren(length_pass))
print(result)
crack_times = result['crack_times_seconds']

print(f"Your generated Password is ---> {Passwort_generieren(length_pass)}")
print(f"Score: {result['score']}")
print(f"Offline Attack (1,000 guesses/second): {convert_seconds_to_readable(round(crack_times['offline_slow_hashing_1e4_per_second']))}")
        

