# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:32:18 2019

@author: Osama Arif
"""

from PIL import Image
import os, sys, fnmatch
import argparse
from tqdm import tqdm 


def resize_image(path, max_size):
  if path[-1] != '/':
    path = path + '/'

  dirs = os.listdir(path)
  for subdir in tqdm(dirs):
      subdir += '\\'
      if os.path.isdir(path+subdir):
          for item in tqdm(os.listdir(path+subdir)):
            if os.path.isfile(path+subdir+item) and (fnmatch.fnmatch(item, '*(1)*')):
                os.remove(path+subdir+item)
                continue
            if os.path.isfile(path+subdir+item) and not (fnmatch.fnmatch(item, '*_cmp*')):
                try:
                    img = Image.open(path+subdir+item)
                    f,e = os.path.splitext(path+subdir+item)
                    img.save(f+'_cmp'+e,optimize=True,quality=max_size)
                    os.remove(path+subdir+item)
                except:
                    continue

            else:
                continue
            
                

def main():
  parser = argparse.ArgumentParser(
    description='given a folder path, resize all images inside')
  parser.add_argument(
    '--path',
    type=str,
    help='full path to the target folder')
  parser.add_argument(
    '--max_size',
    type=float,
    help='the largest size that you want an image to be (in pixels)')

  args = parser.parse_args()

  resize_image(args.path, args.max_size)

#python compress.py --path='/your/full/image/directory' --max_size='512'
if __name__ == '__main__':
  main()