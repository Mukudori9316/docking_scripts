import sys, os, datetime
import numpy as np
import matplotlib.pyplot as plt


def search_dlg(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.split('.')[1] == "dlg":
                file_list.append(root+'\\'+f)
    return(file_list)


def get_score(path):
    datas, scores, elist, kilist = [], [], [], []
    f = open(path)
    for line in f:
        if line[:5] == "MODEL" or line[:4] == "USER":
            datas.append(line.split())
    for data in datas:
        if len(data) >2 and data[2] =='Free':
            elist.append(data[7])
        elif len(data) >2 and data[2] =='Inhibition':
            k = float(data[6])
            if data[7] == 'mM':
                fk = k*1000000
            elif data[7] == 'uM':
                fk = k*1000
            else: fk = k
            kilist.append(fk)
    for e, ki in zip(elist, kilist):
        scores = np.array([e, ki], dtype=float)
    results = [path, scores]
    f.close()
    return(results)


def logdata(direc):
    scores, Y1, Y2, label = [], [], [], []
    log = ''
    today = datetime.datetime.today()
    dstr = today.strftime('%Y%m%d')
    for path in search_dlg(direc):
        scores.append(get_score(path))
    for i in scores:
        name = i[0].split('\\')[3]+':'+i[0].split('\\')[4]
        ZB = i[0].split('\\')[4][2:]
        score = i[1]
        if len(score) == 0:
            score = np.array([0,0])
        Y1.append(score[0])
        Y2.append(score[1])
        label.append(ZB)
        log += (name+str(score)+'\n')
    print(log)
    logn = dstr+'_result.txt'
    f = open(direc+'\\'+logn, 'w')
    f.write(log)
    f.close()

    Y1 = np.array(Y1)
    fig, ax1 = plt.subplots()
    X = np.arange(len(Y1))
    p1 = ax1.bar(X, Y1*(-1), color='b',width=0.4, label='-energy', align="center")
    plt.xticks(X+0.2, label)

    ax2 = ax1.twinx()
    p2 = ax2.bar(X+0.4, np.log10(Y2), color='g',width=0.4, label='Ki', align="center")
    p = [p1,p2]
    ax1.legend(p,[i.get_label() for i in p])
    plt.show()


logdata("C:\AutoDock\\170518")
