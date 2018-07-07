import face_recognition
from scipy.misc import imsave
from os import listdir
from os.path import isfile, join

input_folder = 'AgeDb'
output_folder = 'output'

def crop_image(image, pos):
    return image[pos[0]:pos[2], pos[3]:pos[1]]

def proccess_image(filename):
     image = face_recognition.load_image_file(join(input_folder, filename), mode='L')
     pos = face_recognition.face_locations(image)[0]
     imsave(join(output_folder, filename), crop_image(image, pos))

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

n_files = len(listdir(input_folder))
count = 0
failed_images = 0

for filename in listdir(input_folder):
    print(str(count) + " / " + str(n_files))
    count += 1
    try:
        proccess_image(filename)
    except Exception:
        failed_images += 1

print('Fallaron', failed_images)

