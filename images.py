from PIL import Image
import numpy as np
import pathlib

value_names =  ['glc', 'man', 'gal', 'ara', 'xyl']
pred_names = ['glc_pred', 'man_pred', 'gal_pred', 'ara_pred', 'xyl_pred']

target_width = 224
target_height = 224
channels = 3

def get_data_files():
    files = []
    for subdir in pathlib.Path('trainingset').glob('*'):
        for file in pathlib.Path(subdir).glob('*.png'):
            files.append(file)
    return files

def extract_values(filename):
    splitted = str(filename.name).split('_')
    values=[]
    for i in range(0, 5):
        values.append(float(splitted[i]))
    return values


def preprocess_image(filename):
    img = Image.open(filename)
    # setting crop values that "seem to work" to remove axis from the picture
    #remove 5% from each side to get rid of the black frame
    width = img.size[0]
    heigth = img.size[1]

    cropped_img = img.crop((int(width/20), int(heigth/20), int(width*0.95), int(heigth*0.95)))
    resized_img = cropped_img.resize(size=(target_height, target_width))
    as_array = np.array(np.asarray(resized_img))
    as_array = as_array[:,:,:channels]
    img.close()
    resized_img.close()
    return as_array
