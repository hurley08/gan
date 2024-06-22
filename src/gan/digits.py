# gan/digits.py

import torch 
from torch import nn

import math
import matplotlib.pyplot as plt
import torchvision
import torchvision.transforms as transforms


torch.manual_seed(111)
device = ""
if torch.cuda.is_available():
	device = torch.device("cuda")
else:
	device = torch.device("cpu")





transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, ), (0.5,))])
train_set = torchvision.datasets.MNIST(root=".", train=True, download=True, transform=transform)
batch_size = 32
train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)

real_samples, mnist_labels = next(iter(train_loader))
for i in range(16):
	ax = plt.subplot(4, 4, i+1)
	plt.imshow(real_samples[i].reshape(28, 28), cmap='gray_r')
	plt.yticks([])	
	plt.xticks([])