import os
from controller.saving import models_dir
from utilities.file_handler import load_pkl
from tensorflow.keras.models import load_model
from sklearn_crfsuite import CRF


# load bot from filesystem
def loader():
    if not os.path.exists(models_dir):
        print('> NO EXISTING BOT FOUND.')
    else:
        print('> LOADING BOT')
        if os.path.exists(models_dir + '/model.h5') and os.path.exists(models_dir + '/metadata'):
            model = load_model(models_dir + '/model.h5')
            metadata = load_pkl(models_dir + '/metadata')
            if os.path.exists(models_dir + '/crfmodel'):
                crfmodel = CRF(model_filename=models_dir + '/crfmodel')
            else:
                crfmodel = None
            print('> LOADING DONE')
            return metadata, model, crfmodel
        else:
            print('!! Incomplete Training. Skipping...')
    
    return None, None, None
