import logging
import sys
import os
from os.path import join, isdir
from os import mkdir, makedirs
import time
import json

from pycocotools.coco import COCO
# import cv2
import numpy as np
from concurrent import futures
import math
import matplotlib.pyplot as plt
import pandas as pd


logging.basicConfig(format='%(asctime)s - %(levelname)s :: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Initializing INPUT

# For accepting Sys ARG for directory use below line
# DATA_DIR = sys.argv[1]
DATA_DIR = "/data/jkakkad/fsod-data/coco/annotations"
logging.info(DATA_DIR + "\n")

support_dict = {
    "support_box": [],
    "category_id": [],
    "image_id": [],
    "id": [],
    "file_path": []
}

voc_idxs = {0, 1, 2, 3, 4, 5, 6, 8, 14, 15, 16, 17, 18, 19, 39, 56, 57, 58, 60, 62}

FILES = ['instances_train2017.json']

for annotation_file in FILES:
    annFile = join(DATA_DIR, annotation_file)
    dataset = None
    with open(annFile, 'r') as file:
        dataset = json.load(file)
        print(dataset.keys())

    if dataset is None:
        logging.error("Dataset cannot be none")
        sys.exit()
    
    # print("\n CATEGORIES")
    # for category in dataset['categories']:
    #     print(category)

    idxs_split2 = [i for i in range(len(dataset['categories'])) if i not in voc_idxs]
    category_split_1 = [dataset['categories'][i] for i in voc_idxs]
    category_split_2 = [dataset['categories'][i] for i in idxs_split2]

    cids_split1 = [c['id'] for c in category_split_1]
    cids_split2 = [c['id'] for c in category_split_2]
    print('Split 1: {} classes'.format(len(category_split_1)))
    for c in category_split_1:
        print('\t', c['name'])
    print('Split 2: {} classes'.format(len(category_split_2)))
    for c in category_split_2:
        print('\t', c['name'])


    
        








