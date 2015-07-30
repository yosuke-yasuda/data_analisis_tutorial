import pickle
import numpy as np
from make_network_data import make_matrix_from_tsv_file
from scipy.spatial import distance

__author__ = 'yasudayousuke'

import unittest
import csv

def import_bow_data():
    id_bow = {}
    filename = "data/selected_pairs.tsv"
    id_num_map_file_name = filename + ".id_num_map.pickle"
    try:
        with open(id_num_map_file_name, mode='rb') as f:
            id_num_map = pickle.load(f)
    except Exception as e:
        print(e.message)
        id_num_map = make_matrix_from_tsv_file(filename)[0]
        with open(id_num_map_file_name, mode='wb') as f:
            pickle.dump(id_num_map, f)
    with open("data/id_bow_matrix.txt", 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        vocab = []
        for field in reader.next():
            if field != "id":
                vocab.append(field)
        for row in reader:
            try:
                id_bow[id_num_map[row[0]]] = np.array([float(data) for data in row[1:]])
            except Exception as e:
                print row[0]
    return vocab, id_bow

def import_facet():
    filename = "data/mission.facet.2.tsv"
    id_title = {}
    csv.field_size_limit(1000000000)
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for dict in reader:
            id_title[dict["_N"]] = dict["TI"]
    return id_title

def calc_centroid(index_list, id_bow_dict):
    bow_sum = np.array([0.] * len(id_bow_dict.values()[0]))
    count = 0
    for paper_index in index_list:
        try:
            bow_sum += id_bow_dict[paper_index]
            count += 1
        except Exception as e:
            pass
    return count, bow_sum / float(count)

class MyTestCase(unittest.TestCase):
    def test_import_bow_data(self):
        vocab, id_bow = import_bow_data()
        self.assertEqual(type(id_bow), dict)
        self.assertEqual(type(vocab), list)

    def test_calc_centroids(self):
        vocab, id_bow = import_bow_data()
        centroid = calc_centroid([39284, 115550], id_bow)
        self.assertEqual(len(centroid), len(vocab))


if __name__ == '__main__':
    filename = "data/selected_pairs.tsv"
    partition_file_name = filename+".partition.pickle"
    vocab, id_bow = import_bow_data()
    id_num_map_file_name = filename + ".id_num_map.pickle"
    id_title = import_facet()
    with open(id_num_map_file_name, mode='rb') as f:
        id_num_map = pickle.load(f)
        num_id_map = {v: k for k, v in id_num_map.items()}
    with open(partition_file_name, mode='rb') as f:
        partition = pickle.load(f)
    bincount = np.bincount(partition.values())
    for index in np.argsort(-bincount):
        papers = [key for key, value in partition.items() if value == index]
        count, centroid = calc_centroid(papers, id_bow)
        print "### community%s count%s(%0.1f%%)" % (index, count, count*100/float(len(partition.values())))
        print "---\n"
        for vocab_index in np.argsort(-centroid)[:20]:
            print "* %s:%s" % (vocab[vocab_index], centroid[vocab_index])
        print "---\n"
        distances = [distance.euclidean(centroid, id_bow[paper]) for paper in papers]
        for dist_index in np.argsort(distances)[:10]:
            paper_index = papers[dist_index]
            print "* %s:%s" % (id_title[num_id_map[paper_index]], distance.euclidean(centroid, id_bow[paper_index]))
    #unittest.main()
