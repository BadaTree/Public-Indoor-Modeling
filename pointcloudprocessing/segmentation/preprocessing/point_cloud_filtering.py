import open3d as o3d
import numpy as np

if __name__ == '__main__':
    # Read point cloud:
    file_name = "coex.ply"
    pcd = o3d.io.read_point_cloud("C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/"+file_name)
    # Down sampling to reduce the running time:
    # voxel_down_sample 함수를 사용하여 3D 포인트 클라우드를 다운샘플링합니다. 
    # 이를 통해 더 작은 데이터 세트로 작업할 수 있으며 실행 시간을 단축할 수 있습니다.
    pcd = pcd.voxel_down_sample(voxel_size=0.02) 

    # Radius outlier removal: remove_radius_outlier 함수를 사용하여 반경 이상치 제거를 수행합니다. 
    # 이 함수는 지정된 반경 내에 너무 적은 포인트가 있는 클라우드 포인트를 제거합니다. 
    # 결과적으로 이상치로 표시된 포인트들을 outlier_rad_pcd로 가져와서 색을 붙입니다.
    pcd_rad, ind_rad = pcd.remove_radius_outlier(nb_points=16, radius=0.05)
    outlier_rad_pcd = pcd.select_by_index(ind_rad, invert=True)
    outlier_rad_pcd.paint_uniform_color([1., 0., 1.])

    # Statistical outlier removal: remove_statistical_outlier 함수를 사용하여 통계 이상치 제거를 수행합니다. 
    # 이 함수는 각 포인트 주변에 있는 이웃 포인트 수와 표준 편차 비율을 기반으로 이상치를 제거합니다. 
    # 이상치로 표시된 포인트들을 outlier_stat_pcd로 가져와서 색을 붙입니다.
    pcd_stat, ind_stat = pcd.remove_statistical_outlier(nb_neighbors=20,
                                                 std_ratio=2.0)
    outlier_stat_pcd = pcd.select_by_index(ind_stat, invert=True)
    outlier_stat_pcd.paint_uniform_color([0., 0., 1.])

    # Translate to visualize: 
    # 시각화를 위해 이상치 제거된 포인트 클라우드와 이상치 포인트 클라우드를 3D 공간에 표시하기 위해 포인트 위치를 조정합니다.
    points = np.asarray(pcd_stat.points)
    points += [5, 0, 0]
    pcd_stat.points = o3d.utility.Vector3dVector(points)

    points = np.asarray(outlier_stat_pcd.points)
    points += [10, 0, 0]
    outlier_stat_pcd.points = o3d.utility.Vector3dVector(points)

    # Display:
    o3d.visualization.draw_geometries([pcd_stat, pcd_rad, outlier_stat_pcd, outlier_rad_pcd])



