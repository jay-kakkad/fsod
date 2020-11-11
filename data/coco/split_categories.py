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


def filter_coco(coco, split):
    new_anns = []
    all_cls_dict = {}
    for img_id, id in enumerate(coco.imgs):
        img = coco.loadImgs(id)[0]
        anns = coco.loadAnns(coco.getAnnIds(imgIds=id, iscrowd = None))
        SKIP_FLAG = False

        if len(anns) == 0:
            continue

        for ann in anns:
            if ann['category_id'] in split:
                if ann['bbox'][2] * ann['bbox'][3] < 32*32:
                    SKIP_FLAG = True
                    break
        
        if SKIP_FLAG:
            continue
        
        for ann in anns:
            if ann['category_id'] in split:
                new_anns.append(ann)
                
                if category_id in all_cls_dict.keys():
                        all_cls_dict[category_id] += 1
                else:
                    all_cls_dict[category_id] = 1
        
        print(new_anns)
        print(sorted(all_cls_dict.items(), key = lambda kv:(kv[1], kv[0])))
        return new_anns
 

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

    non_voc_idxs = set([i for i in range(len(dataset['categories'])) if i not in voc_idxs])

    category_voc = [dataset['categories'][i] for i in voc_idxs]
    category_non_voc = [dataset['categories'][i] for i in non_voc_idxs]

    cids_voc = [c['id'] for c in category_voc]
    cids_non_voc = [c['id'] for c in category_non_voc]

    print('VOC: {} classes'.format(len(category_voc)))
    for c in category_voc:
        print('\t', c['name'])
    print('Non VOC: {} classes'.format(len(category_non_voc)))
    for c in category_non_voc:
        print('\t', c['name'])

    coco = COCO(annFile)

    # VOC based annotations
    annotations_voc = []

    for ann in dataset['annotations']:
        if ann['category_id'] in cids_voc:
            annotations_voc.append(ann)
    

    # for non-voc, there can be non-voc images
    annotations_non_voc = filter_coco(coco, cids_non_voc)




    
        








