from pyrender import Scene, Viewer
import trimesh
import requests

# GLTF 모델의 URL
gltf_url = "https://github.com/KhronosGroup/glTF-Sample-Models/raw/master/2.0/Duck/glTF/Duck.gltf"

# GLTF 모델 다운로드
gltf_data = requests.get(gltf_url)

# requests.get()으로 얻은 응답 객체에서 content 대신 content 바이트 데이터를 사용
gltf_bytes = gltf_data.content

# Trimesh로 GLTF 모델 로드
duck = trimesh.load(gltf_bytes, file_type='gltf')

# Pyrender Scene 생성
scene = Scene(ambient_light=[1.0, 1.0, 1.0])

# Trimesh에서 Pyrender Mesh 생성
duckmesh = scene.add(duck)

# Viewer를 사용하여 시갤화
viewer = Viewer(scene, use_raymond_lighting=True)

# 뷰어 윈도우를 열어서 모델을 시갤화
viewer.render()
