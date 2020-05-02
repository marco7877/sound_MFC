#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######
#
# Marco A. Flores-Coronado, Universidad Autónoma del Estado de Morelos (UAEM)
# 2020
#
# This code extracts audio information from a video file and then computes
# Mel Frecuency Cepstral Coefficient (MFCC) from the aforementioned. Resulting
# vectors may be saved as .txt file


############# Libraries ################
from moviepy.editor import *
import scipy
import glob
#############    main   #################
def main():
    openFile=True
    writeaudio=True
    MFCC=True
    analizeExtracted=True
    fileDirection="/home/marco/Documents/spyder-py3/stimuli/ga/"
    audioDirection="/direction/to/audio"
    files=glob.glob(fileDirection+"*.mp4")
    saveplain=True
    for videoDirection in files:  
        if (openFile==True):
            import sys
            print("Opening the target video and extracting audio")
            audiovisualfile=VideoFileClip(videoDirection)#opening video file
            audio=audiovisualfile.audio#extracting audio information
        if (writeaudio==True):
            import os
            print("Saving audio information as .wav file")
            output_path="./output/"
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            direction=videoDirection.split("/")
            syllable=direction[-2]
            ext=direction[-1]
            ext=ext.split(".")
            ext=ext[0]
            name=output_path+syllable+ext+".wav"
            audio.write_audiofile(name)
            audiovisualfile.close()#we need to close the objects
            audio.close()
        if (MFCC==True):
            import scipy.io.wavfile as wav
            from python_speech_features import mfcc
            if (analizeExtracted==True):
                (sampleRate,clip)=wav.read(name)
            else:
                (sampleRate,clip)=wav.read(audioDirection)
            mfcc_extracted=mfcc(clip, 
                                     sampleRate, 
                                     winlen=0.025,#width of the analysis window (ms)
                                     winstep=0.01,#step within windows (s)
                                     numcep=13,#number of cepstrals exctracted
                                     nfilt=26,#number of filters used for mfcc
                                     nfft=512)#number of fast Fourier Transform from
                                     #which mfcc are extracted
        if (saveplain==True):
            text_path="./plain/"
            if not os.path.exists(text_path):
                os.makedirs(text_path)
            direction=videoDirection.split("/")
            syllable=direction[-2]
            ext=direction[-1]
            ext=ext.split(".")
            ext=ext[0]
            document=text_path+syllable+ext+".csv"
            from numpy import savetxt
            savetxt(document,mfcc_extracted,fmt='%1.32f',delimiter=",")
if __name__ == "__main__":
    main()
