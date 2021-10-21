yes = "True"
no = "False"
what = "False | False"
a = input()
while(a):
    if a == "SP" or a == "PR" or a == "RS":
        print(yes)
    elif a == "SS" or a == "PP" or a == "RR":
        print(what)
    else:
        print(no)
    a = input()
