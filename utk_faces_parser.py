## Parser for utk_faces database

import math
import os
from shutil import os

def rename_utk(folderPath = './utk_faces_renamed'):
    ageRangeCounter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    baseFilename = "face_{}_{}.jpg"    

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    for filename in os.listdir(folderPath):
        age = int(filename.split("_")[0])
        group = 0
        if age <= 1:
            group = 1

        elif age > 1 and age < 10:
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
        os.rename(folderPath + '/' + filename, folderPath + '/' + newName)

    if renamed:
        print(ageRangeCounter)


def class_counter(folderPath, verbose = True):
    ageRangeCounter = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for filename in os.listdir(folderPath):
        # Count images per group. Img are already renamed
        group = int(filename.split("_")[1])
        ageRangeCounter[group] += 1
    
    if verbose:
        print("Age range counter:", ageRangeCounter)
    return ageRangeCounter


def class_percentile(ageRangeCounter, testing = 0.9, train = 0.1, verbose = False):  
    agePercentile = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}

    for i in range(1, 8):
        trainingQty = math.floor(ageRangeCounter[i] * testing)
        testQty = ageRangeCounter[i] - trainingQty
        agePercentile[i] = [trainingQty , testQty]

    if verbose:
        print("Hold out {}/{}  class count: {}".format(train * 100, testing * 100, agePercentile)) 
    return agePercentile


if __name__ == "__main__":
    renamed = True
    folderPath = "./utk_faces_renamed"
    if not renamed:
        rename_utk(folderPath)
    ageCounter = class_counter(folderPath)
    class_percentile(ageCounter, verbose=True)
