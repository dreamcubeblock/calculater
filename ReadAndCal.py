import re


# 从文件中获取题目
def readqst(qstpath):
    qst_list = []

    with open(qstpath, 'r', encoding='utf-8') as f:
        qst = f.readlines()

    # 去除题号
    for eachline in qst:
        line = eachline.split('. ')[-1]
        line = line.strip('\n')
        qst_list.append(line)

    return qst_list


# 从文件中获取答案
def readans(anspath):
    ans_list = []

    with open(anspath, 'r', encoding='utf-8') as f:
        ans = f.readlines()

    # 去除题号
    for eachline in ans:
        line = eachline.split('. ')[-1]
        line = line.strip('\n')
        ans_list.append(line)

    return ans_list


# 改卷
def check(qst_list, ans_list):
    correct_list = []
    wrong_list = []
    for each in range(len(qst_list)):
        if cal(qst_list[each]) == cal(ans_list[each]):
            correct_list.append(each+1)
        else:
            wrong_list.append(each+1)
    return [correct_list, wrong_list]


# 传入算式字符串，返回结果
def cal(formula):
    # 去除带分数
    print(formula)
    formula=formula.replace('×','*').replace('÷','/').replace('−','-').replace("\n", "").replace("\r", "").replace("=", "")
    mix = re.findall(r"\d+\'\d+/\d+", formula)
    mix1 = []
    for each in range(len(mix)):
        mix1.append('(' + mix[each].replace('\'', '+') + ')')
        formula = formula.replace(mix[each], mix1[each])
    cal_res = round(eval(formula), 5)
    return cal_res


# 保存阅卷结果到文件
def saveres(res, savepath='Grade.txt'):
    # 输出格式：
    # Correct: 5 (1, 3, 5, 7, 9)
    # Wrong: 5 (2, 4, 6, 8, 10)
    cor = 'Correct: ' + str(len(res[0]))
    if len(res[0]) != 0:
        cor += ' ('
        for each in res[0]:
            cor += str(each)
            cor += ', '
        if cor[-2:] == ', ':
            cor = cor[:-2]
        cor += ')'

    wro = 'Wrong: ' + str(len(res[1]))
    if len(res[1]) != 0:
        wro += ' ('
        for each in res[1]:
            wro += str(each)
            wro += ', '
        if wro[-2:] == ', ':
            wro = wro[:-2]
        wro += ')'

    with open(savepath, 'w', encoding='utf-8') as f:
        f.write(cor+'\n'+wro)


if __name__ == '__main__':
    qst_list = readqst('ExercisesDemo.txt')
    ans_list = readans('AnswersDemo.txt')
    res = check(qst_list, ans_list)
    saveres(res)
