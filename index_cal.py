def time_str_to_int(time_):  # 글로 된 시간이 들어오면 그때 인덱스를 반환 해줘
    r = time_.split(":")
    minute = int(r[1])
    second = int(r[-1].split(".")[0])
    sec = minute * 60 + second
    return sec


def int_to_index(raw_time, moment):  # 해당 초에 시작하는 인덱스를 알려줘
    for i in range(len(raw_time)):
        r = time_str_to_int(raw_time[i])
        if (moment == r):
            return i
