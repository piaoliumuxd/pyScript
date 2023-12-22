'''
Author: your name
Date: 2021-04-18 22:07:31
LastEditTime: 2023-05-21 11:54:11
LastEditors: piaoliumuxd 1442654512@qq.com
Description: In User Settings Edit
FilePath: \excelDataProc\myCode.py
'''
import pandas as pd 
import matplotlib.pyplot as plt
import glob
import os

from sqlalchemy import false

def drawCurves():
    # Load Excel data into a pandas dataframe
    df = pd.read_csv('./result/wine.csv')

    # Extract x and y values from the dataframe
    x = df['Serial number']
    y = df['fixed acidity']
    legend = df['type']

    # Plot the curve
    for i in legend.unique():
        plt.plot(x[legend==i], y[legend==i], label=i)
    plt.legend()
    # plt.show()
    plt.savefig('./result/output.png')
    df['image'] = './result/output.png'
    df.to_csv('./result/data_with_image.csv', index=False)

    return True

def fileMerged(df, pf):
    """
    知识点pandas如何向指定位置添加一列
    """
    df.insert(0, 'type', "red")    # 先在第一列插入列名
    # df['type'] = "red"  # 然后给这一列赋值

    pf.insert(0, 'type', "white")    
    # pf['type'] = "white"  

    df.to_csv('./result/winequality-red.csv', index=False)
    pf.to_csv('./result/winequality-white.csv',index=False)


    all_files = glob.glob(r'./result/*.csv')    # 遍历当前目录下的所有以.csv结尾的文件
    all_data_frame = []
    row_count = 0
    for file in all_files:
        data_frame = pd.read_csv(file)
        all_data_frame.append(data_frame)
        # axis=0纵向合并 axis=1横向合并
    data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=False, sort=False)
    data_frame_concat.to_csv("./result/wine.csv", index=False, encoding="utf-8")     # 将重组后的数据集重新写入一个文件

    

if __name__ == '__main__':
    
    df = pd.read_csv("winequality-red.csv", header = 0)
    pf = pd.read_csv("winequality-white.csv")

    # fileMerged(df, pf)
    drawCurves()


# '''
# TODO:
# 1、设置函数入参：文件所在路径、从第几行开始合并数据
# 2、保存的数据中多一行 Unnamed，如何去掉？
# '''