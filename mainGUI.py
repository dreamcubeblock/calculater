import tkinter as tk
from tkinter.filedialog import *
from main import *
from ReadAndCal import *
import argparse


def funb1():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    root.geometry(size)

    f1 = tk.Frame(root)
    theLabel1 = tk.Label(f1, text='生成题目模式', font=('', 30), pady=20)
    theLabel2 = tk.Label(f1, text='*若文件已存在，问题和答案输出将覆盖已有内容', font=('', 10), pady=0)
    theLabel1.pack()
    theLabel2.pack()
    f1.pack(padx=10, pady=5)

    f2 = tk.Frame(root)
    qstnum = tk.IntVar()
    tk.Label(f2, text='请输入生成题目数(≥1的整数)', font=('', 13)).grid(row=0, column=0, padx=2, pady=5)
    tk.Entry(f2, state='normal')
    tk.Entry(f2, textvariable=qstnum, font=('', 13), bd=2, width=6).grid(row=0, column=1, padx=5, pady=5)
    ansnum = tk.IntVar()
    tk.Label(f2, text='请输入最大数值(>1的整数)', font=('', 13)).grid(row=1, column=0, padx=2, pady=5)
    tk.Entry(f2, textvariable=ansnum, font=('', 13), bd=2, width=6).grid(row=1, column=1, padx=5, pady=5)
    f2.pack(pady=5)

    def selectFile1():
        filepath = asksaveasfilename(defaultextension='.txt')  # 选择保存路径
        filenamesave1.set(filepath)  # 设置变量filename的值

    def selectFile2():
        filepath = asksaveasfilename(defaultextension='.txt')  # 选择保存路径
        filenamesave2.set(filepath)  # 设置变量filename的值

    f3 = tk.Frame(root)
    filenamesave1 = tk.StringVar()
    tk.Label(f3, text='题目保存路径', font=('', 15)).grid(row=1, column=0, padx=2, pady=5)
    tk.Entry(f3, textvariable=filenamesave1, font=('', 10, ), bd=3, width=48).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(f3, text=' ...', font=('', 10), command=selectFile1).grid(row=1, column=2, padx=0)


    filenamesave2 = tk.StringVar()
    tk.Label(f3, text='答案保存路径', font=('', 15)).grid(row=2, column=0, padx=2, pady=5)
    tk.Entry(f3, textvariable=filenamesave2, font=('', 10), bd=3, width=48).grid(row=2, column=1, padx=5, pady=5)
    tk.Button(f3, text=' ...', font=('', 10), command=selectFile2).grid(row=2, column=2, padx=0)
    f3.pack(pady=10)

    def breakfun():
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        frame1.pack(padx=10, pady=10)
        frame2.pack(padx=10, pady=20)
        frame3.pack(padx=10, pady=20)
    def okfun():
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        theLabel1 = tk.Label(root, text='生成题目和答案中...', font=('Arial', 30), pady=38)
        theLabel1.pack()

        def do():
            parser = argparse.ArgumentParser(description='calculater')
            args = parser.parse_args()
            args.qstnumber = qstnum.get()  # 问题数
            args.qstsavepath = filenamesave1.get()  # 问题存储路径
            args.maxnumber = ansnum.get()  # 最大数值
            args.anssavepath = filenamesave2.get()  # 答案存储路径

            # 生成题目和答案
            qst = getqst(args)
            ans = getans(qst)

            # 保存程序生成的题目和答案
            save(qst, args.qstsavepath)
            save(ans, args.anssavepath)
            return args
        args = do()
        theLabel1.pack_forget()
        fra1 = tk.Frame(root)
        fra2 = tk.Frame(root)
        tk.Label(fra1, text='生成成功！', font=('Arial', 30), pady=38).grid(row=1, column=0)
        tk.Label(fra1, text='题目保存路径：'+args.qstsavepath, font=('Arial', 15), pady=10).grid(row=2, column=0)
        tk.Label(fra1, text='答案保存路径：'+args.anssavepath, font=('Arial', 15), pady=10).grid(row=3, column=0)
        def breakfun1():
            fra1.pack_forget()
            fra2.pack_forget()
            frame1.pack(padx=10, pady=10)
            frame2.pack(padx=10, pady=20)
            frame3.pack(padx=10, pady=20)
        tk.Button(fra2, text='返回', font=('', 20), padx=10, pady=5, command=breakfun1).grid(row=4, column=0)
        fra1.pack()
        fra2.pack(pady=33)

    f4 = tk.Frame(root)
    tk.Button(f4, text='确定', font=('', 23), bd=4, command=okfun).grid(row=0, column=0, padx=80)
    tk.Button(f4, text='返回', font=('', 23), bd=4, command=breakfun).grid(row=0, column=1, padx=80)
    f4.pack(pady=20)

    root.mainloop()


def funb2():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

    root.geometry(size)

    f1 = tk.Frame(root)
    theLabel1 = tk.Label(f1, text='阅卷模式', font=('', 30), pady=25)
    theLabel2 = tk.Label(f1, text='*若文件已存在，阅卷结果将覆盖已有内容', font=('', 10), pady=0)
    theLabel1.pack()
    theLabel2.pack()
    f1.pack(padx=10, pady=5)

    def selectFile1():
        filepath = askopenfilename(defaultextension='.txt')  # 选择打开路径
        filenameopen.set(filepath)  # 设置变量filename的值

    def selectFile2():
        filepath = askopenfilename(defaultextension='.txt')  # 选择打开路径
        filenameopen2.set(filepath)  # 设置变量filename的值

    def selectFile3():
        filepath = asksaveasfilename(defaultextension='.txt')  # 选择打开路径
        filenameopen3.set(filepath)  # 设置变量filename的值

    f3 = tk.Frame(root)
    filenameopen = tk.StringVar()
    tk.Label(f3, text='题目文件路径', font=('', 18)).grid(row=1, column=0, padx=2, pady=5)
    tk.Entry(f3, textvariable=filenameopen, font=('', 10,), bd=3, width=48).grid(row=1, column=1, padx=5, pady=10)
    tk.Button(f3, text=' ...', font=('', 10), command=selectFile1).grid(row=1, column=2, padx=0)

    filenameopen2 = tk.StringVar()
    tk.Label(f3, text='答案文件路径', font=('', 18)).grid(row=2, column=0, padx=2, pady=5)
    tk.Entry(f3, textvariable=filenameopen2, font=('', 10), bd=3, width=48).grid(row=2, column=1, padx=5, pady=10)
    tk.Button(f3, text=' ...', font=('', 10), command=selectFile2).grid(row=2, column=2, padx=0)

    filenameopen3 = tk.StringVar()
    tk.Label(f3, text='阅卷结果保存路径', font=('', 15)).grid(row=3, column=0, padx=2, pady=5)
    tk.Entry(f3, textvariable=filenameopen3, font=('', 10), bd=3, width=48).grid(row=3, column=1, padx=5, pady=10)
    tk.Button(f3, text=' ...', font=('', 10), command=selectFile3).grid(row=3, column=2, padx=0)
    f3.pack(pady=18)

    def breakfun():
        f1.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        frame1.pack(padx=10, pady=10)
        frame2.pack(padx=10, pady=20)
        frame3.pack(padx=10, pady=20)
    def okfun():
        f1.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        theLabel1 = tk.Label(root, text='正在阅卷中...', font=('Arial', 30), pady=38)
        theLabel1.pack()

        parser = argparse.ArgumentParser(description='calculater')
        args = parser.parse_args()
        args.qstpath = filenameopen.get()  # 问题数
        args.anspath = filenameopen2.get()  # 问题存储路径

        qst = readfile(args.qstpath)
        ans = readfile(args.anspath)
        cheackres = check(qst, ans)

        # 保存阅卷结果
        saveres(cheackres, filenameopen3.get())

        theLabel1.pack_forget()
        fra1 = tk.Frame(root)
        fra2 = tk.Frame(root)
        fra3 = tk.Frame(root)
        tk.Label(fra1, text='阅卷完成！', font=('Arial', 30), pady=30).grid(row=1, column=0)
        tk.Label(fra3, text='正确：' + str(len(cheackres[0])), font=('Arial', 30), pady=10, padx=40).grid(row=3, column=0)
        tk.Label(fra3, text='错误：' + str(len(cheackres[1])), font=('Arial', 30), pady=10, padx=40).grid(row=3, column=1)
        tk.Label(fra1, text='阅卷结果保存路径：' + filenameopen3.get(), font=('Arial', 15), pady=10).grid(row=2, column=0)
        tk.Label(fra1, text='*具体结果请打开文件查看', font=('Arial', 10), pady=5).grid(row=3, column=0)
        def breakfun2():
            fra1.pack_forget()
            fra2.pack_forget()
            fra3.pack_forget()
            frame1.pack(padx=10, pady=10)
            frame2.pack(padx=10, pady=20)
            frame3.pack(padx=10, pady=20)
        tk.Button(fra2, text='返回', font=('', 20), padx=10, pady=5, command=breakfun2).grid(row=4, column=0)
        fra1.pack()
        fra3.pack()
        fra2.pack(pady=33)

    f4 = tk.Frame(root)
    tk.Button(f4, text='确定', font=('', 23), bd=4, command=okfun).grid(row=0, column=0, padx=80)
    tk.Button(f4, text='返回', font=('', 23), bd=4, command=breakfun).grid(row=0, column=1, padx=80)
    f4.pack(pady=10)
# ------------------------------------------------------------------------------------
root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

root.title('生成四则运算题目及阅卷')

# 窗口居中显示
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
if screenwidth>=1920 and screenheight>=1080:
    width, height = 712*screenwidth/1920, 380*screenheight/1080
else:
    width, height = 712, 380
size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size)

theLabel = tk.Label(frame1, text='请选择程序模式', font=('Arial', 30), pady=38)
theLabel.pack()

b1 = tk.Button(frame2, text='生成题目模式', font=('', 20), padx=10, pady=5, command=funb1)
b2 = tk.Button(frame2, text='阅卷模式', font=('', 20), padx=10, pady=5, command=funb2)
b3 = tk.Button(frame3, text='退出程序', font=('', 20), padx=10, pady=5, bd=4,command=root.destroy)
b3.grid(column=0, row=0, padx=50)
b1.grid(column=0, row=0, padx=50)
b2.grid(column=1, row=0, padx=50)

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=20)
frame3.pack(padx=10, pady=20)


root.mainloop()
