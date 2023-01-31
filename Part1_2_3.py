
#PART 1,2,3 SOURCE CODE

#info.txt is the text file for part 3


#intialization of variables

star_list = [0,0,0,0]  # default star list
q_or_y = ""  # null string
oucms = 0  # deafult outcome number
nulls = [] # null list


# functions

def scorelist():   # storing the output to the text file "info.txt" 
    
    with open("info.txt", "w") as f:    
        for x in nulls:
            if x == [120,0,0]:
                
                print("progress - ", x, file=f)
            if x == [100,20,0] or x == [100,0,20]:
                print("progress (module trailer) - ", x, file=f) 
            if x ==  [80,40,0] or x ==  [80,20,20] or x == [80,0,40] or x == [60,60,0] or x == [60,40,20] or x == [60,0,60] or x == [40,80,0] or x == [40,60,20] or x == [40,40,40] or x == [40,40,40] or x == [20,100,0] or x == [20,80,20] or x == [20,60,40] or x ==[20,40,60] or x == [0,120,0] or x == [0,100,20] or x == [0,80,40] or x == [0,60,60]:
                print("Module retriever - ", x, file=f)   
            if x ==  [40,0,80] or x== [20,20,80] or x== [20,0,100] or x ==[0,20,100] or x ==[0,0,120]:
                print("Exclude - ", x, file=f)  


def read_file():   # Reading all the data records stored in text file "info.txt"
    with open('info.txt', 'r') as file:
        text = file.read()
        print("part 3:")
        print(text)    
    


def histogram():   # printing the summary of outputted results in a histogram
    print("Histogram")
    print("progress", star_list[0],'   : ','*'* star_list[0])
    print('Trailer ',star_list[1],'   : ','*'* star_list[1])
    print('Retriever',star_list[2],'  : ','*'* star_list[2])
    print('Excluded ',star_list[3],'  : ','*'* star_list[3] )
    print()
    print()
    print(oucms, "outcomes in total.")
    print()


def progress():   # indexing the stars according to the grade of module and printing the grade
    while q_or_y != "q":
        if passed == 120  and defer == 0 and fail ==0: 
            print ("Progress") 
            star_list[0] = star_list[0]+1
            break

        elif ( passed == 100 and defer == 20 and fail == 0) or ( passed == 100 and defer == 0 and fail == 20):
            print ("Progress(module trailer)")
            star_list[1] = star_list[1]+1
            break

        elif (passed == 80 and defer == 40 and fail == 0  ) or (passed == 80 and defer == 20 and fail == 20) or (passed == 80 and defer == 0 and fail == 40 ) or (passed == 60 and defer == 60 and fail == 0) or(passed == 60 and defer == 40 and fail == 20) or(passed == 60 and defer == 20 and fail == 40) or(passed == 60 and defer == 0 and fail == 60) or(passed == 40 and defer == 80 and fail == 0) or (passed == 40 and defer == 60 and fail == 20) or(passed == 40 and defer == 40 and fail == 40) or(passed == 40 and defer == 20 and fail == 60) or(passed == 20 and defer == 100 and fail == 0) or(passed == 20 and defer == 80 and fail == 20) or(passed == 20 and defer == 60 and fail == 40) or(passed == 20 and defer == 40 and fail == 60) or(passed == 0 and defer == 120 and fail == 0) or(passed == 0 and defer == 100 and fail == 20) or(passed == 0 and defer == 80 and fail == 40) or(passed == 0 and defer == 60 and fail == 60):
            print("Module retriever")
            star_list[2] = star_list[2]+1
            break

        elif ( passed == 40 and defer == 0 and fail == 80) or ( passed == 20 and defer == 20 and fail == 80) or ( passed == 20 and defer == 0 and fail == 100) or ( passed == 0 and defer == 40 and fail == 80) or ( passed == 0 and defer == 20 and fail == 100) or ( passed == 0 and defer == 0 and fail == 120):
            print("Exclude")  
            star_list[3] = star_list[3]+1
            break 
        
      
print("Welcome to module progress tracker\n\n")

while True:

    try: # Exception handling for non-integer inputs

        passed = int(input("Enter your total PASS credits : "))  
        
        if passed not in range(0,121,20):  # range should be not below 0, not over 120 and should be multiples of 20 (step)
            print("Out of range.")
            print()
            continue
        defer = int(input("Enter your total DEFER credits : "))
        
        if defer not in range(0,121,20):
            print("Out of range.")
            print()
            continue
        fail = int(input("Enter your total FAIL credits : "))
        
        if fail not in range(0,121,20):
            print("Out of range.")
            print()
            continue
        if passed + defer + fail != 120:  # total of passed, defer, refer should not exceed 120
            print("Total incorrect")
            print()
            continue
        
        else:
            
            result_list = [ passed, defer, fail]  # storing inputs to a list

            nulls.append(result_list)  # appending result_list to a null list

            progress() 
            oucms = oucms + 1 
        
            print("\nwould you like to enter another set of data? ")
            q_or_y = input("\nEnter 'y' for yes or 'q' to quit and view results : ").lower() 
            print()
            if q_or_y == 'y':
                continue

            elif q_or_y == 'q':
                histogram()
                scorelist()
                read_file()
                break
            else:
                print("wrong input! check your progress\n")
                histogram()
                scorelist()
                read_file()
                break
            
    except ValueError:   # catches errors for non-integer inputs 
        print("Integer required\n") 

