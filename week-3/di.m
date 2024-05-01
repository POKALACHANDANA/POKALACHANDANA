clc
clear all
close all
t=0:0.01:1
a=dictionary(['s1','s2','s3','s4','s5'],[[2,5],[5,10],[3,7],[10,12],[1,2]])
k=input("Enter sinusodal key to generate")
if a[k]
x=a[k][0]*sin(2*pi*sindict[k][1]*t)
plot(t,x)
