# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:56:13 2024

@author: nguyenthikieutrang
"""
a=float(input("Nhap so km:"))
so_tien_la=0
if a <=1:
    so_tien_la = 20000
elif a<=3:
    so_tien_la = (a-1)*13000
elif a<=8:
    so_tien_la = 3*13000+(a-3)*12000
else:
    so_tien_la = 3*13000+(a-3)*12000+(a - 8)*10000
    if so_tien_la > 100000:
        so_tien_la =(3*13000+(a-3)*12000+(a - 8)*10000)*0.92
print("Tong tien: ", int(so_tien_la))