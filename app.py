from task_manager import log_task_update
from summary_generator import generate_summary
from blockers_analyzer import detect_blockers

def menu():
    print("🤖 AI Project Manager Bot")
    print("1. Log Task Update")
    print("2. Generate Summary")
    print("3. Detect Blockers")
    print("4. Exit")

while True:
    menu()
    choice = input("Select option: ")
    
    if choice == "1":
        update = input("Enter your task update: ")
        log_task_update(update)
    elif choice == "2":
        print("📋 Project Summary:\n")
        print(generate_summary())
    elif choice == "3":
        print("🚧 Blockers or Risks:\n")
        print(detect_blockers())
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice")