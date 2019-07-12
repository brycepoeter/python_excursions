def check_for_duplicates(string): 
    b = sorted(string)
    marker = True
    for i in range(1, len(string)): 
        if b[i] == b[i-1]: 
            marker = False
            break
    if marker == True: 
        print("It has all unique characters")
    else: 
        print("It has some repeats")


check_for_duplicates("sarah")
