#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib.pyplot import *
import skimage
import skimage.io
import copy
import math

snippet_w = 512
add_all_fft = True
nr_pixels = 10000

class Tester():

    def __init__(self):
        # every observed snippet (512,512) is reduced to a patch of 1024 (32,32)
        col = range(1024)
        col.append('name')
        self.printer_types = np.array(())

        # (1) imgs with their class
        self.data = pd.DataFrame(columns=col)
        self.train = pd.DataFrame()
        col2 = range(snippet_w*snippet_w)
        col2.append('name')
        self.questioned_data = pd.DataFrame(columns=col2)
        self.statistics = pd.DataFrame()
        self.cor_matrix = np.array(())


    def loadimg(self,path):
        #qimg = QtGui.QImage()
        col = range(1024)
        col.append('name')
        questioned = pd.DataFrame(columns=col)

        if not add_all_fft:
            eigen = pd.read_pickle("knowledge/eigenData.pkl")
            eigenData = np.matrix(eigen)
            # filename = QtGui.QFileDialog.getOpenFileName(
            #            self, 'Open File', '', 'Images (*.png *.xpm *.jpg)')
            # qimg.load(filename)
            print("image is loaded.")

        #pixmap = QtGui.QPixmap.fromImage(qimg) # show loaded image in screen (too large)
        #self.lbl2.setPixmap(pixmap) # show loaded image in screen (too large)

        #tmp = skimage.io.imread(str(filename))
        tmp = skimage.io.imread(str(path))

        if tmp.size == 0:
            print("Image could not be load: ")
            print(path)
            #return False

        if(len(tmp.shape) == 3):
            tmpGrey = tmp[:,:,0]*0.0722 + tmp[:,:,1]*0.7152 + tmp[:,:,2]*0.2126
        # compute FFT spectra for serveral segments
        a=0
        # number of pixels per segents
        nperseg=[512,512]

        # number of pixels which overlap
        noverlap = np.empty([2], dtype=int)
        noverlap[0] = 0 #nperseg[0] // 2
        noverlap[1] = 0 #nperseg[1] // 2
        # number of pixels to move each segment
        step = np.empty([len(tmpGrey.shape)], dtype=int)
        step[0] = nperseg[0] - noverlap[0]
        step[1] = nperseg[1] - noverlap[1]

        # number of segments in one scanned image (in both dimensions)
        segment_count = np.empty([len(tmpGrey.shape)], dtype=int)
        segment_count[0] = (tmpGrey.shape[0]-noverlap[0])//step[0]
        segment_count[1] = (tmpGrey.shape[1]-noverlap[1])//step[1]

        # for(each segment in img): cut of segment
        for i in range(0, segment_count[0]-1):
            for j in range(0, segment_count[1]-1):
                # segment as copy of img snippet
                start_i = i*nperseg[0]
                start_j = j*nperseg[1]
                segment = tmpGrey[start_i:(start_i+nperseg[0]),start_j:(start_j+nperseg[1])]
                # cut relevant data out of scanned image
                #tmpGreySegment = tmpGrey[:,range(96,160,2)]
                #tmpGreySegment = tmpGreySegment[range(80,176,3),:]
                #tmpGreySegment = tmpGreySegment.reshape(1024)
                #tmpGreySegment = tmpGreySegment.tolist() + [curr]
                # windowing function on segment
                # build 1d window
                segment_hanning = copy.copy(segment)

                # hanning vectors
                u_vector = np.hanning(segment.shape[0])#eine Zeile
                v_vector = np.hanning(segment.shape[1])#eine Spalte

                # 2d hanning matrix
                for u in range(0,segment.shape[0]-1):
                    for v in range(0,segment.shape[1]-1):
                        segment_hanning[u][v] = np.multiply(u_vector[u], v_vector[v])*255

                segment_windowed = copy.copy(segment)

                #img.astype(float64)
                #np.int8(z)
                threshold = 200
                # then break (but for later average computation remove 1 from valid_segments or something)
                average_brightness = 0
                ## multiply hanning window to image
                for u in range(0,segment.shape[0]-1):
                    #img_hanning[u] = np.multiply(u_vector[u], v_vector)
                    t_max = np.float64(0)
                    for v in range(0,segment.shape[1]-1):
                        average_brightness += np.float64(segment[u][v])
                        t = np.float64(segment_hanning[u][v])/255
                        segment_windowed[u][v] = t * np.float64(segment[u][v]) + (1-t) * 255
                        #segment_windowed[u][v] = np.multiply(np.float64(img[u][v]), img_hanning[u][v])/255
                        if t>t_max:
                            t_max=np.float64(t)
                average_brightness *= 1/segment.size
                if average_brightness >= threshold:
                    print("over threshold")
                else:
                    # compute fft for every segment in an image
                    f = np.fft.fft2(segment_windowed)
                    fshift = np.fft.fftshift(f)
                    magnitude_spectrum = 20*np.log(np.abs(fshift))

                    # darken region around axis
                    middle = int(magnitude_spectrum.shape[0]/2)
                    magnitude_spectrum[middle-5:middle+5,:] = magnitude_spectrum.min()
                    magnitude_spectrum[:,middle-5:middle+5] = magnitude_spectrum.min()

                    # add segment fft to data_detailed
                    self.questioned_data.loc[a] = magnitude_spectrum.reshape(magnitude_spectrum.size).tolist() + ['Q']


    def inspect(self):

        class_column = self.questioned_data.shape[1]-1
        nr_segments = self.questioned_data.shape[0]
        printers_nr = np.arange(self.printer_types.size)

        sum = np.zeros((self.printer_types.size))

        for p in range(self.printer_types.size):
            sum[p] = np.sum(np.sum(self.cor_matrix[p]))

        correlation_list = np.zeros((nr_segments, self.printer_types.size))

        # prove every segment
        for i in range(self.questioned_data.shape[0]):

            # prove similarity - correlation of segment fft with additive spcectras
            for p in range(len(self.printer_types)):
                correlation_list[i,p] = np.dot(self.questioned_data.ix[i,:class_column], self.cor_matrix[p,:,:].reshape(class_column))

        result = np.zeros(len(self.printer_types))

        for row in range(correlation_list.shape[0]):
            likeliest_class = np.where(correlation_list[row,:]==correlation_list[row,:].max())[0][0]
            result[likeliest_class] += 1

        s = result.sum()

        result_stats = list()

        for p in range(len(self.printer_types)):
            similiarity = 100 * result[p]/s
            print self.printer_types[p]+ ":     " + "{0:.2f}".format(similiarity) + "%"
            result_stats.append([self.printer_types[p], "{0:.2f}".format(similiarity) + "%"])

        return result_stats


    def get_Learner(self):

        self.statistics = pd.read_pickle("knowledge/statistics.pkl")
        class_column = self.statistics.shape[1]-1
        self.printer_types = np.unique([printer for printer in self.statistics.ix[:,class_column]])
        self.cor_matrix = np.zeros((self.printer_types.size,snippet_w,snippet_w))

        if self.statistics.empty:
            print("No statistics file on memory.")
        else:
            print("got statistics!")

        for p in range(self.printer_types.size):
            self.cor_matrix[p] = pd.read_pickle("knowledge/corr_"+self.printer_types[p]+".pkl")


def main():

    tester = Tester()

    tester.get_Learner()
    tester.loadimg('images/idcards_all/Canon_Pro/idcard_15.jpg')
    tester.inspect()



if __name__ == '__main__':
    main()