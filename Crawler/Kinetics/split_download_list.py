import argparse
import os
import math

import pandas as pd

def main(input_csv, output_dir,
         num_splits):

    # Reading and parsing Kinetics.
    name = input_csv.split('/')[-1]
    vlist = pd.read_csv(input_csv)
    nums = vlist.shape[0]
    stride = int(math.ceil(float(nums)/num_splits))
    for i in range(num_splits):
        vlistSplit = vlist[i*stride : min((i+1)*stride, nums)]
        vlistSplit.to_csv(os.path.join(output_dir, ''.join([name.split('.')[0], '_split%d'%(i+1), '.csv'])), index=False)
        print(vlistSplit.shape[0])


if __name__ == '__main__':

    description = 'Helper script for spliting kinetics download links for parallization.'
    p = argparse.ArgumentParser(description=description)
    p.add_argument('--input-csv', type=str,
                   help=('CSV file containing the following format: '
                         'YouTube Identifier,Start time,End time,Class label'), default='./data/kinetics_tmp.csv')
    p.add_argument('--output-dir', type=str,
                   help='Output directory where splits will be saved.', default='./data')
    p.add_argument('-n', '--num-splits', type=int, default=2)
    args = p.parse_args()
    main(**vars(args))
