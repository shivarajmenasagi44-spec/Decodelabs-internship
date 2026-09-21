print("DEFENSIVE LOGIC:PASSWORD CHECKER")
print("=======================================")
print("---------------------------------------")
password=input("enter your password-->")
length=len(password)
if length<8:
    print("password strength-->weak")
    print("password length-->",length)
    print("score is 0")
    print("password is under 8 characters EXPONTIAL BRUTE FORCE RISK(immidiate fail)")
    print("===============================================sh")
    exit()

has_digit=any(char.isdigit() for char in password)
has_capital=any(char.isupper() for char in password)
symbols="!@#$%&*?"
has_symbols=any( not char.isalnum() for char in password)
has_unicode=any(ord(char)>127 for char in password)


score=sum([has_digit,has_capital,has_symbols])
reasons=[]
if not has_digit:
    reasons.append("missing a number [0-9]")
if not has_capital:
    reasons.append("missing a capital letter [A-Z]")
if not has_symbols:
    reasons.append("missing a  special character]")
if  has_unicode:
    reasons.append("unicode character is detected")

if score==3 and length>=12:
    strength="storng"
elif score>=2 and length>=8:
    strength="medium"  
else :
    strength="weak"  
print("password strength-->",strength)
print("password length-->",length)
print("password score-->",score)

if len(reasons)==0:
    print("password meets security requirement")
else:
    for reason in reasons:
        print("-",reason)
print("=====================================")
print("-------------------------------------")



