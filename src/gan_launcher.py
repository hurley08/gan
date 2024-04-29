# /scratch.py

import torch
from torch import nn

import math
import matplotlib.pyplot as plt



class Launcher():
	def __init__(self, seed=111, d_length=1024, dimensions=2):
		torch.manual_seed(seed)
		self.train_data_length = d_length
		self.train_data =  torch.zeros((d_length, 2))
		self.train_data[:, 0] = 2 * math.pi * torch.rand(d_length)
		self.train_data[:, 1] = torch.sin(self.train_data[:, 0])
		self.train_labels = torch.zeros(d_length)
		self.train_set = [(self.train_data[i], self.train_labels[i]) for i in range(d_length)]

		print('Launchar has been instantiated')


l = Launcher()
