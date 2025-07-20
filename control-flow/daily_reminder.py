# Prompt user for the task description
task = input("Enter your task: ").strip()

# Prompt user for the priority level
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to process based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# Modify the message if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        message += " that requires immediate attention today!"
    elif priority == "low":
        message += ", but it is time-bound, so try to complete it soon."
    else:
        message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the customized reminder
print(message)
