from __future__ import division
import  math
"prvi pravac"
a=17
b=55
c=32
"drugi pravac"
i=68
j=15
k=46

prvi= a+b/60+c/3600
drugi= i+j/60+k/3600
ugao= drugi-prvi
print('ugao je:', int(ugao//1) ,"stepeni", int((ugao%1)*60)//1 ,"minuta " , int((((ugao%1)*60)%1)*60) ,"sekundi")