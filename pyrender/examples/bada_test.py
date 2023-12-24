import trimesh
from pyrender import PerspectiveCamera,\
                     Mesh, Scene, Viewer

import numpy as np
import threading
import time

# 함수로 뷰어를 실행하는 코드
def run_viewer(scene):
    viewer = Viewer(scene, use_raymond_lighting=True, run_in_thread=True)

# 회전을 처리하는 함수
def rotate_scene_automatically(scene):
    viewer = Viewer(scene, use_raymond_lighting=True, run_in_thread=True)
    while True:
        # 회전 각도 및 속도 설정
        angle = 0.5  # 회전 각도 (라디안)
        rotation_speed = 0.05  # 회전 속도

        # 현재 뷰어의 시점을 가져와 회전합니다.
        with viewer.lock:
            camera_node = scene.get_nodes(name="CameraNode")[0]
            scene.set_pose(camera_node, np.eye(4))  # 뷰어 재설정
            scene.viewer.interactive_scene.set_pose(camera_node, "camera", zangle=-angle)
            scene.viewer.interactive_scene.render()

        time.sleep(rotation_speed)

# 3D 모델 로드 및 Scene 생성
bottle_gltf = trimesh.load('C:/Users/SKH/Github_local/3d/pyrender/examples/models/poly5.glb')
bottle_trimesh = bottle_gltf.geometry[list(bottle_gltf.geometry.keys())[0]]
mesh = Mesh.from_trimesh(bottle_trimesh)

scene = Scene()
scene.add(mesh)

# 뷰어 스레드 시작
viewer_thread = threading.Thread(target=run_viewer, args=(scene,))
viewer_thread.start()

# 회전 스레드 시작
rotate_thread = threading.Thread(target=rotate_scene_automatically, args=(scene,))
rotate_thread.start()

# 스레드가 실행 중인 동안 메인 스레드는 여전히 활성화된 상태로 유지됩니다.
viewer_thread.join()
rotate_thread.join()
