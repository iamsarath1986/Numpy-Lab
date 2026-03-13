import numpy as np
import operator

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
avg_heart_rate = label_map['AvgHeartRate']

def operator_map(operator_str):
    if operator_str == "<":
        return operator.lt
    elif operator_str == ">":
        return operator.gt
    elif operator_str == "<=":
        return operator.le
    elif operator_str == ">=":
        return operator.ge
    else:
        raise ValueError("Operator not found.")

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
    print("5. Correlation analysis")
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
        try:
            basic_statistics_head()
            print("Analysis of the daily health:")
            user_input_label = int(input("Choose label (1. Sleep hours, 2. Workout minutes): "))

            if user_input_label not in [1, 2]:
                raise ValueError("Label not found.")

            if user_input_label == 1:
                user_input_of_sleeping_hours = float(input("Enter the sleep hours: "))
                user_input_operator = input("Choose operator (<, >, <=, >=): ")
                op_func = operator_map(user_input_operator)
                mask = op_func(array_data[:, sleep_hours], user_input_of_sleeping_hours)

                if not np.any(mask):
                    print("No data found.")
                else:
                    hours_slept = array_data[mask, sleep_hours]
                    days_slept = array_data[mask, day_col].astype(int)

                    for sleep, day in zip(hours_slept, days_slept):
                        print(f"You slept {sleep} hours on day {day}.")

            if user_input_label == 2:
                user_input_of_workout_minutes = float(input("Enter the workout minutes: "))
                user_input_operator = input("Choose operator (<, >, <=, >=): ")
                op_func = operator_map(user_input_operator)
                mask = op_func(array_data[:, workout_minutes], user_input_of_workout_minutes)

                if not np.any(mask):
                    print("No data found.")
                else:
                    days_workout = array_data[mask, day_col].astype(int)
                    heart_rate = array_data[mask, avg_heart_rate]
                    steps = array_data[mask, steps]

                    for day, hr, st in zip(days_workout, heart_rate, steps):
                        print(f"On day {day}, you exercised for {hr} heart rate and {st} steps.")

                    print(f"Average heart rate: {heart_rate.mean():.2f}")
        except ValueError as e:
            print(str(e))
    elif choice == 5:
        try:
            print("Correlation analysis:")
            user_input_label = int(input("Choose label (1. Sleep hours and average workout heart rate, 2. Sleep hours and workout minutes, 3. Workout minutes and steps): "))
            if user_input_label not in [1, 2, 3]:
                raise ValueError("Label not found.")

            if user_input_label == 1:
                print("This explores if your sleep quality affects your cardiovascular strain during exercise.")
                sleep = array_data[:, sleep_hours]
                heart_rate = array_data[:, avg_heart_rate]
                correlation = np.corrcoef(sleep, heart_rate)[0, 1]
            elif user_input_label == 2:
                print("This checks if your energy levels (from sleep) influence how long you can work out.")
            elif user_input_label == 3:
                print("This is usually a very strong positive correlation, as walking is often part of the workout.")

        except ValueError as e:
            print(str(e))

        # TODO: 3. Correlation exploration
        #
        # Compute correlations between:
        #
        # Sleep hours and average workout heart rate
        #
        # Sleep hours and workout minutes
        #
        # Workout minutes and steps
        #
        # Interpret: on days with more sleep, do you tend to work out longer or at higher intensity?.

    elif choice == 5:
        break
