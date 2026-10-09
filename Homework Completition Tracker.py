
original_homework = 4
homework = 4

print(f"You have {homework} homework tasks to do today!\n")

completed_homework = 0
task_num = 1

while task_num <= original_homework:
    if task_num == 1:
        next_task = "Math worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"

    answer = input(f"Have you finished {next_task}? (yes/no): ")
    answer = answer.lower().strip()

    if answer == "yes":
        print("Well done! Homework task completed!")
        completed_homework += 1
        task_num += 1
        homework -= 1
    else:
        print("Okay, complete the task and check it again!")

    print("Homework tasks remaining:", homework)
    print()

print("===== All homework completed =====")

print("\nNow let's safely peek at an infinite loop...")

test_value = 0
safety_counter = 0

while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    safety_counter += 1

    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", original_homework)
print("Homework Completed:", completed_homework)
print("=======================================")