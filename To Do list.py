# 1 - add tasks to a list

#2 - mark task as complete

#3 - view tasks

#4 - break/ Exit
def main():
  while True:
    print(message)
    choice = input("Enter Your Choice: ")

    match choice:
        case '1':
            #add task to tasks list
            add_task()

        case '2':
            mark_task_complete()
        case '3':
            view_tasks()
        case '4':
            break
        case _:
            print("Please Enter a Number Between 1 and 4")
tasks = []
message = """ 
1 - Add tasks to The list
2 - Mark task as complete
3 - View tasks
4 - Exit
"""

def add_task():
    task = input("Enter Your Task: ").title()

    task_info = {"task": task, "completed": False}
    tasks.append(task_info)
    print("Task Added To List Successfully")


def mark_task_complete():
  incomplete_tasks = [task for task in tasks if task["completed"] is False]
  if not incomplete_tasks:
    print("No Tasks To Mark As Complete")
    return
  for i, task in enumerate(incomplete_tasks, 1):
    print(f"{i}. {task['task']}")

  task_number = int(input("Enter Number Of Task To Mark Completed: "))
  incomplete_tasks[task_number - 1]["completed"] = True
  print("Task Marked Complete")
def view_tasks():
  if not tasks:
    print("No Tasks Yet, Add One")
    return
  print("Here Are Your Tasks: ")
  for i, task in enumerate(tasks, start=1):
    status = '✅' if task["completed"] else '✖️'
    print(f"{i}. {task['task'].title()} {status}")
main()