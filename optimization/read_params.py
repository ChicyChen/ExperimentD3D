import numpy as np

# paper's prediction
para_path = "/home/siyich/siyich/d3d_exp/exp_refrigerator/params/b005-0001/10900/1_511_5466/params.npy"

# our's prediction
# para_path = "/home/siyich/d3d-hoi/optimization/exp_refrigerator/params/b005-0001/10068/1_1_5466/params.npy"
para = np.load(para_path, allow_pickle=True)
print(para)