import time

import pandas as pd

from hz_potential import potential, what_u_see


def ssvep(idx, date):
    time.sleep(20)

    path = 'C:/MAVE_RawData/' + date + '/Rawdata.txt'
    raw = pd.read_csv(path, sep="\t", engine='python', encoding="cp949")

    fps = 210
    blink_index = int(idx)  # 아무값
    rest_start_index = blink_index + 10 * fps
    rest_end_index = rest_start_index + 20 * fps
    rest_7Hz, rest_13Hz = potential(raw, rest_start_index, rest_end_index)
    print("rest Hz")
    print(rest_7Hz, rest_13Hz)
    stimul_start_index = len(raw) - 20 * fps
    stimul_end_index = len(raw)
    print("자극 끝 순간")
    print(len(raw))
    sti_7Hz, sti_13Hz = potential(raw, stimul_start_index, stimul_end_index)
    print("stimul Hz")
    print(sti_7Hz, sti_13Hz)
    see = what_u_see(rest_7Hz, rest_13Hz, sti_7Hz, sti_13Hz)
    return [see, len(raw)]
