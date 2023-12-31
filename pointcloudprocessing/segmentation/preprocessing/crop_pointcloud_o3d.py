import numpy as np
import open3d as o3d
import math
import itertools

if __name__ == '__main__':
    # Read point cloud:
    file_name = "point_cloud.ply"
    pcd = o3d.io.read_point_cloud("C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/"+file_name)

    # Create bounding box:
    bounds = [[-math.inf, math.inf], [-math.inf, math.inf], [0.2, 2]]  # set the bounds
    bounding_box_points = list(itertools.product(*bounds))  # create limit points
    bounding_box = o3d.geometry.AxisAlignedBoundingBox.create_from_points(
        o3d.utility.Vector3dVector(bounding_box_points))  # create bounding box object

    # Crop the point cloud using the bounding box:
    pcd_croped = pcd.crop(bounding_box)

    # Display the cropped point cloud:
    o3d.visualization.draw_geometries([pcd_croped])
