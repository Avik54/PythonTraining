# function
def sum_(*vals): 
    total = 0
    for num in vals: 
        total += num 
    print(total) 
  
# function call 
sum_(1,2,3) # should return 6
sum_() # should return 0
sum_(5,7) # should return 12