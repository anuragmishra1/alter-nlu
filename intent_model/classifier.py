from tensorflow.keras.layers import Dense, Dropout, Embedding, Input, GlobalMaxPool1D, BatchNormalization, concatenate, Conv1D
from tensorflow.keras.models import Model


# classification model
def model_def(x, y, z):
    input_1 = Input(shape=(x,))
    embedding_1 = Embedding(y, 128, input_length=x)(input_1)

    conv_1 = Conv1D(32, 1, use_bias=True, padding='valid', activation='relu')(embedding_1)
    normalized_1 = BatchNormalization()(conv_1)
    drop_out_1 = Dropout(0.5)(normalized_1)
    pooling_1 = GlobalMaxPool1D()(drop_out_1)

    conv_2 = Conv1D(32, 2, use_bias=True, padding='valid', activation='relu')(embedding_1)
    normalized_2 = BatchNormalization()(conv_2)
    drop_out_2 = Dropout(0.5)(normalized_2)
    pooling_2 = GlobalMaxPool1D()(drop_out_2)

    conv_3 = Conv1D(32, 3, use_bias=True, padding='valid', activation='relu')(embedding_1)
    normalized_3 = BatchNormalization()(conv_3)
    drop_out_3 = Dropout(0.5)(normalized_3)
    pooling_3 = GlobalMaxPool1D()(drop_out_3)

    merged_1 = concatenate([pooling_1, pooling_2, pooling_3])

    dense_1 = Dense(2*len(z), activation='relu', use_bias=True)(merged_1)
    dense_2 = Dense(2*len(z), activation='relu', use_bias=True)(dense_1)
    dense_3 = Dense(2*len(z), activation='relu', use_bias=True)(dense_2)

    dense_4 = Dense(len(z), activation='softmax', use_bias=True)(dense_3)
    final_model = Model(inputs=[input_1], outputs=[dense_4])
    final_model.compile(optimizer='adam', loss='categorical_crossentropy')

    return final_model
