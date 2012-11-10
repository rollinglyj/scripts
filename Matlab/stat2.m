function test
y=randn(100,1);
[mean,stdev] = stat(y)

function [mean,stdev] = stat(x) 
n = length(x); 
mean = sum(x)/n; 
stdev = sqrt(sum((x-mean).^2/n)); 
