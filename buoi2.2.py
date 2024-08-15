# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:21:58 2024

@author: nguyenthikieutrang
"""
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập hệ số b:"))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm")
else:
    x= -b / a
    print("Nghiệm của phương trình là x =", x)
import math
print("Giải phương trình bậc 2")
a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
c = float(input("Nhập hệ số c"))
if (a == 0):
    if (b == 0):
        print("Phương trình vô nghiệm!");