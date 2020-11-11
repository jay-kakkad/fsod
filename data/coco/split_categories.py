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

FILES = ['instances_train2017.json']

for annotation_file in FILES:
    annFile = join(DATA_DIR, annotation_file)
    dataset = None
    with open(annFile, 'r') as file:
        dataset = json.load(file)
        print(dataset.keys())

    if dataset is None:
        print("ERROR: Dataset cannot be none")
        sys.exit()
    
    print("\n CATEGORIES")
    for category in dataset['categories']:
        print(category)
    
        








