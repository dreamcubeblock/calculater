import re
import fractions


# 读取文件
def readfile(qstpath):
    file_list = []
    with open(qstpath, 'r', encoding='utf-8') as f:
        file = f.readlines()
    # 去除题号
    for eachline in file:
        line = eachline.split('.')[-1]
        line = line.strip('\n')
        file_list.append(line)
    return file_list


# 改卷
def check(q_list, a_list):
    correct_list = []
    wrong_list = []

    for each in range(len(q_list)):
        if cal(q_list[each]) == cal(a_list[each]):
            correct_list.append(each+1)
        else:
            wrong_list.append(each+1)

    return [correct_list, wrong_list]


# 传入算式字符串，返回结果
def cal(formula):

    # 去除空格和等号，规范算式
    formula=formula.replace('×','*').replace('÷','/').replace('−','-').replace("\n", "").replace("\r", "").replace("=", "").replace(" ","")

    # 去除带分数
    mix = re.findall(r"\d+\'\d+/\d+", formula)
    mix_list = []
    for each in range(len(mix)):
        mix_list.append('(' + mix[each].replace('\'', '+') + ')')
        formula = formula.replace(mix[each], mix_list[each])

    # 去除除号变为分数
    finddiv = re.findall(r"\d+/\d+", formula)
    alldiv = []

    def myfun(matched):
        value = matched.group('value')
        return 'fractions.Fraction(' + value + ',1)'
    formula = re.sub(r'(?P<value>\d+)', myfun, formula)

    # 将所有除法和分数替换为fractions.Fraction对象，目的是计算过程和结果保留分数
    loc = locals()
    exec("res = " + formula)
    cal_res = loc['res']

    return cal_res


# 保存阅卷结果到文件
def saveres(res_list, savepath='Grade.txt'):
    # 规范输出格式
    def output(outres):
        retstr = ''
        if len(outres) != 0:
            retstr += ' ('
            for each in outres:
                retstr += str(each)
                retstr += ', '
            if retstr[-2:] == ', ':
                retstr = retstr[:-2]
            retstr += ')'
        return retstr

    cor = 'Correct: ' + str(len(res_list[0])) + output(res_list[0])
    wro = 'Wrong: ' + str(len(res_list[1])) + output(res_list[1])

    with open(savepath, 'w', encoding='utf-8') as f:
        f.write(cor+'\n'+wro)


if __name__ == '__main__':
    qst_list = readfile('Exercises.txt')
    ans_list = readfile('Answers.txt')
    res = check(qst_list, ans_list)
    saveres(res)
