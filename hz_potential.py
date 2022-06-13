import preprocessing


def potential(raw, index_s, index_e):
    fs = (index_e - index_s) / 20
    raw_ = raw.loc[:, ['EEG_Fp1', 'EEG_Fp2']]

    pre = preprocessing.butter_bandpass_filter(raw_, 1, 30, fs)
    eeg = preprocessing.ica(pre, 2)
    eeg_n = eeg[1]

    fp1_ssvep = eeg_n[index_s:index_e, 0]  # 시작 시점 인덱스

    Hz11_fp1, Hz17_fp1 = preprocessing.analysis_ssvep(fp1_ssvep, fs, 11, 17)
    return Hz11_fp1, Hz17_fp1


def what_u_see(r_11, r_17, sti_11, sti_17):
    diff_11 = sti_11 - r_11
    diff_17 = sti_17 - r_17
    print('see')
    print(diff_11, diff_17)
    if diff_11 - diff_17 > 0:
        return 11  # 11변화가 더 크다
    else:
        return 17  # 17변화가 더 크다

#
# def potential_compare(raw,index_s, fs=250):
#     pre = preprocessing.butter_bandpass_filter(raw, 1, 30, fs)
#     eeg = preprocessing.ica(pre, 2)
#     eeg_n = eeg[1]
#     fp1_ssvep = eeg_n[index_s:, 0]  # 시작 시점 인덱스
#     Hz7_fp1, Hz13_fp1 = preprocessing.analysis_ssvep(fp1_ssvep, fs, 7, 13)
