from scipy.io import wavfile
(fs,x)=wavfile.read('/home/rguktvalley/CL LAB/week-8/sample-file-1.wav')
x_reverse=x[::-1]
wavfile.write('npy.wave',fs,x_reverse)
