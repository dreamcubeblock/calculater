from ReadAndCal import *
import random
import fractions
import argparse
def main():
    # 接收并处理命令行参数
    operate = getargs()  # 包含操作数和参数
    # 生成题目模式
    if operate.mode == 1:

        # 生成题目和答案
        qst = getqst(operate)
        ans = getans(qst)

        # 保存程序生成的题目和答案
        saveqst(qst)
        saveans(ans)
    # 改卷模式
    elif operate.mode == 2:

        qst = readqst(operate.qstpath)
        ans = readans(operate.anspath)
        cheackres = check(qst, ans)
        # 保存结果
        saveres(cheackres)


# 接收并处理命令行参数
def getargs():
    # 1.生成题目模式
    # 使用 -n 参数控制生成题目的个数
    # 使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围，该参数可以设置为1或其他自然数。该参数必须给定，否则程序报错并给出帮助信息。
    # 2.阅卷模式
    # 程序支持对给定的题目文件和答案文件，判定答案中的对错并进行数量统计，输入参数如下：
    # -e
    # -a
    # 例：Myapp.exe - e < exercisefile >.txt - a < answerfile >.txt
    parser = argparse.ArgumentParser(description='calculater')
    parser.add_argument('-n', dest='qstnumber', help='how much qst', default=10, type=int)
    parser.add_argument('-r', dest='maxnumber', help='range of number',default=10,type=int)
    parser.add_argument('-e', dest='qstpath', help='exercise file path',default=None,type=str)
    parser.add_argument('-a', dest='anspath', help='answer file path', default=None,type=str)
    parser.add_argument('-mode', dest='mode', help='answer file path', default=None,type=int)
    args = parser.parse_args()
    if args.qstnumber!=None or args.maxnumber!= None:
        assert args.qstnumber!=None and args.maxnumber!= None,"Error:生成题目模式缺少生成题目数量或者数字范围"
        args.mode=1
        return args
    elif args.qstpath!=None or args.anspath!= None:
        assert args.qstpath!=None,"Error:缺失题目文件路径"
        assert args.anspath!=None,"Error:缺少答案文件路径"
        args.mode=2
        return args
    else:
        assert False,"未输入命令行参数，无法运行"


# 生成题目
        
def getqst(args):
    symbol=['+','−','×','÷']
    number=args.qstnumber
    maxnumber=args.maxnumber
    list=[]
    for i in range(number):
        while True:
            mathnumber=random.randint(2,4)
            symbolnumber=mathnumber-1
            sym=[]
            words=[]
            qst=[]
            cum=0
            brackets=0
            if mathnumber==3:
                brackets=random.randint(0,1)
            elif mathnumber==4:
                brackets=random.randint(0,2)
            if brackets==1:
                cum=random.randint(1,mathnumber-1)
            for j in range(symbolnumber):
                k=random.randint(0,3)
                sym.append(symbol[k])
            for k in range(mathnumber):
                number_format=random.randint(1,2)
                if number_format==1:
                    num=random.randint(1,maxnumber-1)
                elif number_format==2:
                    up=random.randint(1,maxnumber-1)
                    down=random.randint(1,maxnumber-1)
                    if up<down:
                        num=str(up)+'/'+str(down)
                    elif up==down:
                        num=str(1)
                    else:
                        if up%down==0:
                            num=str(up/down)
                        else:
                            sname=up//down
                            last=up%down
                            num=str(sname)+"'"+str(fractions.Fraction(last,down))
                words.append(num)
            start=0
            if cum==1 or brackets==2:
                calculates="("+str(words[0])
                start=1
            else:
                calculates=words[0]
            for i in range(1,mathnumber):
                if brackets==2 and i==2:
                    calculates=str(calculates)+' '+str(sym[i-1])+"("+str(words[i])
                    start=1
                if start==1:
                    calculates=str(calculates)+' '+str(sym[i-1])+' '+str(words[i])+")"
                    start=0
                elif cum==i:
                    calculates="("+str(calculates)+' '+str(sym[i-1])+' '+str(words[i])
                    start=1
                elif cum==2 and i==1:
                    calculates=str(calculates)+' '+str(sym[i-1])+" ( "+str(words[i])
                    start=1
                elif cum==3 and i==2:
                    calculates=str(calculates)+' '+str(sym[i-1])+" ( "+str(words[i])
                    start=1
                else:
                
                    calculates=str(calculates)+' '+str(sym[i-1])+' '+str(words[i])
            calculates=calculates+" = "
            if cal(calculates)>=0:
                break

        list.append(calculates)
    return list


# 生成答案
def getans(qst):
    ans=[]
    for i,element in enumerate(qst):
        ans.append(cal(element))
    return ans


# 保存程序生成的题目
def saveqst(qst, savepath='Exercises.txt'):
    # 格式:
    # 1.四则运算题目1
    # 2.四则运算题目2
    # 其中真分数在输入输出时采用如下格式，真分数五分之三表示为3/5，真分数二又八分之三表示为2’3/8。
     with open(savepath,"a",encoding='utf-8') as f:
         for i in range(1,len(qst)+1):   
            #print(i)
            f.write(str(i)+". "+qst[i-1]+"\n")




# 保存程序生成的答案
def saveans(ans, savepath='Answers.txt'):
    # 格式:
    # 1.答案1
    # 2.答案2
    # 特别的，真分数的运算如下例所示：1/6 + 1/8 = 7/24。
     with open(savepath,"a") as f:
         for i in range(1,len(ans)+1):   
            f.write(str(i)+'. '+str(ans[i-1])+"\n")


if __name__ == '__main__':
    main()
