task=[]
user_name="Abhilash"


print("== **WELCOME TO ABHI TO DO LIST** ==")
user_login_input=input("Enter th User Name::")
if user_name==user_login_input:
    while True:
        print(f"Welcome {user_login_input} please Select the Option Given Below:")
        print("1.ADD  TASK")
        print("2.DELETE TASK")
        print("3.CHECK TASK")
        print("4.EXITE")
        try:
         user_option_input=int(input("Select a Option:"))
         match user_option_input:
            case 1:
                temp_task=input("Enter the Task::").split()
                if temp_task:
                   task.extend(temp_task)
                   print("Task Added Sucessfully")
            case 2:
                if not task:   
                 print("No Tasks Avaliable") 
                else:
                 for i,ts in enumerate(task,start=1):
                    print(f"{i}.{ts}")
                 try:
                    user_del=int(input("Enter the Task Number to Delete::"))
                    if 1 <= user_del <= len(task):
                     deleted_task = task.pop(user_del-1)
                     print(f"{deleted_task} Deleted Successfully")
                    else:
                      print("Invalid Task Number")
                 except ValueError:
                    print("Enter Number Bro !!")
            case 3:
                print("== TASK MENUE ==")
                if not task:
                   print("No Task ")
                else:
                    for i,ts in enumerate(task,start=1):
                       print(f"{i}.{ts}")
            case 4:
                print("Thanku for using * Abhi TO DO MENUE *")  
                break
            case _:
                print("INVALID OPTION TRY AGAIN")
        except ValueError:
            print("please Enter Value Bro")


else:
    print("**INVALID USER NAME TRY AGAIN**")
