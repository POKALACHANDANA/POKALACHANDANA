clc
clear all
close all
t=0:0.01:1
si={'s1',[2,5];'s2',[5,10];'s3',[3,7];'s4',[10,12];'s5',[1,2];}
k=str(input("Enter the key"))
figure;
hold on;
for i=1:length(si)
  l=si.k
  f=l(1)
  amp=l(0)
  wave=amp*sin(2*pi*f*t)
  plot(t,wave)
  xlabel('time(s)')
  ylabel('amplitude')
  title('sine wave')
  legend
  plt.show()
endfor
hold off;
