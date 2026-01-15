import numpy as np

array_labels = np.array(["Day", "Steps", "Workout_Minutes", "Avg_Heart_Rate", "Sleep_Hours", "Bodyweight_kg"])

array_data = np.array([
 [ 1,  7500, 35, 118, 6.0, 81.5 ],
 [ 2,  8200, 40, 121, 6.5, 81.4 ],
 [ 3,  6900, 25, 112, 5.5, 81.6 ],
 [ 4, 10500, 50, 126, 7.2, 81.2 ],
 [ 5, 11200, 55, 129, 7.0, 81.0 ],
 [ 6,  5800, 20, 110, 5.0, 81.7 ],
 [ 7,  9600, 45, 125, 6.8, 81.1 ],
 [ 8, 10900, 60, 132, 7.5, 80.9 ],
 [ 9,  7300, 30, 116, 6.0, 81.0 ],
 [10,  8800, 40, 120, 6.3, 80.8 ],
 [11, 12100, 65, 134, 7.8, 80.6 ],
 [12,  6400, 25, 113, 5.8, 80.9 ],
 [13,  9900, 50, 127, 7.1, 80.5 ],
 [14, 10200, 55, 130, 7.3, 80.4 ]
])

day = 14

if not (1 <= day <= array_data.shape[0]):
    print(f"Day {day} is not valid.")
    exit(1)

row_index = day - 1

label_map = {label: i for i, label in enumerate(array_labels)}
day_value = array_data[row_index, label_map['Day']]
step_value = array_data[row_index, label_map['Steps']] # Step value based on day and label

print(f"On {array_labels[label_map['Day']].lower()} {int(day_value)}, you walked {int(step_value)}"
      f" {array_labels[label_map['Steps']].lower()}")

#TODO:: Read the Junie generated about the new changes.

'''
print("")
print("1. Basic statistics & slicing")
print("")
print("Calculate the mean of Steps column:")

#print(array_data[:, step_label_index].mean(dtype=np.float64))
'''