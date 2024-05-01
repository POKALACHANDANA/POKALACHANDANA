inputfile='/home/rguktvalley/CL LAB/week-8/sample-file-1 (copy).wav'
outputfile='/home/rguktvalley/CL LAB/week-8/sample-file-1 (copy).wav'
[y,fs]=audioread(inputfile)
reversedata=flipup(y)
audiowrite(outputfile,reverseddata,fs)
disp('audio is revesed and succesfully saved')
