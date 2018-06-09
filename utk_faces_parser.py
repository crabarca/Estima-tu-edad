## Parser for utk_faces database

import math
import os
from shutil import os

FolderPath = "./utk_faces_renamed"

ageRangeCounter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
baseFilename = "face_{}_{}.jpg"    
renamed = True

for filename in os.listdir(FolderPath):
    if renamed:
        # To count images per group when remained
        group = int(filename.split("_")[1])
        ageRangeCounter[group] += 1
        continue

    age = int(filename.split("_")[0])
    group = 0
    if age < 1:
        group = 1
    
    elif age >= 1 and age < 10:
        group = 2

    elif age >= 10 and age < 16:
        group = 3
    
    elif age >= 16 and age < 28:
        group = 4
    
    elif age >= 28 and age < 51:
        group = 5
    
    elif age >= 51 and age < 75:
        group = 6
    
    else:
        group = 7

    if group != 0:
        ageRangeCounter[group] += 1

    newName = baseFilename.format(str(group).zfill(3), str(ageRangeCounter[group]).zfill(5))
    os.rename(FolderPath + '/' + filename, FolderPath + '/' + newName)

# print(ageRangeCounter)

agePercentile = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

for i in range(2,8):
    training = math.floor(ageRangeCounter[i] * 0.9) # 90 training
    test = math.floor(ageRangeCounter[i] - ageRangeCounter[i] * 0.1) # 10 training
    agePercentile[i] = [training, test]

print(agePercentile)