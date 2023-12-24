import open3d as o3d
import numpy as np
from scipy import interpolate
import os

# 포인트 클라우드 데이터를 읽어옵니다.
file_path = "C:/Users/SKH/Github_local/3d/pointcloudprocessing/data/test/"
file_name = "poly5.glb"

pcd = o3d.io.read_point_cloud(file_path + file_name)

# 포인트 클라우드에서 포인트들의 좌표를 추출합니다.
points = np.asarray(pcd.points)

# 처음 입력 포인트 클라우드 시각화
o3d.visualization.draw_geometries([pcd])

# 2. 시각화 - OpenGL 렌더러 사용
vis = o3d.visualization.VisualizerWithKeyCallback()
vis.create_window(window_name='Open3D Example', width=800, height=600)
render_option = vis.get_render_option()
render_option.background_color = np.asarray([0, 0, 0])
vis.add_geometry(pcd)
vis.run()

# .ply 파일 불러오기
mesh = o3d.io.read_triangle_mesh(pcd)

# Material Preview Mode와 같이 시각화 설정
o3d.visualization.draw_geometries([mesh], mesh_show_wireframe=True)

# Statistical Outlier Removal 이용한 이상치 제거
cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
inlier_pcd = pcd.select_by_index(ind)
print("Statistical Outlier Removal")
o3d.visualization.draw_geometries([inlier_pcd])

# 데이터 다운샘플링
downsampled_pcd = inlier_pcd.voxel_down_sample(voxel_size=0.05)
print("Downsampled")
o3d.visualization.draw_geometries([downsampled_pcd])

# 스플라인 보간
downsampled_points = np.asarray(downsampled_pcd.points)
x = downsampled_points[:, 0]
y = downsampled_points[:, 1]
z = downsampled_points[:, 2]

# 스플라인 함수 설정
tck, _ = interpolate.splprep([x, y, z], s=0)
u = np.linspace(0, 1, num=1000)
interpolated_points = interpolate.splev(u, tck)

interpolated_pcd = o3d.geometry.PointCloud()
interpolated_pcd.points = o3d.utility.Vector3dVector(np.column_stack(interpolated_points))
print("Interpolated")
o3d.visualization.draw_geometries([interpolated_pcd])

# 압축 작업 (예: 랜덤 샘플링)
sample_size = min(1000, len(interpolated_points[0]))  # 원본 배열 크기보다 큰 샘플 크기를 방지
sampled_indices = np.random.choice(len(interpolated_points[0]), size=sample_size, replace=False)
compressed_points = np.array([interpolated_points[0][sampled_indices], interpolated_points[1][sampled_indices], interpolated_points[2][sampled_indices]]).T
compressed_pcd = o3d.geometry.PointCloud()
compressed_pcd.points = o3d.utility.Vector3dVector(compressed_points)
print("Compressed")
o3d.visualization.draw_geometries([compressed_pcd])

# 압축된 데이터를 PLY 파일로 저장
output_directory = "C:/Users/SKH/Github_local/3d/pointcloudprocessing/data/ProcessedData/"
os.makedirs(output_directory, exist_ok=True)
output_ply_file = os.path.join(output_directory, "processed_" + file_name)
o3d.io.write_point_cloud(output_ply_file, inlier_pcd)

print(f"Compressed point cloud saved to {output_ply_file}")
