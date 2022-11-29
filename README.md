# The-system-for-LIS-patients
-------------------------------------



<p align="center"><img src="https://user-images.githubusercontent.com/74172467/204238519-4af4fd86-d7ce-4318-b5f7-b104204d4269.gif" width= "700">
    
💫# Full demo on -> [Youtube](https://youtu.be/MI3txBwcGmY)💫

    
    
# 사용된 기기✏

 <img src="https://user-images.githubusercontent.com/74172467/204225893-72915129-70ce-499b-bff9-c03f2175a322.png" width="300" height = "300">




MAVE: 전전두엽(Fp1, Fp2) 두 채널에서 EEG를 비침습적 방법으로 수집한다.

# 모듈구성✏
- FindBlink.py: 눈 깜빡임을 검출
- analysis.py:  파일을 읽고 눈 깜빡임을 검출한 뒤 검출했다면 그에 맞는 결과 반환 
- App.py : flask 실행
- Preprocessing.py : 전처리 과정 (노이즈 제거, band-pass filter, FFT)
- Hz_potential.py : 해당 구간과 주파수의 평균 전위 값
- Index_cal.py : time 문자열을 시간으로 변환 및 time 비교하여 index 반환
- Load_data.py : mave 데이터 를 실시간으로 읽어 옴
- Ssvep.py : ssvep 주파수 데이터 분석을 실행한 뒤 보고 있는 주파수 반환

# 모듈 별 설명✏

## FinfBlink ✔

눈 깜박임으로 인한 뇌파데이터의 노이즈를 이용하여 눈깜박임을 검출합니다.
5초 사이에 눈 깜박임이 다수 검출된다면 사용자가 서비스 시작을 위한 의도적 행동이라 판단합니다.

1) raw_data에서 최근 5초 동안의 index를 가져옵니다.
2) find_peak 함수를 사용하여 피크를 검출합니다. 눈 깜박임으로 인한 노이즈를 상대적으로 강하기 때문에 height, distance 파라미터를 반복적 실험 후 적절히 조정하였습니다.
3) peak의 개수가 7개 이상이면 마지막 피크의 index위치를 반환합니다.

![Untitled](https://user-images.githubusercontent.com/74172467/202417392-d509f677-dbc3-4ba4-a62a-82192633f4ce.png)
### 그외 시도해본 방법
+ 눈 깜박임으로 인한 Delta, Theata변화량을 사용하는 것보다 raw_data의 노이즈를 활용하는 것이 효과적이었습니다.
+ 한쪽 눈만 감는 경우를 시도해보았지만 유의미한 차이를 확인할 수 없었습니다.

## analysis ✔
눈 깜박임 검출 뒤 서비스가 시작되면 10초 정도의 여유 이후 분석할 csv파일을 읽어옵니다.

## App ✔
flask를 실행합니다.
서버와 함수들을 연결해주는 역할을 합니다.

## preprocessing ✔
뇌파의 전처리에 필요한 함수들을 담아놨습니다.
- ICA 독립성분 분석

    ![image](https://user-images.githubusercontent.com/74172467/204206433-a46210a0-f69f-4e62-b0e9-3555eb9c5d0b.png)
    
    Sklearn의 FastICA를 사용하였습니다. S_는 구분된 신호를 재구조화 한 것이고 A_는 예상되는 혼동행렬입니다.

- FFT

    ![image](https://user-images.githubusercontent.com/74172467/204206925-dcd6c2dd-f466-4035-ad93-a5957b3b6028.png)
    
    Numpy에서 제공하는 FFT는 복소수 형태로 값을 반환해주기 때문에 양의 실수 값만 끊어서 사용하는 함수를 만들었습니다.

- Bandpath Filter

    ![image](https://user-images.githubusercontent.com/74172467/204207332-0a1be2f3-608e-4274-adab-060cf6a8019c.png)
    
    FFT 적용 후 해당 구역의 신호 값을 평균내어 반환한다. 

## Hz_potential ✔
Raw data와 분석이 시작하고 끝나는 Index값이 들어오면, 두 주파수의 평균 전위값, 증가한 전위가 큰 주파수 값을 비교하여 반환합니다.
    
## Index_cal ✔
Mave에서 시간 정보를 문자형으로 제공하기 때문에 시,분,초를 정수형으로 반환 함수입니다.
그리고 해당 시간이 Raw data에서 몇 번째 index인지 반환하는 함수도 담겨져 있습니다.

## Load_data ✔
Mave의 데이터를 실시간으로 읽어오는 함수입니다.

## SSVEP ✔
ssvep 데이터를 분석한 후 사용자의 의도를 파악할 수 있다.

-------------------------------------

# 성능평가✏

![image](https://user-images.githubusercontent.com/74172467/204210441-003db8a8-b8b7-498e-9117-99c1d5231cc4.png)


# 고찰✏

장점:
- Mave에서 제공하는 FFT는 평균 fps를 사용하지만 기기적 한계때문에 fps가 일정하지 않기 때문에 분석에 정확도가 낮아졌다. 이러한 한계점을 극복하기 위해 직접 index slicing을 통해 FFT를 진행하였기 때문에 보다 좊은 정확도를 기대할 수 있다.
- 자극 디자인이 성능에 중요한 영향을 끼쳤다. 자극 이미지의 패턴, 위치 등 디자인에 따라 뇌파의 변화량이 달라졌다. 더하여 SSVEP 자극 주파수가 낮은 대역일수록 값과 변화량이 예민하게 반응하여 불안정하였기에 충분히 높은 대역을 선택해야했다. 또한 적당히 변별력 있는 두 주파수를 고르는 것이 주요했다.

한계점:
- 본 프로젝트에서 사용된 기기는 MAVE이다. MAVE는 전전두염(Fp1, Fp2) 두 채널에서 비침습적 방법으로 뇌파를 수집한다. 시각 자극에 보다 큰 반응을 보이는 후두엽(O1,O2) 채널을 수집하는 기기를 사용했다면 더 높은 성능을 기대할 수 있다.
- 개인별로 SSVEP의 기준이 달랐다. 따라서 획일화된 명확한 임계값을 정하기 어려웠다. 더 높은 성능을 위해서 개인별 최적화 기능을 고려해볼 수 있다.

    
-------------------------------------------
    
# 팀원 소개✏

![image](https://user-images.githubusercontent.com/74172467/204210813-ace0029f-e6b1-419a-8946-001ad68ee9c3.png)
