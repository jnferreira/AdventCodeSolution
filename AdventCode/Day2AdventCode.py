def check_smallquantity(arr_test):
    arr = arr_test
    dict = {}

    for index, charac in enumerate(arr):
        dict[charac] = 0
        
    for index, charac in enumerate(arr):
        for di in dict:
            if di == charac:
                dict[di] += 1
   
    dict = {key:val for key, val in dict.items() if val != 1}

    return(dict)
    
def check_mediumquantity(lines):
    dict_array = []

    for line in lines: 
        dict_array.append(check_smallquantity(line))
    
    return(dict_array)

def check_dictmediumqt(da):
    dict_cs = {'2': 0, '3': 0}
    
    for d in da:  
        flag = True
        flag2 = True       
        for dx in d.values():
            

            if dx == 2:

                if flag:
                    dict_cs['2'] += 1
                    flag = False
                else:
                    dict_cs['2'] += 0

            elif dx == 3:
                if flag2:
                    dict_cs['3'] += 1
                    flag2 = False
                else:
                    dict_cs['3'] += 0

    return(dict_cs)

text_file = open("input_day2.txt", "r")
lines = text_file.read().split('\n')

test1 = check_mediumquantity(lines)
test1_1 = check_dictmediumqt(test1)
print(test1_1)