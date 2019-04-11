import numpy as np
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import matthews_corrcoef
from controller.saving import models_dir


# check validation score and save intent model
class Metrics(Callback):
    def __init__(self):
        self.mccs = []
        self.fit_score = {}


    def on_epoch_end(self, epoch, logs={}):
        val_predict = np.argmax(np.asarray(self.model.predict([self.validation_data[0]])), axis=-1)
        val_targ = np.argmax(self.validation_data[1], axis=-1)
        mcc = matthews_corrcoef(val_targ.tolist(), val_predict.tolist())
        self.mccs.append(mcc)
        if len(self.mccs) > 1:
            if mcc >= max(self.mccs[:-1]):
                diff = 1 / (abs((logs.get('val_loss')/logs.get('loss'))-1)*logs.get('val_loss')*logs.get('loss'))
                temp = [] if mcc not in self.fit_score else self.fit_score[mcc]
                temp.append(diff)
                self.fit_score[mcc] = temp
                if len(self.fit_score[mcc]) > 1:
                    if diff >= max(self.fit_score[mcc][:-1]):
                        self.model.save(models_dir + '/model.h5')
                else:
                    self.model.save(models_dir + '/model.h5')
        else:
            self.model.save(models_dir + '/model.h5')
        return
