import trimesh
import open3d as o3d
import numpy as np
import os
import json

# 파일 경로 및 이름 설정
output_dir = "C:/Users/SKH/Github_local/3d/pointcloudprocessing/data/"
gltf_filename = "10.24.gltf"  # 읽어들일 .gltf 파일명 설정

# .gltf 파일 읽기
gltf_file_path = os.path.join(output_dir, gltf_filename)
if not os.path.exists(gltf_file_path):
    print(f"Error: The .gltf file '{gltf_file_path}' does not exist.")
    exit()

# 파일 읽어서 일부 내용 출력
with open(gltf_file_path, "r") as gltf_file:
    gltf_data = json.load(gltf_file)

# Mesh 데이터 추출
mesh_data = gltf_data["meshes"][0]  # Assuming there's only one mesh

# Extract vertices from POSITION accessor
position_accessor_index = mesh_data["primitives"][0]["attributes"]["POSITION"]
position_accessor = gltf_data["accessors"][position_accessor_index]
buffer_view_index = position_accessor["bufferView"]

# Extract the bufferView information
buffer_view = gltf_data["bufferViews"][buffer_view_index]
buffer_index = buffer_view["buffer"]
byte_offset = buffer_view["byteOffset"]
byte_length = buffer_view["byteLength"]

# Read the binary data from the buffer
with open(os.path.join(output_dir, gltf_data["buffers"][buffer_index]["uri"]), 'rb') as buffer_file:
    buffer_data = buffer_file.read()

# Extract vertices from binary data
vertices = np.frombuffer(buffer_data, dtype=np.float32, offset=byte_offset, count=byte_length // 4)

# Reshape vertices to match the shape expected by Trimesh
vertices = vertices.reshape((-1, 3))

# Create the Trimesh object
mesh = trimesh.Trimesh(vertices=vertices)

# Trimesh 메시를 Open3D TriangleMesh로 변환
vertices = np.array(mesh.vertices)
triangles = np.array(mesh.faces)
mesh_o3d = o3d.geometry.TriangleMesh()
mesh_o3d.vertices = o3d.utility.Vector3dVector(vertices)
mesh_o3d.triangles = o3d.utility.Vector3iVector(triangles)

# Open3D 시각화
o3d.visualization.draw_geometries([mesh_o3d])
