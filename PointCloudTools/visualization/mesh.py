import trimesh

# Ply 파일 로드
mesh = trimesh.load_mesh('C:/Users/SKH/Github_local/3d/PointCloudTools/data/polycam.ply')

# 필요한 경우 메시를 정리하고 닫을 수 있습니다.
mesh.fix_normals()  # 법선 방향 조정
mesh.remove_degenerate_faces()  # 비정상적인 면 제거
mesh.remove_infinite_values()  # 무한한 값 제거
mesh.remove_duplicate_faces()  # 중복된 면 제거
mesh.remove_duplicate_vertices()  # 중복된 정점 제거

# 메시 시각화
mesh.show()
