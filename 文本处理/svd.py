
import numpy as np
import matplotlib.pyplot as plt
la = np.linalg
# 例句： I love NLP.  I love deep learning. I enjoy learning.

words = ["I", "love", 'NLP', "deep", "learning", "enjoy"]
X = np.array([[0,2,0,0,0,1],
              [2,0,1,0,0,0],
              [0,1,0,0,0,0],
              [0,0,0,0,1,0],
              [0,0,0,1,0,1],
              [1,0,0,0,1,0],])
U, s, Vh = la.svd(X, full_matrices=False)
# 打印 U 矩阵的前两列
for i in range(len(words)):
    print(U[i, 0], U[i, 1], words[i])
    plt.text(U[i, 0], U[i, 1], words[i])
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()