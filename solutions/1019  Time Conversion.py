#1019 - Time Conversion

N = int(input())

h = N//3600
m = (N %3600)//60
s = (N%3600) %60

print('{}:''{}:''{}'.format(h,m,s))