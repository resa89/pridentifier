from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.pyplot import *
import os
from ftplib import FTP

from model import inspector

dbimport = False  # True: imgs from ftp server, False: imgs from local folder

# parameter for snippet features
snippet_w = 512
nr_pixels = 10000
scale_fft = False

# method: adding spectra
add_all_fft = True

# method: pca
pca_amount = 20

TRAINING = True  # if False: then generating test dataset statistics

col = [i for i in range(1024)]
col_large = [i for i in range(512*512)]
col.append('name')
col_large.append('name')

printer_types = np.array(())

## path handling
#if dbimport:
#    #setupDB()
#    ROOTDIR = FTP.pwd()
#    DIRS = FTP.nlst()
#else:
pwd = os.getcwd()
ROOTDIR = pwd + '/../data/images/idcards-testset'  # id #idcards_all
SUBPATH = 'the_same_large'
DIRS = os.listdir(ROOTDIR)

# correctPositiveTrain = [0 for i in xrange(len(dirs))]  statt 5
correctPositiveTrain = [0 for i in range(len(DIRS))]
correctNegativeTrain = [0 for i in range(len(DIRS))]
falsePositiveTrain = [0 for i in range(len(DIRS))]
falseNegativeTrain = [0 for i in range(len(DIRS))]
correctPositiveTest = [0 for i in range(len(DIRS))]
correctNegativeTest = [0 for i in range(len(DIRS))]
falsePositiveTest = [0 for i in range(len(DIRS))]
falseNegativeTest = [0 for i in range(len(DIRS))]

hitsPerClassOfInspectedSegments = [0 for i in range(len(DIRS))]

# length of features for each printer
train_feature_length = [0 for i in range(len(DIRS))]
test_feature_length = [0 for i in range(len(DIRS))]