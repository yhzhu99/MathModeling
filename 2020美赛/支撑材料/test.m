close all; clear all; clc
data=xlsread('1.xlsx',1);
x=1:1:1800;
y=polyfit(x,data,1)
plot(x,data,'linestyle','none','marker','.','markersize',5)