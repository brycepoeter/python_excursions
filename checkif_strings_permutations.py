# Given two strings, write a method to decide if one is a permutation of the other  
def check_strings_permutations(str1, str2): 
    sorted_1 = sorted(str1)
    sorted_2 = sorted(str2)
    if len(str1) == len(str2): 
        for i in range (len(str1)): 
            if sorted_1[i] != sorted_2[i]: 
                print("These strings are not permutations")
                break
        else: 
            print("These strings are permutations")
    else: 
        print("These strings are not permutations")

check_strings_permutations("stupide", "dtupise")