# -*- coding: utf-8 -*-
"""Task 1d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e2USepnA0idqMNTQ5U5oj8cgU5R1Mbu-
"""

def powerN(base,n):
    if base==1:
        return 1
    elif base==0:
        return 0
    if n==0:
        return 1
    else:
        return base*powerN(base,n-1)
powerN(3,3)