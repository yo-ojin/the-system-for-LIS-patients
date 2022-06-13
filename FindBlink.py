from scipy.signal import find_peaks


def find_blink(data):
    fs = 230

    x_new = data.loc[-5*fs:]

    peaks, _ = find_peaks(x_new, height=0.0002, distance=40)
    cnt = len(peaks)

    print(cnt)

    if cnt >= 7:
        # print(peaks[-1])
        # print(peaks)
        return peaks[-1]

    return 0
