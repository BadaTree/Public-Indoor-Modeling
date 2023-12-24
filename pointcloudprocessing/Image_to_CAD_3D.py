import cv2

# 1. 이미지 열기
image = cv2.imread('C:/Users/SKH/Github_local/3D_Modeling_with_Three.js/pointcloudprocessing/data/00.jpg', cv2.IMREAD_COLOR)

# 2. 이미지를 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. 엣지 검출 (Canny 엣지 검출 사용)
threshold1 = 30  # 낮은 임계값
threshold2 = 100  # 높은 임계값
edges = cv2.Canny(gray_image, threshold1, threshold2)

# 4. 엣지 검출 결과 저장 또는 표시
cv2.imwrite('edges_result.jpg', edges)  # 결과를 파일로 저장

# 엣지 검출 결과 표시 (윈도우에서 열림)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
