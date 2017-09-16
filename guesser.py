import random
import string
import time

passwordvalue = input("Enter a password(lowercase and numbers)")
t0 = time.time()
passwordguess = ""
guesses = 0
chars=string.ascii_lowercase+string.digits
charslength=len(chars)

def passwordset(size=len(passwordvalue), chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for _ in range(size))

s = set()
while len(s) < charslength**len(passwordvalue):
    s.add(passwordset())


def password(size=len(passwordvalue), chars="".join(s)):
    return "".join(random.choice(chars) for _ in range(size))

while passwordguess != passwordvalue:
    passwordguess = password()
    while passwordguess not in s:
        passwordguess = password()
    print(passwordguess)
    s.remove(passwordguess)
    guesses = guesses+1
print(guesses, "guesses")
t1 = time.time()
print (t1-t0)
