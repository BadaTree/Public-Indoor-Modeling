import pyrender
import trimesh

# glb 파일 경로 C:\Users\SKH\Github_local\IndoorNavModel\pointcloudprocessing\process_gltf.py
glb_file_path = "C:/Users/SKH/Github_local/IndoorNavModel/pointcloudprocessing/data/gltfData/sample.glb"

# glb 파일 로드
scene = trimesh.load(glb_file_path)

# GLB 파일 로드 확인
if scene is None:
    print("Failed to load the GLB file.")
else:
    # scene.geometry가 비어 있는 경우 처리
    if not scene.geometry:
        print("No meshes found in the glb file.")
    else:
        # 메시 추출
        meshes = [scene.geometry[i] for i in range(len(scene.geometry))]
        
        # pyrender 렌더러 생성
        r = pyrender.OffscreenRenderer(viewport_width=800, viewport_height=600)

        # pyrender 렌더러에 메시 추가
        for mesh in meshes:
            pyrender_mesh = pyrender.Mesh.from_trimesh(mesh)
            scene = pyrender.Scene()
            scene.add(pyrender_mesh)

    # 렌더링 설정
    camera = pyrender.PerspectiveCamera(yfov=1.0, aspectRatio=1.0)
    scene.add(camera, pose=camera_pose)

    # 조명 설정 (선택 사항)
    light = pyrender.SpotLight(color=[1.0, 1.0, 1.0], intensity=10.0)
    light_pose = [[0, 0, 2]]  # 조명 위치
    scene.add(light, pose=light_pose)

    # pyrender 뷰어 열기
    viewer = pyrender.Viewer(scene, use_raymond_lighting=True)

    # 뷰어 닫기 전까지 유지
    viewer.render()