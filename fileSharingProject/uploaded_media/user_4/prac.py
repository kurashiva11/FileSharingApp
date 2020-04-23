# import threading

# def foo():
#     print("in foo.")

# class alarm:
#     count = 0
#     def __init__(self, Time):
#         print("new object")
#         Timer = threading.Timer(Time, self.show)
#         print(Timer)
#         self.Timer = Timer
#         Timer.start()
#         alarm.count+=1
#         self.count = alarm.count

#     def show(self):
#         #print("Timer object : ", self.Timer, "count : ", self.count)
#         temp = str(self.Timer)
#         print(temp, type(temp))
#         tmp = threading.Timer(temp)
#         print(tmp, type(tmp))
        
#     def cancel(self):
#         print("Timer cancelling : ", self.Timer)
#         self.Timer.cancel()

#     def __str__(self):
#         return str(self.Timer)

# n = int( input("enter number of Timer you want : ") )
# for i in range(n):
#     time = int( input("enter time (sec): ") )
#     alarm(i*2)

# a = [1, 2]
# a += [3, 4]
# print(a)


# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# ind = 0

# for i in range(len(s)):
#     for j in range(i, len(s)):
#         for k in range(j, len(s)):
#             for l in range(k, len(s)):
#                 for m in range(l, len(s)):
#                     for n in range(m, len(s)):
#                         for o in range(n, len(s)):
#                             print(ind, ":", s[i]+s[j]+s[k]+s[l]+s[m]+s[n]+s[o])
#                             ind+=1
import os, sys

# print("this is before cleared")
# tmp = os.system("cls")
# print("compiling code.")

# if not os.system("g++ test.cpp -o test"):
#     print("compiled successfully and running program.")
#     os.system("test")
# else:
#     print("some error occured")

os.system("cls")

folder_name = input("enter folder name: ")

# print(os.listdir())
if folder_name not in os.listdir():
    os.mkdir(folder_name)


while True:
    op = int(input("\n\nenter options\n1.run a file\n2.create a file\n3.list files\n9.stop execution\n\n=> :"))

    if op==1:
        file_name = input("enter file name to run: ")
        print("compiling file")
        if not os.system(f"cd {folder_name} && g++ {file_name} -o {file_name.split('.')[0]}"):
            print("compilation successful. and running file\n\n\n")
            os.system(f"cd {folder_name} && {file_name.split('.')[0]}")
            print("\n\n")
        else:
            print("compilation error.")

    elif op==2:
        file_name = input("enter file name with extention: ")

        with open(folder_name+'/'+file_name, "w") as fp:
            print("created file", file_name, " in", folder_name)

    elif op==3:
        os.system(f"cd {folder_name} && dir")

    elif op == 9:
        break
