# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:06:40 2020

@author: Vishal
"""
import os
import random

test_dir = r"C:\Users\HP\Desktop\New folder\gender\test"
dir = [os.path.join(test_dir, d) for d in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, d))]

test_names = []
file_male = []
file_female = []

for d in dir:
  if d[-1] == "M":
    file_male += [os.path.join(d, g) for g in os.listdir(d)]
  else:
    file_female += [os.path.join(d, g) for g in os.listdir(d)]



file_male = random.sample(file_male, 250)
file_female = random.sample(file_female, 250)

t_dir = r"C:\Users\HP\Desktop\test2"
m = r"/male/"
f = r"/female/"

for d in file_male:
  os.rename(d, t_dir+m+d[48:])
  
for d in file_female:
  os.rename(d, t_dir+f+d[48:])
  
  
