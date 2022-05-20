import pandas as pd
import random
import os

data = pd.read_table('M_uyg_dmp.txt', sep='\t', index_col=0)

headers = data.columns.values.tolist()
# header_index = list(range(len(headers)))

SAMPLE_EPOCH = 90
SAMPLE_NUMBER = 33

for i in range(SAMPLE_EPOCH):
    sample_index = random.sample(headers, SAMPLE_NUMBER)
    sample_index.sort()

    # print(sample_index)

    sample_data = data[sample_index]
    sample_data.to_csv('{}/{}'.format(i + 1, 'M_uyg_dmp.txt'), sep='\t', index_label="ID")

    print('sample {0} is done, {0}/{1}'.format(i + 1, SAMPLE_EPOCH))
    # print("hh")


print('You are great!')