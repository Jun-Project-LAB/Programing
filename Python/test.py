#!/usr/bin/python

t_num = int(input())
s_num = 10000000
e_num = 99999999+1
rge = int((e_num-s_num)/t_num)

for a in range(1, t_num+1):
    print("Range is {} to {}".format(s_num+rge*(a-1), s_num+rge*a))
