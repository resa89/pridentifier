from matplotlib.pyplot import *
import os
from ftplib import FTP

# [1] build parameters (constants)
DB_IMPORT = False    # True: imgs from ftp server, False: imgs from local folder
ACCUMULATED_SPECTRA = True  # method: adding spectra
TRAINING = True     # if False: then generating test dataset statistics
pca_amount = 20     # method: pca

# [2] user-configurable runtime parameters (constants)
SNIPPET_WIDTH = 512
NUMBER_PIXELS = 10000 #TODO: make number of pixels configurable
SUBPATH = 'data/runtime'

# [3] system-configurable runtime parameters (global variables in one module)
PRINTER_TYPES = np.array(())
NUMBER_OF_CLASSES = 0


# path handling
if DB_IMPORT:
    #setupDB()
    ROOTDIR = FTP.pwd()
    DIRS = FTP.nlst()
else:
    pwd = os.getcwd()
    ROOTDIR = pwd #+ '/../data/images/idcards-testset'  # id #idcards_all
    #SUBPATH = 'the_same_large'
    DIRS = os.listdir(ROOTDIR)



# statistical analysis and result
col = [i for i in range(1024)]
col_large = [i for i in range(512*512)]
col.append('name')
col_large.append('name')

# correctPositiveTrain = [0 for i in xrange(len(dirs))]  statt 5
correctPositiveTrain = [0 for i in range(len(DIRS))]
correctNegativeTrain = [0 for i in range(len(DIRS))]
ACCUMULATED_SPECTRAfalsePositiveTrain = [0 for i in range(len(DIRS))]
falseNegativeTrain = [0 for i in range(len(DIRS))]
correctPositiveTest = [0 for i in range(len(DIRS))]
correctNegativeTest = [0 for i in range(len(DIRS))]
falsePositiveTest = [0 for i in range(len(DIRS))]
falseNegativeTest = [0 for i in range(len(DIRS))]

hitsPerClassOfInspectedSegments = [0 for i in range(len(DIRS))]

train_feature_length = [0 for i in range(len(DIRS))]    # length of features for each printer
test_feature_length = [0 for i in range(len(DIRS))]     # length of features for each printer


#RUNTIME_PATH = SUBPATH
