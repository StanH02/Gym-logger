from datetime import datetime

while True:
    print("\nWelcome to Stan's Gym Logger 💪")
    print("1. Log a new workout")
    print("2. View workout history")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        workout = input('Enter workout: ').title()
        sets = input('Enter sets: ')
        reps = input('Enter reps: ')

        now = datetime.now()
        formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

        logEntry = f"[{formatted_time}] {workout} - {sets} set x {reps} reps\n"

        with open("log.txt", "a") as logFile:
            logFile.write(logEntry)

        print("✅ Workout logged successfully!\n")

    elif choice == "2":
        try:
            with open("log.txt", "r") as logFile:
                logData = logFile.read()
                print("\n📜 Workout History:")
                print("-" * 40)
                print(logData)
        except FileNotFoundError:
            print("No workout history found. Log your first session!")

    elif choice == "3":
        print("👋 Goodbye, Stan! Stay consistent.")
        break

    else:
        print("❌ Invalid choice. Try again.")
