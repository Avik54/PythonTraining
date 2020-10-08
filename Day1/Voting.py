age = input("Enter your age in years: \n")
ageNum = int(age)
ageInMonth = ageNum * 12

if ageNum>=18:  
    print(f"You are eligible for voting");  
    print(f"You are {ageInMonth} months old");
else:  
    print(f"You are ineligible for voting");  
    print(f"You are {ageInMonth} months old");cls
