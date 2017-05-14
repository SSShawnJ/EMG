import numpy as np
from scipy.signal import butter, lfilter, freqz
from matplotlib import pyplot as plt


###Filter API###
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
def butter_bandpass_filter(data, cutoffLow, cutoffHigh, fs, order=5):
    b, a = butter_bandpass(cutoffLow,cutoffHigh, fs, order=order)
    y = lfilter(b, a, data)
    return y






#####Private Functions######
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    #For digital filters, Wn is normalized from 0 to 1, where 1 is the Nyquist frequency,
    #pi radians/sample.(Wn is thus in half-cycles / sample.) 
    #For analog filters, Wn is an angular frequency (e.g. rad/s).
    b, a = butter(order, Wn=normal_cutoff, btype='lowpass', analog=False)
    return b, a

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    #For digital filters, Wn is normalized from 0 to 1, where 1 is the Nyquist frequency,
    #pi radians/sample.(Wn is thus in half-cycles / sample.) 
    #For analog filters, Wn is an angular frequency (e.g. rad/s).
    b, a = butter(order, Wn=normal_cutoff, btype='highpass', analog=False)
    return b, a

def butter_bandpass(cutoffLow,cutoffHigh, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoffLow = cutoffLow / nyq
    normal_cutoffHigh = cutoffHigh / nyq
    #For digital filters, Wn is normalized from 0 to 1, where 1 is the Nyquist frequency,
    #pi radians/sample.(Wn is thus in half-cycles / sample.) 
    #For analog filters, Wn is an angular frequency (e.g. rad/s).
    b, a = butter(order, Wn=[normal_cutoffLow,normal_cutoffHigh], btype='bandpass', analog=False)
    return b, a









################### Filter Testing########################
order = 5
fs = 20.0       # sample rate, Hz
cutoff = 5  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)  #w : ndarray. The normalized frequencies at which h was computed, in radians/sample.
plt.subplot(6, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Demonstrate the use of the filter.
# First make some data to be filtered.
T = 5.0             # seconds
n = int(T * fs)     # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) \
        + 0.5*np.sin(12.0*2*np.pi*t)

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)

plt.subplot(6, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()





b, a = butter_highpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)  #w : ndarray. The normalized frequencies at which h was computed, in radians/sample.
plt.subplot(6, 1, 3)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Highpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()



# Filter the data, and plot both the original and filtered signals.
y = butter_highpass_filter(data, cutoff, fs, order)

plt.subplot(6, 1, 4)
plt.plot(t, data, 'b-')
plt.plot(t, y, 'g-', linewidth=2)
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()


cutoffLow=5
cutoffHigh=7
b, a = butter_bandpass(cutoffLow,cutoffHigh, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)  #w : ndarray. The normalized frequencies at which h was computed, in radians/sample.
plt.subplot(6, 1, 5)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoffLow, 0.5*np.sqrt(2), 'ko')
plt.plot(cutoffHigh, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoffLow, color='k')
plt.axvline(cutoffHigh, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Bandpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()



# Filter the data, and plot both the original and filtered signals.
y = butter_bandpass_filter(data, cutoffLow,cutoffHigh, fs, order)

plt.subplot(6, 1, 6)
plt.plot(t, data, 'b-')
plt.plot(t, y, 'g-', linewidth=2)
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()


plt.subplots_adjust(hspace=0.4)
plt.show()