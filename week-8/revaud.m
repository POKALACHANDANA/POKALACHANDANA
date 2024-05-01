inputfile='npy.wav'
outputfile='npy.wav'
[y,fs]=audioread(inputfile)
reversedata=flipup(y)
audiowrite(outputfile,reverseddata,fs)
disp('audio is revesed and succesfully saved')
