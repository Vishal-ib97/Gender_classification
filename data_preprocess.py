import os
import numpy as np
from sklearn.model_selection import train_test_split
import random

# train and validation data

data_dir = r"C:\Users\HP\Desktop\New folder\gender\aligned"

dir = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

file_male = []
file_female = []

for d in dir:
  if d[-1] == "M":
    file_male += [os.path.join(d, g) for g in os.listdir(d)]
  else:
    file_female += [os.path.join(d, g) for g in os.listdir(d)]

file_male = random.sample(file_male, 1000)
file_female = random.sample(file_female, 1000)
m_y = np.zeros([len(file_male), 1])
f_y = np.ones([len(file_female), 1])

male_train, male_valid, y, y1 = train_test_split(file_male, m_y, random_state = 0, test_size = 0.2)
female_train, female_valid, y, y1 = train_test_split(file_female, f_y, random_state = 0, test_size = 0.2)

train_dir = r"C:\Users\HP\Desktop\train"
test_dir = r"C:\Users\HP\Desktop\test"
valid_dir = r"C:\Users\HP\Desktop\valid"
m = r"/male/"
f = r"/female/"

for d in male_train:
  os.rename(d, train_dir+m+d[51:])
for d in male_valid:
  os.rename(d, valid_dir+m+d[51:])

for d in female_train:
  os.rename(d, train_dir+f+d[51:])
for d in female_valid:
  os.rename(d, valid_dir+f+d[51:])
  
  
# test data
  
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

for d in file_male:
  os.rename(d, t_dir+m+d[48:])
  
for d in file_female:
  os.rename(d, t_dir+f+d[48:])