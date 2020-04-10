#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2020-04-09
Purpose: Update GPS coordiantes on TIF images in a given directory.
"""

import argparse
import os
import sys
from osgeo import gdal
import numpy as np
import pandas as pd
import glob
import csv
from datetime import datetime

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dir',
                        metavar='dir',
                        type=str,
                        help='The directory containing TIF images')

    parser.add_argument('-c',
                        '--csv',
                        help='CSV file with updated coordinates',
                        metavar='FILE',
                        type=str,
                        required=True)
    
    parser.add_argument('-o',
                        '--outdir',
                        metavar='outdir',
                        type=str,
                        default='gpscorrect_out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    startTime = datetime.now()

    args = get_args()
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    images = glob.glob(args.dir + "*.tif", recursive=True)
    print(images)
    
    df = pd.read_csv(args.csv, index_col = 'Filename', usecols = ['Filename', 'Upper left', 'Lower right'])
    
    for i in images:
        filename = ''.join(os.path.splitext(os.path.basename(i)))
        u_l = df.loc[[str(filename)][0], ['Upper left'][0]]
        u_l_long, u_l_lat = u_l.split(',')
        l_r = df.loc[[str(filename)][0], ['Lower right'][0]]
        l_r_long, l_r_lat = l_r.split(',')
        print(f'Upper left: {u_l_lat} {u_l_long} "\n" Lower right: {l_r_lat} {l_r_long}')
        basename = os.path.splitext(os.path.basename(i))[0]
        print(basename)
        outfile = args.outdir + basename + '_corrected.tif'
        cmd = f'gdal_translate -of "GTiff" -co "COMPRESS=LZW" -a_ullr {u_l_long} {u_l_lat} {l_r_long} {l_r_lat} -a_srs EPSG:4326 {i} {outfile}'
        subprocess.call(cmd, shell=True)

    print(f'Done, process took {datetime.now() - startTime}. See {args.outdir}.')
    #num = 0
    #for i in images:
    #    num += 1
    #    ds = gdal.Open(i)
    #    cmd = f'gdal_translate -a_ullr {top_left_lon} {top_left_lat} {bottom_right_lon} {bottom_right_lat} -a_srs EPSG:4269 input.png output.tif'
    #    subprocess.call(cmd, shell=True)





# --------------------------------------------------
if __name__ == '__main__':
    main()
