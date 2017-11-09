#灰色斜率关联度
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import math
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']                           #设置图中正常显示中文
#import seaborn as sns
#sns.set_style("darkgrid",{"font.sans-serif":['KaiTi', 'Arial']})    设置图例背景和网格线
#from matplotlib.font_manager import FontProperties
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)        动态设置字体

class GSCD(object):
    def readexcel(self,name,index):
        data_sheet = pd.read_excel(name,index_col=index)
        return data_sheet
    def cal_GSCD(self,data):
        num_of_rows = data.shape[0] #行数
        L_std=[]
        i_std=0
        while i_std < num_of_rows:
            L_std.append(data.ix[i_std].std(ddof=0))
            i_std = i_std + 1  #计算每一行标准差并存到列表L_std中
        #return L_std
        num_of_file = data.shape[1]  #列数
        #return num_of_file
        i_rows = 0 #行循环初始值
        L_slope = [] #存放斜率变量的列表
        while i_rows < num_of_rows:
            L_slope.append([])
            i_file = 1 #列循环初始值
            while i_file < num_of_file:
                slope = (data.iloc[i_rows,i_file]-data.iloc[i_rows,i_file-1])/L_std[i_rows]
                L_slope[i_rows].append(slope)
                i_file = i_file + 1
            i_rows = i_rows + 1
        #return L_slope
        i_coco = 1
        L_coco = []
        while i_coco < num_of_rows:
            L_coco.append([])
            L_cocofile = 0
            while L_cocofile < num_of_file -1:
                data_coco=1/(1+abs(L_slope[0][L_cocofile]-L_slope[i_coco][L_cocofile]))
                L_coco[i_coco-1].append(data_coco)
                L_cocofile = L_cocofile + 1
            i_coco = i_coco + 1  #将相关系数保存在列表中
        #return L_coco
        i_degree = 0
        L_degree=[]
        while i_degree < num_of_rows-1:
            num_degree = sum(L_coco[i_degree])/len(L_coco[i_degree])
            L_degree.append(num_degree)
            i_degree = i_degree + 1
        #return data.index
        #return L_degree
        #字典形式输出
        Dic_degree = {}
        i_dataframe = 1
        while i_dataframe < len(data.index):
            Dic_degree[data.index[i_dataframe]] = L_degree[i_dataframe-1]
            i_dataframe = i_dataframe +1
        return Dic_degree
    #排序
    def factor_sort(self,dic):
        return sorted(dic.items(),key=lambda item:item[1],reverse=True)
    #画图
    def line_chart(self,dataframe):
        ax = (dataframe.T).plot()
        plt.xlabel(u"年份")
        plt.ylabel(u"数值")
        plt.show()
