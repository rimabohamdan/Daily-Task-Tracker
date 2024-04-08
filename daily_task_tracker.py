done = []
ongoing = []
tasks_input = input("Enter your tasks for today separated by comma :").split(", ")
for tasks in tasks_input :
    print("\n" + tasks + "\n")
    replay = input(f"Did you finish {tasks} alredy? (yes/no):")
    if replay.lower() == "yes" :
        done.append(tasks)
        print("Nice job")
    else :
        ongoing.append(tasks)
        print("Try not to put it off")
    print("________")
progress = input("Do you want to see your today's progress ? (yes/no)")
if progress.lower() == "yes" :
   print(f"""
              **** Done Tasks ****
              {done}
     """)
   print(f"""
              **** Ongoing Tasks ****
              {ongoing}
     """)

input("Press Enter to exit")
