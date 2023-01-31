# PART 4 SOURCE CODE

#intialization of variables

result_dict = {} # null dictionary

def dict_func():  # filtering out the user inputs and printing out the matching print statement 
    print("Part 4 :")
    for x in result_dict:
        if result_dict.get (x) == ([120],[0],[0]) :
                print(x, " : progress -", (result_dict.get(x)))
        if  result_dict.get (x) == ([100],[20],[0]) or result_dict.get (x) == ([100],[0],[20]) :
                print(x, " : progress(module trailer) -", (result_dict.get(x)))
        if  result_dict.get (x) == ([80],[40],[0]) or result_dict.get (x) == ([80],[20],[20]) or result_dict.get (x) == ([80],[0],[40]) or result_dict.get (x) == ([60],[60],[0]) or result_dict.get (x) == ([60],[40],[20]) or result_dict.get (x) == ([60],[20],[40]) or result_dict.get (x) == ([60],[0],[60]) or result_dict.get (x) == ([40],[80],[0]) or result_dict.get (x) == ([40],[60],[20]) or result_dict.get (x) == ([40],[40],[40]) or result_dict.get (x) == ([40],[20],[60]) or result_dict.get (x) == ([20],[100],[0]) or result_dict.get (x) == ([20],[80],[20]) or result_dict.get (x) == ([20],[60],[40]) or result_dict.get (x) == ([20],[40],[60]) or result_dict.get (x) == ([0],[120],[0]) or result_dict.get (x) == ([0],[100],[20]) or result_dict.get (x) == ([0],[80],[40]) or result_dict.get (x) == ([0],[60],[60]) :
                print(x, " : Do Not progress(module retriever) -", (result_dict.get(x)))     
        if  result_dict.get (x) == ([40],[0],[80]) or result_dict.get (x) == ([20],[20],[80]) or result_dict.get (x) == ([20],[0],[100]) or result_dict.get (x) == ([0],[40],[80]) or result_dict.get (x) == ([0],[20],[100]) or result_dict.get (x) == ([0],[0],[120]) :                    
            print(x, " : Exclude -", (result_dict.get(x)))
            print() 

print("Welcome to module progress tracker\n\n")

while True:

    try:  # Exception handling for non-integer inputs
        
        stu_id = input("enter your student ID : ")
        print()
        passed = int(input("Please enter your credits at pass : "))
        
        if passed not in range(0,121,20):   # range should be not below 0, not over 120 and should be multiples of 20 (step)
            print()
            print("Out of range.")
            print()
            continue
        defer = int(input("Please enter your credits at defer : "))
        
        if defer not in range(0,121,20):
            print()
            print("Out of range.")
            print()
            continue
        fail = int(input("Please enter your credits at fail : "))
        
        if fail not in range(0,121,20):
            print()
            print("Out of range.")
            print()
            continue
        if passed + defer + fail != 120:   # total of passed, defer, refer should not exceed 120
            print()
            print("Total incorrect")
            print()
            continue
        
        else:  

            result_dict[stu_id] = [passed],[defer],[fail]   # assigning key and values 
            print()
            print("\nwould you like to enter another set of data? ")
            q_or_y = input("\nEnter 'y' for yes or 'q' to quit and view results : ").lower() 
            print()

            if q_or_y == 'y':
                continue

            elif q_or_y == 'q':
                dict_func()                      
                break

            else:
                print()
                print("wrong input! check your progress\n")   
                dict_func()     
                break
            
    except ValueError:   # catches errors for non-integer inputs
        print()     
        print("Integer required\n") 

