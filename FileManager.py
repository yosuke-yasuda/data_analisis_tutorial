# -*- coding: utf-8 -*-
__author__ = 'ryoito'

class FileManager:
    def readFile(self, fName, pattern):
        print fName + "の読み込み開始"
        f = open(fName)
        lines = f.readlines()
        f.close()
        store = []
        for line in lines:
            line = line[:-1].split(pattern)
            store.append(line)
        return store

    def readLineFile(self, fName):
        print fName + "の読み込み開始"
        f = open(fName)
        lines = f.readlines()
        f.close()
        return lines

    def readFilePair(self, fName, pattern):
        print fName + "の読み込み開始"
        f = open(fName)
        lines = f.readlines()
        f.close()
        store = []
        for line in lines:
            line = line.split(pattern)
            store.append(line)
        return store

    #二次元配列をタブ区切りで書き出す
    def twoOutFile(self, array, fName):
        print fName + "の書き出し開始"
        s = ""
        for i in range(len(array)):
            for j in range(len(array[i])-1):
                if isinstance(array[i][j], float) or isinstance(array[i][j], int):
                    s += str(array[i][j]) + "\t"
                else:
                    s += array[i][j] + "\t"
            if isinstance(array[i][j], float) or isinstance(array[i][j], int):
                s += str(array[i][len(array[i])-1]) + "\n"
            else:
                s += array[i][len(array[i])-1] + "\n"
        f = open(fName, "w")
        f.write(s)
        f.close()

    #一次元配列をタブ区切りで書き出す
    def strOutFile(self, s, fName):
        print fName + "の書き出し開始"
        f = open(fName, "w")
        f.write(s)
        f.close()

    #一次元配列をタブ区切りで書き出す
    def oneOutFile(self, array, fName):
        print fName + "の書き出し開始"
        s = ""
        for i in range(len(array)-1):
            s += str(array[i]) + "\t"
        s += str(array[len(array)-1])+"\n"
        f = open(fName, "w")
        f.write(s)
        f.close()

    #一次元配列をタブ区切りで書き出す
    def oneOutDictFile(self, dict, fName):
        print fName + "の書き出し開始"
        array = sorted(dict.items())
        s = ""
        for i in range(len(array)-1):
            s += str(array[i][0])+":"+str(array[i][1])+"\t"
        s += str(array[len(array)-1][0])+":"+str(array[len(array)-1][1])
        f = open(fName, "w")
        f.write(s)
        f.close()
