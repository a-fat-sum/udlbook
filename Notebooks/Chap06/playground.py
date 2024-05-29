import numpy as np

n_steps = 81
batch_size = 5
alpha = 0.6
beta = 0.6
momentum = np.zeros([2,1])
phi_all = np.zeros((2,n_steps+1))
phi_all[0,0] = -1.5
phi_all[1,0] = 6.5
x = phi_all[:,3]
y = np.zeros([2,1])
z = x - y 
k = 5
