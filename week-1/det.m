clc
clear all
close all
A=[1,2;3,4]
det=A(1,1).*A(2,2)-A(1,2).*A(2,1)
disp(['determinant of the 2X2 matrix:',num2str(det)])