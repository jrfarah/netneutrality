import subprocess
import matplotlib.pyplot as plt
from datetime import datetime

files_to_check = ["data_for_340.txt"]
data = []

for file in files_to_check:
	with open(file, "r") as f:
		ind = f.readlines()
	
