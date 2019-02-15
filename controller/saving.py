import os
import shutil
from utilities.file_handler import save_pkl


models_dir = './bot_model'


def reset_botmodel():
    if not os.path.exists(models_dir):
        os.mkdir(models_dir)
    else:
        print("> Reset Model")
        shutil.rmtree(models_dir)
        os.mkdir(models_dir)
    return


# save bot metadata
def save_metadata(input_file):
    reset_botmodel()
    print("> Saving Metadata")
    save_pkl(input_file, models_dir + '/metadata')
    return
