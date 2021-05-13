import numpy as np
import scipy as sp
from scipy import sparse


eye = np.eye(4)

sparse_matrix = sparse.csr_matrix(eye)
print(sparse_matrix)
