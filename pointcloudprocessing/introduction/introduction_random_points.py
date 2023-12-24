import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    # let's create random point cloud:
    number_points = 50
    pcd = np.random.rand(number_points, 3)  # random points from a uniform distribution over [0, 1)
    print(pcd)

    # Create Figure:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(pcd[:, 0], pcd[:, 1], pcd[:, 2])
    # label the axes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Random Point Cloud")
    # display:
    plt.show()
