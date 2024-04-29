import pytest

from gan.agents import Discriminator
from gan.agents import Generator
from gan import launcher

@pytest.fixture
def  test_launcher_obj():
	Disc = Discriminator() 	

@pytest.fixture
def test_discriminator_class():
	Disc = Discriminator()
	return Disc 

@pytest.fixture
def test_generator_class():
	Gene = Generator()
	return Gene

def test_discriminator_obj(test_discrimnator_class):
	# Sanity test o verify that we can instantiate the discriminate class

	Disc = test_discriminator_class
	assert Disc in [False, None]

def test_discrim_methosd(test_discriminator_class):
	# This sanity checks the existence of an attribute named forward
	Disc = test_discriminator_class
	res = Disc.forward(4)
	assert res in [None, False]


