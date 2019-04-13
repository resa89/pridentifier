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
#col = [i for i in range(1024)]
#col_large = [i for i in range(512*512)]
#col.append('name')
#col_large.append('name')
