import pandas as pd

def get_replacable(p):
    p = sorted(p, key=lambda x:x[0])
    p = pd.DataFrame(p)
    p = p.rename(columns={0:"start", 1:"end", 2:"name"})
    p["new_end"] = p["start"].shift(periods = -1, fill_value = -1)
    p.loc[-1] = (0, 0, "other", p['start'][0])
    p.index = p.index + 1
    p = p.sort_index()
    p = list(zip(p['end'].tolist(), p['new_end'].tolist(), ["other"]*p.shape[0])) + list(zip(p['start'].tolist(), p['end'].tolist(), p['name'].tolist()))
    p = sorted(p, key=lambda x:x[0])
    return p

def multiple_slice(val):
    output = []
    if val['entities'] != []:
        start_end = [(item['start'], item['end'], item['entity']) for item in val['entities']]
        start_end = get_replacable(start_end)
        for item in start_end:
            if item[1] == -1:
                sliced = " ".join(val['text'][item[0]:].split())
            else:
                sliced = " ".join(val['text'][item[0]:item[1]].split())               
            if len(sliced) > 0:
                output.append(([sliced], [item[2]]))
    return output

def get_sliced_data(val):
    sliced_frame = pd.DataFrame(val.apply(multiple_slice, axis=1), columns=["combined"])
    sliced_frame = sliced_frame[sliced_frame.astype('str')['combined'] != '[]']
    sliced_frame.reset_index(drop=True, inplace=True)
    return sliced_frame
