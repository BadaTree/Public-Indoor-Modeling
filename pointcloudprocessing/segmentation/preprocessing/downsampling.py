import open3d as o3d
import numpy as np

if __name__ == '__main':
    # Read point cloud:
    file_name = "point_cloud.ply"
    pcd = o3d.io.read_point_cloud("C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/"+file_name)
    
    # Random down-sampling:
    random_pcd = pcd.voxel_down_sample(voxel_size=0.4)  # 변경된 부분
    
    # Uniform down-sampling:
    uniform_pcd = pcd.uniform_down_sample(every_k_points=200)

    # Voxel down-sampling:
    voxel_pcd = pcd.voxel_down_sample(voxel_size=0.4)

    # Translating point clouds and updating colors to display:
    points = np.asarray(random_pcd.points)
    points += [-3, 3, 0]
    random_pcd.points = o3d.utility.Vector3dVector(points)

    points = np.asarray(uniform_pcd.points)
    points += [0, 3, 0]
    uniform_pcd.points = o3d.utility.Vector3dVector(points)

    points = np.asarray(voxel_pcd.points)
    points += [3, 3, 0]
    voxel_pcd.points = o3d.utility.Vector3dVector(points)

    # Display:
    o3d.visualization.draw_geometries([pcd, random_pcd, uniform_pcd, voxel_pcd])

    # Save down-sampled point clouds to files
    o3d.io.write_point_cloud("random_downsampled.ply", random_pcd)
    o3d.io.write_point_cloud("uniform_downsampled.ply", uniform_pcd)
    o3d.io.write_point_cloud("voxel_downsampled.ply", voxel_pcd)
