#Hiển thị ra màn hình các số nguyên tố trong đoạn từ a đến b. (Với a <= b, a,b là số nguyên tố)
import math
try:
    num = int(input("Nhập vào một số bất kì: "))
    if num <= 1:
        print(f'{num} không phải là số nguyên tố')
    else:
        for i in range(2,num):
            if num % i == 0:
                print(f'{num} không phải là số nguyên tố')
                break
        else:
            print(f'{num} là số nguyên tố')
except:
    print("Định dạng đầu vào không hợp lệ")
