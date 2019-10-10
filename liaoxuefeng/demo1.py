#!/usr/bin/env python
#encoding=UTF-8

h=input('请输入身高(cm）：')
w=input('请输入体重（KG）：')
height=float(h)
weight=float(w)
bmi = weight/((height/100)**2)

if bmi<18.5:
  print ('过轻')
elif (bmi >=18.5) and (bmi<25):
  print ('正常')
elif (bmi >=25) & (bmi<28):
  print ('过重')
elif (bmi >=28) and (bmi<32):
  print ('肥胖')
elif bmi >=32:
  print ('过重')
else:
  print ('无法判断')
print (bmi)