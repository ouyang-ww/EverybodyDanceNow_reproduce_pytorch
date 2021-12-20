import os
import numpy as np
import torch
import time
import sys
from collections import OrderedDict
from torch.autograd import Variable
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')
mainpath = os.getcwd()
pix2pixhd_dir = Path(mainpath+'/src/pix2pixHD/')
sys.path.append(str(pix2pixhd_dir))


from data.data_loader import CreateDataLoader
from models.models import create_model
import util.util as util
from util.visualizer import Visualizer
import src.config.train_opt as opt
import tensorflow as tf

visualizer = Visualizer(opt)

rgb_image_float = tf.constant([
  [[1000, 0, 0], [0, 500, 1000]],
]) / 1000
print(rgb_image_float)

tinydict = {'Name': 6, 'Age': 7}
visualizer.plot_current_errors(tinydict, 0)