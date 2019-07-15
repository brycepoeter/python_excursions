numbers = ["1","2","3",["4","5","6",["7","8","9"]]] 
numbers_new =[]
for i in range(len(numbers)): 
    if len(numbers[i]) == 1: 
        numbers_new.append(numbers[i])
    if len(numbers[i]) > 1: 
        for j in range(len(numbers[i])): 
            if len(numbers[i][j]) == 1: 
                numbers_new.append(numbers[i][j])
            if len(numbers[i][j]) > 1: 
                for k in range(len(numbers[i][j])): 
                    if len(numbers[i][j][k]) == 1: 
                        numbers_new.append(numbers[i][j][k]) 

print(numbers_new)
print(len("13"))
                    


