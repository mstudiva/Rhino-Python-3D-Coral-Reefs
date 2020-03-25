#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:02:34 2020

@author: iancombs
"""
import os, argparse, re

parser = argparse.ArgumentParser(description='Extract still images from .mp4 videos for use in Agisoft Metashape')
parser.add_argument("-f", type=str, help="number of frames per second you wish to extract from video. [default = 3fps]", action = "store", default='3')
parser.add_argument("-t", type=str, help="file extension. [default = MP4]", action ="store", default ="MP4")

args = parser.parse_args()
f = args.f
t = args.t

path = os.getcwd()

for fileName in [fileName for fileName in os.listdir(path)]:
    root, ext = os.path.splitext(fileName)
    if fileName.endswith(t):
        os.system("ffmpeg -i "+root+ext+" -vf fps="+f+" "+root+".%d.png")
    else:
        continue
