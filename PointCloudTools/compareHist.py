import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
image1_path = 'C:/Users/SKH/Github_local/IndoorNavModel/PointCloudTools/data/image5.png'
image2_path = 'C:/Users/SKH/Github_local/IndoorNavModel/PointCloudTools/data/image55.png'
print(image1_path,image2_path)
# 이미지 파일 불러오기
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# 이미지 불러오기에 실패한 경우 처리
if image1 is None or image2 is None:
    print("이미지 파일을 읽을 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 이미지의 크기 확인
    height1, width1, _ = image1.shape
    height2, width2, _ = image2.shape

    print(f"이미지 1의 크기: {width1} x {height1}")
    print(f"이미지 2의 크기: {width2} x {height2}")

    # 이미지 크기가 같은지 확인
    if width1 != width2 or height1 != height2:
        print("이미지 크기가 다릅니다. 크기를 맞춰주세요.")
    else:
        # 이미지 크기가 동일한 경우 이미지 비교 작업을 진행
        # BGR 색상을 HSV 색상으로 변환
        image1_hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
        image2_hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

        # 이미지의 히스토그램 계산
        hist_image1 = cv2.calcHist([image1_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
        hist_image2 = cv2.calcHist([image2_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        # 히스토그램 비교
        similarity = cv2.compareHist(hist_image1, hist_image2, cv2.HISTCMP_CORREL)
        print(f"두 이미지의 유사성 CORREL: {similarity*100:.2f}%")
        similarity = cv2.compareHist(hist_image1, hist_image2, cv2.HISTCMP_CHISQR)
        print(f"두 이미지의 유사성: {similarity}")
        similarity = cv2.compareHist(hist_image1, hist_image2, cv2.HISTCMP_INTERSECT)
        print(f"두 이미지의 유사성: {similarity}")
        similarity = cv2.compareHist(hist_image1, hist_image2, cv2.HISTCMP_BHATTACHARYYA)
        print(f"두 이미지의 유사성 BHATTACHARYYA: {similarity*100:.2f}%")
# 이미지가 올바르게 불러와졌는지 확인
if image1 is None or image2 is None:
    print("이미지 파일을 읽을 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 이미지 크기 확인 (두 이미지는 같은 크기여야 함)
    if image1.shape == image2.shape:
        # 두 이미지의 크기가 동일한 경우 각 픽셀 비교 수행
        difference = cv2.subtract(image1, image2)
        b, g, r = cv2.split(difference)

        # 모든 채널의 차이를 합하여 이미지 간의 전체적인 차이 계산
        total_diff = cv2.countNonZero(cv2.add(cv2.add(b, g), r))
        
        # 이미지 유사도(유사성)
        similarity = (total_diff / (image1.size / image1.shape[2])) * 100  # 이미지 크기로 나누어 유사도 계산
        
        print(f"두 이미지의 유사도: {similarity:.2f}%")
    else:
        print("이미지 크기가 다릅니다. 크기를 맞춰주세요.")

  

# 데이터
methods = ['Min', 'Max', 'Avg']
similarities = [71, 85, 78]  # 유사도 데이터 (예를 들어서)

# 표 그리기
plt.figure(figsize=(5, 4))  # 표의 크기 지정

plt.bar(methods, similarities, color='#872434')  # 막대 그래프 생성

#plt.xlabel('Methods')  # x축 레이블
plt.ylabel('Similarity (%)' , fontsize=14)  # y축 레이블
plt.title('Histogram value-based comparison', fontsize=18)  # 표 제목

plt.ylim(0, 100)  # y축 범위 설정 (0부터 100까지)

plt.xticks(rotation=30,fontsize=15)  # x축 레이블 회전

plt.tight_layout()  # 레이아웃 조정
plt.show()  # 표 표시
