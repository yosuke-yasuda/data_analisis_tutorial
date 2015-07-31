# -*- coding: utf-8 -*-
__author__ = 'ryoito'

from FileManager import FileManager
import nltk
from nltk import stem
from nltk.corpus import stopwords
import math
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy
from sklearn.cluster import KMeans
import sys
import cPickle as pickle
import random
from scipy.spatial.distance import jaccard

class PyKMeans:
    def __init__(self, class_num = 2, maxN = 10000):
        self.cnum = class_num #クラスタ数
        self.centroids = [{} for col in xrange(self.cnum)]
        self.maxN = maxN #最大イテレーション数

    #クラスタリング
    def clustering(self, data):
        labels = [random.randint(0, self.cnum - 1) for col in xrange(len(data))]
        prev_centroids = [{} for col in xrange(self.cnum)]
        count = 0
        while self.sum_cos(prev_centroids, self.centroids) > 0.01 and count < self.maxN:
            prev_centroids = [self.centroids[i][:] for i in xrange(len(self.cnum))]
            #E-STEP
            cls_count = [0] * self.cnum
            for idx in xrange(len(data)):
                bow = data[idx]
                label = labels[idx]
                for w in bow.keys():
                    cls_count[label] += 1
                    self.centroids[label].setdefault(w, 0)
                    self.centroids[label][w] += bow[w]
            for c in xrange(self.cnum):
                for w in self.centroids[c].keys():
                    self.centroids[c][w] /= cls_count[c]

            #M-STEP
            for idx in xrange(len(data)):
                bow = data[idx]
                max_c = 0 #一番似てるクラスタ
                max_sim = 0 #一番似ている時の類似度
                for c in xrange(self.cnum):
                    centroid = self.centroids[c]
                    sim = self.cos(bow, centroid)
                    if max_sim < sim:
                        max_c = c
                        max_sim = sim
                labels[idx] = c #一番似てるクラスタを採用
            count += 1
        return labels #ラベル群を返す

    #クラスタリング結果を使ってどのクラスタか判定
    def fit(self, bow):
        max_c = 0 #一番似てるクラスタ
        max_sim = 0 #一番似ている時の類似度
        for c in xrange(self.cnum):
            centroid = self.centroids[c]
            sim = self.cos(bow, centroid)
            if max_sim < sim:
                max_c = c
                max_sim = sim
        return max_c, max_sim

    def sum_cos(self, mtx1, mtx2):
        s = 0
        for idx in mtx1:
            s += self.cos(mtx1[idx],mtx2[idx])
        return s

    def cos(self, vec1, vec2):
        len1 = 0.
        len2 = 0.
        ip = 0.
        for v in vec1.values():
            len1 += v * v
        len1 = math.sqrt(len1)
        for v in vec2.values():
            len2 += v * v
        len2 = math.sqrt(len2)
        for k in vec1.keys():
            if vec2.has_key(k): ip += vec1[k] * vec2[k]
        if len1 == 0 or len2 == 0: return float("inf")
        return ip / len1 / len2


# タイトルとアブストラクトを結合させて、論文ID\tタイトル\tアブストラクトの文書を作る関数
def merge_doc(input_data):
    sys.stderr.write("文書の作成")
    attr = input_data[0]
    id_num = attr.index('_N')
    title_num = attr.index('TI')
    abst_num = attr.index('AB')
    doc = []
    for line in input_data[1:]:
        tmp = line[id_num] + '\t' + line[title_num] + '\t' + line[abst_num]
        doc.append(tmp)
    return doc

#論文IDとタイトルとアブストラクトを結合させた文章から辞書を作る
def make_id_text_dic(id_text):
    id_text_dict = {}
    for line in id_text:
        tmp = line.split('\t')
        id_text_dict[tmp[0]] = tmp[1]
    return id_text_dict

#形態素解析を行う関数
def morphological_analysis(text):
    tokens = []
    for sentence in nltk.sent_tokenize(text.lower()):
        tokens.extend(nltk.pos_tag(nltk.word_tokenize(sentence)))
    return tokens

#必要な品詞のみを抽出する関数
def subtract_words(array):
    out = []
    for line in array:
        if line[1][:2] == 'NN' or line[1][:2] == 'VB':
            out.append(line[0])
    return out

#ストップワードの処理
def stop_word(text):
    stopset = set(stopwords.words('english'))
    return [w for w in text if len(w) > 2 and w not in stopset]

#ステミングをする
def stemming(text):
    out = []
    stemmer = stem.PorterStemmer()
    for word in text:
        out.append(stemmer.stem(word))
    return out

#形態素解析をし、文字を小文字に変換した後に、ストップワード処理、ステミング処理を実行する関数
def pre_process(texts_dic):
    sys.stderr.write("形態素解析")
    processed_text_dic = {}
    keys = texts_dic.keys()
    for key in keys:
        text_mor = morphological_analysis(texts_dic[key])
        text_pro = subtract_words(text_mor)
        text_stop = stop_word(text_pro)
        text_stem = stemming(text_stop)
        processed_text_dic[key] = text_stem
    return processed_text_dic

#ユーニークな単語集合を作る
def make_unique_word(texts_dic):
    keys = texts_dic.keys()
    tmp = []
    for key in keys:
        tmp += texts_dic[key]
    return list(set(tmp))


#tfの計算をする関数
def calc_tf(text, unique_word):
    pre_unique = list(set(text))
    #低頻度語処理後の単語リストに載っていなければ、除外する
    unique = []
    for word in pre_unique:
        if word in unique_word:
            unique.append(word)
    tf_count_dict = {}
    for l in unique:
        tf_count_dict[l] = 0
    for word in text:
        if word in unique_word:
            tf_count_dict[word] += 1
    return tf_count_dict


#dfの計算をする関数
def calc_df(text_dict, unique_word):
    df_count_dict = {}
    keys = text_dict.keys()
    for l in unique_word:
        df_count_dict[l] = 0
    for word in unique_word:
        for key in keys:
            if word in text_dict[key]:
                df_count_dict[word] += 1
    return df_count_dict


#tf-idfの計算をする関数
def calc_tf_idf(text_dict, limit):
    sys.stderr.write("tf-idfの計算")
    pre_unique_word = make_unique_word(text_dict)
    unique_word = remove_low_words(text_dict, pre_unique_word, limit)  #低頻度処理を行う
    df_dict = calc_df(text_dict, unique_word)
    keys = text_dict.keys()
    tf_idf_dict = {}
    for key in keys:
        tf_store = calc_tf(text_dict[key], unique_word)
        tf_idf_store = {}
        key_word = tf_store.keys()
        for word in key_word:
            tf = tf_store[word] * 1.0 / len(text_dict[key])
            idf = math.log(len(keys) * 1.0 / df_dict[word])
            tf_idf_store[word] = tf * idf
        tf_idf_dict[key] = tf_idf_store
    return tf_idf_dict, unique_word


#低頻度語処理を行う
def remove_low_words(texts_dict, unique_word, limit):
    sys.stderr.write("低頻度語処理")
    df_dict = calc_df(texts_dict, unique_word)
    keys = df_dict.keys()
    new_unique_word = []
    for key in keys:
        if df_dict[key] > limit:
            new_unique_word.append(key)
    return new_unique_word

#コサイン類似度の計算
def cos_sim(a, b):
    numerator = numpy.dot(a, b)
    denominator = numpy.linalg.norm(a)*numpy.linalg.norm(b)
    if denominator != 0:
        return numerator/denominator
    else:  # 分母が0になる場合0を返す
        return 0

#文章のベクトル化
def vectorizer(tf_idf_dict, unique_word):
    keys = tf_idf_dict.keys()
    id_bow_dict = {}
    for key in keys:
        tmp_tf_idf_dict = tf_idf_dict[key]
        word_key = tmp_tf_idf_dict.keys()
        vector = [0] * len(unique_word)
        for word in word_key:
            location = unique_word.index(word)
            vector[location] = tmp_tf_idf_dict[word]
        id_bow_dict[key] = vector
    return id_bow_dict

#文章類似度のマトリックスを作成
def make_adj_matrix(input_dict, threshold):
    sys.stderr.write("文章類似度のマトリックスを作成")
    num = len(input_dict)
    counter = 0

    out_str = ""
    keys = input_dict.keys()
    for key_i in keys:
        if counter % 10 == 0:
            sys.stderr.write(str(round(counter*1.0/num*100, 1)) + "% 終了")
        store = {}  # 類似度を保存する
        for key_j in keys:
            if key_i != key_j:
                store[key_j] = cos_sim(input_dict[key_i], input_dict[key_j])
            else:
                store[key_j] = 1.0
        top_10 = sort_location(store, threshold)
        for id in top_10.keys():
            out_str += key_i + '\t' + id + '\t' + str(top_10[id]) + '\n'
        counter += 1
    return out_str

def sort_location(dict, threshold):
    locations = {}
    # しきい値が0なら類似度top10を、そうでなければその値を類似度のしきい値として用いる
    if threshold == 0:
        for k, v in sorted(dict.items(), key=lambda x:-x[1])[:0:10]:
            if v != 0:
                locations[k] = v
    else:
        for k, v in sorted(dict.items(), key=lambda x:x[1], reverse=True)[::1]:
            if v >= threshold:
                locations[k] = v
    return locations

def make_matrix(id_bow_dict):
    sys.stderr.write("Bow行列の作成")
    matrix = []
    keys = id_bow_dict.keys()
    for key in keys:
        matrix.append(id_bow_dict[key])
    return [matrix, keys]


#主成分分析による可視化
def pca(matrix):
    sys.stderr.write("主成分分析")
    pca = PCA(n_components=3)
    pca.fit(matrix)
    xyz = pca.transform(matrix)
    return xyz

#K-Means法によるクラスタリング
def kmeans(matrix, num):
    sys.stderr.write("K-Means法によるクラスタリング")
    kmeans_model = KMeans(n_clusters=num, random_state=10).fit(matrix)
    labels = kmeans_model.labels_
    return labels

#データの可視化
def show(data, label, fname):
    sys.stderr.write("データの可視化")
    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(len(data)):
        ax.scatter3D(data[i][0], data[i][1], data[i][2], 'o', color=color(label[i]), s=3)
    plt.savefig(fname+'.png')
    plt.show()

def color(num):
    if num == 0:
        return 'b'
    if num == 1:
        return 'g'
    if num == 2:
        return 'r'
    if num == 3:
        return 'c'
    if num == 4:
        return 'm'
    if num == 5:
        return 'y'
    if num == 6:
        return 'k'

def add_name(limit,threshold):
    if threshold == 0:
        return str(limit)
    else:
        return str(limit)+'_'+str(threshold)

#メイン関数の実行
if __name__ == '__main__':
    fm = FileManager()
    f = fm.readFile('mission.facet.2.tsv', '\t')
    limit = 1  # 低頻度後の閾値
    threshold = 0  # cos類似度のしきい値
    cluster_num = 6  # クラスタ数
    name = add_name(limit, threshold)

    texts = merge_doc(f)
    texts_dic = make_id_text_dic(texts)
    processd_text = pre_process(texts_dic)

    #tf-idfの計算
    tf_idf_dict, unique_word = calc_tf_idf(processd_text, limit)
    id_bow_dict = vectorizer(tf_idf_dict, unique_word)
    fm.oneOutFile(unique_word, 'word_'+name+'.txt')

    #隣接行列の作成
    adj_mat_str = make_adj_matrix(id_bow_dict, threshold)
    fm.strOutFile(adj_mat_str, 'sim_matrix_'+name+'.txt')  # テキストファイルに書き出す

    # PCAの前データを作成
    pre_bow_matrix = make_matrix(id_bow_dict)
    bow_matrix = pre_bow_matrix[0]
    ids = pre_bow_matrix[1]
    fm.twoOutFile(bow_matrix, 'bow_matrix_'+name+'.txt')  # テキストファイルに書き出す
    fm.oneOutFile(ids, 'ids_'+name+'.txt')  # テキストファイルに書き出す

    #K-Means法の実行と可視化
    pca_box_matrix = pca(bow_matrix)
    fm.twoOutFile(pca_box_matrix, 'pca_data_'+name+'.txt')
    label = kmeans(pca_box_matrix, cluster_num)
    fm.oneOutFile(label, 'label_'+name+'.txt')  # テキストファイルに書き出す
    show(pca_box_matrix, label, name)