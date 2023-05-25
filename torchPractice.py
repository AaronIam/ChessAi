import torch

ones = torch.ones(2,2)
twos = torch.ones(2,2) + 1
rand = torch.rand(2,2)
rand2 = torch.rand(2,2)
print(abs(rand - rand2))
#print(ones + twos)
#print(twos)