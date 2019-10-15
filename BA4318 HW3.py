age = int(input("How old are you? "))

if age>19:
    print("You 're adult")
elif age<=19 and age>10:
    print("You are adolescent")
elif age>1 and age<=10:
    print("You are child")
else:
    print("You are infant")