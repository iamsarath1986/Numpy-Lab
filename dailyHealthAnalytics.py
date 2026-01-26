import numpy as np

np.set_printoptions(precision=2, suppress=True)

array_labels = np.array(["Day", "Steps", "Workout_Minutes", "Avg_Heart_Rate", "Sleep_Hours", "Bodyweight_kg"])

array_data = np.array([
    [4, 10500, 50, 126, 7.2, 81.2],
    [5, 11200, 55, 129, 7.0, 81.0],
    [6, 5800, 20, 110, 5.0, 81.7],
    [1, 7500, 35, 118, 6.0, 81.5],
    [2, 8200, 40, 121, 6.5, 81.4],
    [3, 6900, 25, 112, 5.5, 81.6],
    [7, 9600, 45, 125, 6.8, 81.1],
    [10, 8800, 40, 120, 6.3, 80.8],
    [11, 12100, 65, 134, 7.8, 80.6],
    [12, 6400, 25, 113, 5.8, 80.9],
    [13, 9900, 50, 127, 7.1, 80.5],
    [14, 10200, 55, 130, 7.3, 80.4],
    [8, 10900, 60, 132, 7.5, 80.9],
    [9, 7300, 30, 116, 6.0, 81.0]
])

print("1. Enter the day number to get the details")
print("2. Check the average Steps, Workout minutes, Sleep hours")
try:
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2]:
        print("Number should be 1 or 2.")
        exit(1)

    label_map = {label: i for i, label in enumerate(array_labels)}
    day_col = label_map['Day']
    steps = label_map['Steps']
    workout_minutes = label_map['Workout_Minutes']
    sleep_hours = label_map['Sleep_Hours']

    if choice == 1:
        try:
            day = int(input("Enter the day number: "))

            if not (1 <= day <= array_data.shape[0]):
                print(f"Day {day} is not valid.")
                exit(1)

            mask = array_data[:, day_col] == day
            day_value = array_data[mask, label_map['Day']]
            step_value = array_data[mask, label_map['Steps']]

            print(f"On {array_labels[label_map['Day']].lower()} {int(day_value[0])}, you walked {int(step_value[0])}"
                  f" {array_labels[label_map['Steps']].lower()}")
        except ValueError:
            print("Invalid input.")

    elif choice == 2:
        try:
            range_days_input = input("Enter the days range (format of the input (8-14, 8 – 14, 8 to 14)): ")

            range_days_replace = range_days_input.replace(" ", "")

            if "to" in range_days_replace:
                range_days_split = range_days_replace.split('to')
            elif "-" in range_days_replace:
                range_days_split = range_days_replace.split('-')
            else:
                print("Invalid range.")
                exit(1) #TODO: Reprompt user for valid input.

            range_begin = int(range_days_split[0])
            range_end = int(range_days_split[1])

            if range_begin < 1 or range_end < 1:
                print("Numbers should be greater than zero.")
                exit(1) #TODO: Reprompt user for valid input.

            if range_begin > range_end:
                print("Invalid range.")
                exit(1)

            mask = (array_data[:, day_col] >= range_begin) & (array_data[:, day_col] <= range_end)
            rows = array_data[mask]

            print("")
            print("1. Basic statistics & slicing")
            print("")
            print("Average (Steps, Workout minutes, Sleep hours):")
            print("")

            means = rows.mean(axis=0)
            print(f"{array_labels[steps]}: {means[steps]:.2f}")
            print(f"{array_labels[workout_minutes]}: {means[workout_minutes]:.2f}")
            print(f"{array_labels[sleep_hours]}: {means[sleep_hours]:.2f}")
        except ValueError:
            print("Invalid input.")
    else:
        exit(1)

except ValueError:
    print("Invalid choice.")