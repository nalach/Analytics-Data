#!python
import os
import numpy as np

angles = []
data = []
i = 0
while i <= 100000:
    data.append(0)
    a = i/1000
    angles.append(a)
    i += 5

huber_folder_path = os.path.join("Sample_data","Huber")
file_names = [filename for filename in os.listdir(huber_folder_path) if os.path.isfile(os.path.join(huber_folder_path, filename))]

for filename in file_names:
    with open(os.path.join(huber_folder_path, filename), "r") as f:
        j = 0
        for line in f:
            if line[0] == " ":
                data[j] = data[j] + int(line.split(" ")[1])
                j += 1

k = 0
file = open("Added.xy", "w")
for d in data:
    file.write(str(angles[k]) + " " + str(d) + "\n")
    k += 1
file.close()


