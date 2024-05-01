from scipy.io import wavfile
(fs,x)=wavfile.read('np.wav')
x_reverse=x[::-1]
wavfile.write('n.wave',fs,x_reverse)
