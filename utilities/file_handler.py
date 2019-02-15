import pickle


# pickle format file save
def save_pkl(input_file, output_file):
    with open(output_file, 'wb') as handle:
        pickle.dump(input_file, handle, protocol=pickle.HIGHEST_PROTOCOL)


# pickle format file load
def load_pkl(file_name):
    with open(file_name, 'rb') as handle:
        var = pickle.load(handle)
        return var