tasks =[]
while True:
    task  =input("Enter a task:")
    tasks.append(task)
    choice = input ("Do you want to add another task?(yes/no):")
    if choice.lower()!="yes":
        break
    print("\nYour To-Do List:")
    for task in tasks:
        print("-", task)
        
