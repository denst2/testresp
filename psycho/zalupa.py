# import numpy as np
#
# A = np.array([
#     [[1, 2], [4, 5], [1, 2]],
#     [[1, 2], [4, 5], [1, 2]],
#     [[1, 2], [4, 5], [1, 2]],
# ])
# B = np.array([
#     [7, 8],
#     [8, 7],
#     [1, 8]
# ])
#
# print(A.shape, B.shape)
#
# C = A.reshape((A.shape[0], A.shape[1], A.shape[2],1)) + B.reshape((1, B.shape[0], 1, B.shape[1]))
# D = C.sum(1)
#
# print(D.shape)
#
C = A.reshape((A.shape[0],A.shape[1],A.shape[2],1)) + B.reshape((1,B.shape[0],1,B.shape[1]))
D = C.sum(1)