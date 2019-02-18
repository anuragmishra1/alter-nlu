import numpy as np
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import matthews_corrcoef
from controller.saving import models_dir


# check validation score and save intent model
class Metrics(Callback):
    def __init__(self):
        self.mccs = []


    def on_epoch_end(self, epoch, logs={}):
        val_predict = np.argmax(np.asarray(self.model.predict([self.validation_data[0]])), axis=-1)
        val_targ = np.argmax(self.validation_data[1], axis=-1)
        mcc = matthews_corrcoef(val_targ.tolist(), val_predict.tolist())
        self.mccs.append(mcc)
        if len(self.mccs) > 1:
            if mcc >= max(self.mccs[:-1]):
                self.model.save(models_dir + '/model.h5')
        else:
            self.model.save(models_dir + '/model.h5')
        return
