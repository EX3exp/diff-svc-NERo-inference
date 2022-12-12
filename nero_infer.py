from utils.hparams import hparams
from preprocessing.data_gen_utils import get_pitch_parselmouth,get_pitch_crepe
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import utils
import librosa
import torchcrepe
from infer import *
import logging
from infer_tools.infer_tool import *

hparams.set_hparams('', '', '', True, True, True, True)
logging.getLogger('numba').setLevel(logging.WARNING)

# 工程文件夹名，训练时用的那个
project_name = "nero"
model_path = '/content/drive/MyDrive/diffsvc/NERo_diff-svc/model_ckpt_steps_30000.ckpt'
config_path = '/content/drive/MyDrive/diffsvc/NERo_diff-svc/config.yaml'
hubert_gpu = True
svc_model = Svc(project_name,config_path,hubert_gpu, model_path)
print('model loaded')
