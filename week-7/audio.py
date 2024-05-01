import soundfile as sf
from matplotlib import pyplot as plt
#load audio file
file_path='-0\/home/rguktvalley/CL LAB/sample-file-1.wav'
signal,sample_rate=sf.read(file_path)

#calculate time array
duration=len(signal) /sample_rate
time=[i/sample_rate for i in range(len(signal))]

#plot the signal
plt.figure(figsize=(10,4))
plt.plot(time,signal)
plt.xlabel('time(s)')
plt.ylabel('amplitude')
plt.title('audio signal')
plt.grid(True)
plt.show()

