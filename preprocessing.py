import numpy as np
import numpy.fft as fft
from scipy.signal import butter, lfilter
from sklearn.decomposition import FastICA


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def ica(evoked, n_components=2):
    fast_ica = FastICA(n_components=n_components)
    S_ = fast_ica.fit_transform(np.transpose(evoked))
    A_ = fast_ica.mixing_
    return np.transpose(S_), A_


def calculate_fft(signal):
    frequency = np.array(fft.fft(signal))
    ps = ((frequency.real * frequency.real) + (frequency.imag * frequency.imag)) / (len(frequency) * len(frequency)) * 2
    ps = ps[:int(len(ps) / 2)]
    return ps


def extract_band_power(eeg, df, lowcut, highcut):
    # FFT
    ps = calculate_fft(eeg)
    # Extract band spectrum
    band_ps = ps[int(lowcut / df):int(highcut / df)]
    # Calculate band power
    band_power = np.average(band_ps)

    return band_power


def calculate_df(fs, length):
    return fs / length


def analysis_ssvep(eeg, fs, Hz_1, Hz_2):
    df = calculate_df(fs, len(eeg))
    Hz11 = extract_band_power(eeg, df, Hz_1 - 0.5, Hz_1 + 0.5)
    Hz17 = extract_band_power(eeg, df, Hz_2 - 0.5, Hz_2 + 0.5)
    return Hz11, Hz17
