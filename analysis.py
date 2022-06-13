import datetime as dt
import time

import pandas as pd

import FindBlink
import load_data


def analysis():
    print('함수 실행')
    # 파일 실시간으로 받아오기
    now = dt.datetime.now()
    t_date = load_data.creat_Path(now)

    path_raw = 'C:/MAVE_RawData/' + t_date + '/Rawdata.txt'  # 파일 경로

    while 1:
        temp = pd.read_csv(path_raw, delimiter='\t', encoding='cp949')

        data = temp.loc[:, 'EEG_Fp1']

        result = FindBlink.find_blink(data)
        if result != 0:
            return [result, t_date]

    # 눈깜박임 감지 알려주기!-> 휴식 화면 ㄱㄱ
    # 30초동안
    time.sleep(10)
    while 1:
        raw = pd.read_csv(path_raw, sep="\t", engine='python', encoding="cp949")
