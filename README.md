# data_analisis_tutorial
勉強会用レポジトリ

## 環境

### バージョン
python 2.7

### ライブラリ
* decorator==3.4.2
* funcsigs==0.4
* matplotlib==1.4.3
* mock==1.2.0
* networkx==1.9.1
* nose==1.3.7
* numpy==1.9.2
* pbr==1.3.0
* pyparsing==2.0.3
* python-dateutil==2.4.2
* python-louvain==0.4
* pytz==2015.4
* scipy==0.15.1
* six==1.9.0
* wsgiref==0.1.2
* [community ](https://bitbucket.org/taynaud/python-louvain)

### ライブラリインストール

```sh
$ pip install -r requirements.txt
```

communityは[こちら](https://bitbucket.org/taynaud/python-louvain)を参考に

### データ修正
```sh
$ cat data/selected_pairs.tsv| tr ',' '\t'  > data/_selected_pairs.tsv
$ mv data/_selected_pairs.tsv data/selected_pairs.tsv
```