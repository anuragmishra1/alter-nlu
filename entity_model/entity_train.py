from sklearn_crfsuite import CRF
from entity_model.entity_featurizer import get_trainable_features
from controller.saving import models_dir


def train_entity(intent_data, entity_data, used_punct, unused_punct):
    crf = CRF(algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100,
            all_possible_transitions=True,
            model_filename = models_dir+'/crfmodel',
            verbose=True)

    X, y = get_trainable_features(intent_data, entity_data, used_punct, unused_punct)
    crf.fit(X,y)
