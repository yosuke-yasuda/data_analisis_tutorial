import pickle
import numpy as np
import networkx as nx
import community as co
import random
from scipy.sparse import lil_matrix
import matplotlib.pyplot as plt
import csv


__author__ = 'yasudayousuke'

import unittest

def make_matrix_from_tsv_file(file_name):
    csv.field_size_limit(1000000000)
    tsvfile = open(file_name, 'rb')
    tsvreader = csv.reader(tsvfile, delimiter='\t')
    id_num_map = {}
    path_list = []
    count = 0
    for row in tsvreader:
        if row[0] not in id_num_map.keys():
            id_num_map[row[0]] = count
            count += 1
        if row[1] not in id_num_map.keys():
            id_num_map[row[1]] = count
            count += 1

        path_list.append((id_num_map[row[0]], id_num_map[row[1]]))

    matrix = lil_matrix((count, count), dtype=int)
    for path_pair in path_list:
        matrix[path_pair[0], path_pair[1]] = 1
    return id_num_map, matrix

def partition_graph(G):
    return co.best_partition(G)

def draw_spring_layout(G, partition):
    pos = nx.spring_layout(G)
    random.seed(0)
    for index, com in enumerate(set(partition.values())):
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=5, linewidths=0,
                               node_color='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    nx.draw_networkx_edges(G, pos, alpha=0.5, width=0.1)
    plt.savefig("image/output_graph.png")

class MyTestCase(unittest.TestCase):
    def test_make_matrix_from_tsv_file(self):
        result_map, result_matrix = make_matrix_from_tsv_file("data/30_sample_pairs.tsv")

    def test_partition_graph(self):
        result = partition_graph(nx.from_scipy_sparse_matrix(make_matrix_from_tsv_file("data/30_sample_pairs.tsv")[1]))
        self.assertEqual(type(result), dict)

if __name__ == '__main__':
    #unittest.main()
    filename = "data/mission.pairs.tsv"
    graph_file_name = filename+".graph.pickle"
    partition_file_name = filename+".partition.pickle"
    try:
        with open(graph_file_name, mode='rb') as f:
            G = pickle.load(f)
    except Exception as e:
        print(e.message)
        G = nx.from_scipy_sparse_matrix(make_matrix_from_tsv_file(filename)[1])
        with open(graph_file_name, mode='wb') as f:
            pickle.dump(G, f)
    try:
        with open(partition_file_name, mode='rb') as f:
            partition = pickle.load(f)
    except Exception as e:
        partition = partition_graph(G)
        with open(partition_file_name, mode='wb') as f:
            pickle.dump(partition, f)
    draw_spring_layout(G, partition)
