# /scratch.py

import torch
from torch import nn
from gan.discriminator import Discriminator
from gan.generator import Generator

import math
import matplotlib.pyplot as plt

torch.manual_seed(111)



train_data_length = 1024
train_data = torch.zeros((train_data_length, 2))
train_data[:, 0] = 2 * math.pi * torch.rand(train_data_length)
train_data[:, 1] = torch.sin(train_data[:, 0])
train_labels = torch.zeros(train_data_length)
train_set = [(train_data[i], train_labels[i]) for i in range(train_data_length)]

batch_size = 32
train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)

#plt.plot(train_data[:, 0], train_data[:, 1], ".")
#plt.show()

lr = 0.001
num_epochs = 300
loss_function = nn.BCELoss()

discriminator = Discriminator()
generator = Generator()

optimizer_discriminator = torch.optim.Adam(discriminator.parameters(), lr=lr)
optimizer_generator = torch.optim.Adam(generator.parameters(), lr=lr)

for epoch in range(num_epochs):
	for n, (real_samples, _) in enumerate(train_loader):
		# Data for training the discriminator
		real_samples_labels = torch.ones((batch_size, 1))
		latent_space_samples = torch.randn((batch_size, 2))
		generated_samples = generator(latent_space_samples)
		generated_samples_labels = torch.zeros((batch_size, 1))
		all_samples = torch.cat((real_samples, generated_samples))
		all_samples_labels = torch.cat((real_samples_labels, generated_samples_labels))


		# Training the discriminator
		discriminator.zero_grad()
		output_discriminator = discriminator(all_samples)
		loss_discriminator = loss_function(output_discriminator.backward())
		optimizer_discriminator.step()


		# Data for training the generator
		latent_space_samples = torch_randn((batch_size, 2))


		# Training the generator
		generator = zero_grad()
		generated_samples = generator(latent_space_samples)
		output_discriminator_generated = discriminator(generated_samples)
		loss_generator = loss_function(output_discriminator_generated, real_samples_labels)
		loss_generator.backward()
		optimizer_generator.step()


		# Show loss
		if epoch % 10 == 0 and n == batch_size - 1:
			print(f"Epoch: {epoch} Loss D.: {loss_discriminator}")
			print(f"Epoch: {epoch} Loss G.: {loss_generator}")

latent_space_samples = torch.randn(100,2)
generated_samples = gemerator(latent_space_samples)

generated_samples = generated_samples.detach()
plt.plot(generated_samples[:, 0], generated_samples[:,1], ".")
plt.show()