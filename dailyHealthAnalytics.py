import numpy as np

np.set_printoptions(precision=2, suppress=True)

array_labels = np.array(["Day", "Steps", "WorkoutMinutes", "AvgHeartRate", "SleepHours", "Bodyweight(kg)"])

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

label_map = {label: i for i, label in enumerate(array_labels)}
day_col = label_map['Day']
steps = label_map['Steps']
workout_minutes = label_map['WorkoutMinutes']
sleep_hours = label_map['SleepHours']

def basic_statistics_head():
    print("")
    print("Basic statistics & Performance Metrics")
    print("--------------------------------------")
    print("")

def days_range(data):
    range_days_input = input("Enter the days range (format of the input (8-14, 8 - 14, 8 to 14)): ")

    range_days_replace = range_days_input.replace(" ", "").lower()

    if "to" in range_days_replace:
        range_days_split = range_days_replace.split('to')
    elif "-" in range_days_replace:
        range_days_split = range_days_replace.split('-')
    else:
        raise ValueError("Format is not correct. Use 'A-B' or 'A to B'.")

    try:
        range_begin = int(range_days_split[0])
        range_end = int(range_days_split[1])
    except ValueError:
        raise ValueError("Numbers should be integers.")

    if range_begin < 1 or range_end < 1:
        raise ValueError("Numbers should be greater than zero.")

    if range_begin > range_end:
        raise ValueError("Range begin is greater than range end.")

    if range_end not in data[:, day_col]:
        raise ValueError(f"Day {range_end} is not valid.")

    masking_data = (data[:, day_col] >= range_begin) & (data[:, day_col] <= range_end)

    return data[masking_data]

while True:
    print("Application")
    print("===========")
    print("1. Enter the day number to get the details")
    print("2. Check the average steps, workout minutes, sleep hours")
    print("3. Check the min and max of steps, workout minutes, sleep hours")
    print("4. Analysis of the daily health")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        try:
            day = int(input("Enter the day number: "))

            if day not in array_data[:, day_col]:
                raise ValueError(f"Day {day} is not valid.")

            mask = array_data[:, day_col] == day
            day_value = array_data[mask, label_map['Day']]
            step_value = array_data[mask, label_map['Steps']]

            print(f"On {array_labels[label_map['Day']].lower()} {int(day_value[0])}, you walked {int(step_value[0])}"
                  f" {array_labels[label_map['Steps']].lower()}")
        except ValueError as e:
            print(str(e))
    elif choice == 2:
        try:
            rows = days_range(array_data)
            if rows.size == 0:
                raise ValueError("Rows not found.")

            basic_statistics_head()
            print("Average (Steps, Workout minutes, Sleep hours):")
            print("")

            means = rows.mean(axis=0)
            print(f"{array_labels[steps]}: {means[steps]:.2f}")
            print(f"{array_labels[workout_minutes]}: {means[workout_minutes]:.2f}")
            print(f"{array_labels[sleep_hours]}: {means[sleep_hours]:.2f}")
            print("")
        except ValueError as e:
            print(str(e))
    elif choice == 3:
        try:
            rows = days_range(array_data)
            if rows.size == 0:
                raise ValueError("Rows not found.")

            basic_statistics_head()
            print("Min and max (Steps, Workout minutes, Sleep hours):")
            print("")

            min_rows = rows.min(axis=0)
            max_rows = rows.max(axis=0)
            print(f"{array_labels[steps]} - Min: {min_rows[steps]:.2f}, Max: {max_rows[steps]:.2f}")
            print(f"{array_labels[workout_minutes]} - Min: {min_rows[workout_minutes]:.2f}, Max: {max_rows[workout_minutes]:.2f}")
            print(f"{array_labels[sleep_hours]} - Min: {min_rows[sleep_hours]:.2f}, Max: {max_rows[sleep_hours]:.2f}")
        except ValueError as e:
            print(str(e))
    elif choice == 4:
        basic_statistics_head()
        print("Analysis of the daily health:")
        user_input_label = int(input("Choose label (1. Sleep hours, 2. Workout minutes): "))

        if user_input_label == 1:
            user_input_to_check_average = float(input("Enter the sleep hours: "))
        elif user_input_label == 2:
            user_input_to_check_average = float(input("Enter the workout minutes: "))
        else:
            raise ValueError("Label not found.")

        user_input_operator = int(input("Choose operator (1. <, 2. >, 3. <=, 4. >=): "))

        #if user_input_to_check_average < array_data[:, user_input_to_check_average]:
        print(user_input_to_check_average)
        print(array_data[:, user_input_to_check_average])


        #TODO: Select all days where: Sleep < 6 hours, Workout minutes ≥ 45 from those days, get the average heart rate and steps.
        #TODO: Check the boolean masks and applying them to 2-D arrays.
    elif choice == 5:
        break
