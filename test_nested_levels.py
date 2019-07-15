numbers = ["1","2","3",["4","5","6",["7","8","9", ["10", "11", "12", ["13", "14", "15"]]]]] 

class Counter: 
    def __init__(self, count): 
        self.count = count 
    def up_count(self): 
        self.count += 1 

counter = Counter(0)

def check_array(array): 
    contains_array = False 
    for i in range(len(array)): 
        if type(array[i]) == list:
            contains_array = True  
        while contains_array == True: 
            array = array[i]
            print(array)
            counter.up_count()
            print(counter.count)
            contains_array = False 
            check_array(array)

check_array(numbers)
print(f"{counter.count} levels beyond an array of strings")
