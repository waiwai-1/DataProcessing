import pandas as pd
import random
import os

M_uyg_dmp = pd.read_table('M_uyg_dmp.txt', sep='\t')
SNP_test = pd.read_table('SNP_test.txt', sep='\t')

headers = M_uyg_dmp.columns.values.tolist()
header_index = list(range(len(headers)))

SAMPLE_EPOCH = 90
SAMPLE_NUMBER = 33

for i in range(SAMPLE_EPOCH):
    sample_index = random.sample(headers, SAMPLE_NUMBER)
    sample_index.sort()

    # print(sample_index)

    sample_M_uyg_dmp = M_uyg_dmp[sample_index]
    sample_M_uyg_dmp.to_csv('{}/{}'.format(i + 1, 'M_uyg_dmp.txt'), sep='\t')

    sample_SNP_test = SNP_test[sample_index]
    sample_SNP_test.to_csv('{}/{}'.format(i + 1, 'SNP_test.txt'), sep='\t')


    print('sample {0} is done, {0}/{1}'.format(i + 1, SAMPLE_EPOCH))



print('You are great!')