import numpy as np
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import f1_score
from controller.saving import models_dir


# check validation score and save intent model
class Metrics(Callback):
    def __init__(self):
        self.val_f1s = []


    def on_epoch_end(self, epoch, logs={}):
        val_predict = np.argmax(np.asarray(self.model.predict([self.validation_data[0]])), axis=-1)
        val_targ = np.argmax(self.validation_data[1], axis=-1)
        val_f1 = f1_score(val_targ.tolist(), val_predict.tolist(), average='micro')
        self.val_f1s.append(val_f1)
        if len(self.val_f1s) > 1:
            if val_f1 >= max(self.val_f1s[:-1]):
                self.model.save(models_dir + '/model.h5')
        return
