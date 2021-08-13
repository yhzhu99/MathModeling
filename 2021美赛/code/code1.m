i=imread('pic.jpg');
imshow(i);
[x0,y0] = ginput;
[x1,y1] = ginput;
x1= (x1-min(x0))*2/(max(x0)-min(x0))-1;
y1=(y1-max(y1))*3/(min(y0)-max(y0))+0.5;
plot(x1,y1,'.');                         
axis([-1,1.5,0,4]);
