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

### データをセット

`data/`以下に、`mission.facet.2.tsv`、`mission.pairs.tsv`、`selected_pairs.tsv`を入れる

### データ修正
`tsv`が`,`区切りになっているので、ファイルを修正
```sh
$ cat data/selected_pairs.tsv| tr ',' '\t'  > data/_selected_pairs.tsv
$ mv data/_selected_pairs.tsv data/selected_pairs.tsv
```


## 描画結果

### selected_pairs
![結果](https://raw.githubusercontent.com/double-y/data_analisis_tutorial/master/image/result_graph.png)

### mission.pairs
![結果](https://raw.githubusercontent.com/double-y/data_analisis_tutorial/master/image/all_graph_result.png)

## セントロイド抽出結果

### community4 count8172(24.9%)
---
* brain:0.072744633813
* studi:0.0567753727706
* correl:0.0555539587486
* process:0.0523508223202
* fmri:0.0482326104747
* activ:0.0442766017731
* memori:0.0425555786907
* connect:0.0395569553584
* disord:0.038189251777
* attent:0.0378429939897
* cortex:0.0332452199021
* respons:0.0277350392028
* schizophrenia:0.0274277443699
* network:0.0264617827311
* work:0.0257441896742
* percept:0.0250704737886
* effect:0.0249371158147
* face:0.0247269637731
* imag:0.0238328453924
* modul:0.0234984259312
---
* Visual search: Bottom-up or top-down?:5.51506175045
* Visual consciousness and bodily self-consciousness:5.35050189549
* Cultural neuroscience:5.29950704874
* The Neural Basis of Empathy:4.8661234138
* Empathy and contextual social cognition:4.85494198656
* Tonal cognition:4.85494198656
* How infant perceive faces:4.75730811665
* The "What" and "When" of Self-Initiated Movements:4.61042076244
* Residual inhibition:4.59045910988
* Self-consciousness in non-communicative patients:4.51267382613
### community2 count6658(20.3%)
---
* model:0.0798068245731
* network:0.0604571746802
* spike:0.0592839020544
* neuron:0.0591440280747
* learn:0.0465948323512
* dynam:0.0440287996692
* memori:0.0415371112072
* plastic:0.0365535869813
* activ:0.0347250238495
* cell:0.0315029209085
* cortex:0.0293081884127
* oscil:0.0287925920879
* code:0.0286109566269
* system:0.0281423188264
* field:0.0249969179202
* pattern:0.0239745545327
* synaps:0.0236113326576
* mechan:0.0229417816075
* circuit:0.0223672006723
* comput:0.0222035914649
---
* Driven by inhibition:4.58788447768
* Neural Assembly Computing:4.31104093816
* Hippocampal Polysynaptic Computation:4.31104093816
* Biologically plausible neural computation:4.31104093816
* A Proto-Architecture for Innate Directionally Selective Visual Maps:4.30899206317
* Activity-dependent structural plasticity:4.22129305201
* Short-term synaptic plasticity:4.22129305201
* Two layers of neural variability:3.96402061275
* The hippocampus as a cognitive graph:3.89349197571
* Characterization of Weak Collective Neural Coherence:3.88586062414
### community3 count4642(14.2%)
---
* delay:0.272348927178
* stabil:0.236412359573
* network:0.148534954223
* synchron:0.102576952813
* analysi:0.0777274532985
* system:0.0732028770182
* solut:0.0633213495913
* time:0.0549127352078
* class:0.0527869693783
* control:0.0517511430664
* criteria:0.0465833739477
* uncertain:0.0453511038152
* recurr:0.044005883339
* distribut:0.0417669974023
* coupl:0.0411658743916
* jump:0.0402546146693
* mix:0.0397989603556
* bam:0.0396387400218
* robust:0.038450637056
* hopfield:0.0379348572683
---
* A new impulsive integro-differential inequality and its applications:3.47531903192
* Nontrivial Global Attractors in 2-D Multistable Attractor Neural Networks:3.11261711505
* Practical criteria for. positive-definite matrix, M-matrix and Hurwitz matrix:3.06295322343
* Non-autonomous Functional Differential Equations and Applications:3.04949914763
* ON A CLASS OF GLOBALLY STABLE NEURAL CIRCUITS:2.91868545782
* MEMRISTOR. A GENERAL PERSPECTIVE:2.83319332155
* A new nonlinear integro-differential inequality and its application:2.7824578667
* Stability of functional differential equations with variable impulsive perturbations via generalized ordinary differential equations:2.67818754683
* On periodic dynamical systems:2.67631844721
* On global exponential stability of standard and full-range CNNs:2.67195974354
### community1 count2612(8.0%)
---
* network:0.131642368803
* learn:0.101531065856
* memori:0.100156576325
* model:0.0825255834015
* perceptron:0.0741405259889
* hopfield:0.0605441570373
* dynam:0.0576593785521
* capac:0.0573661036274
* pattern:0.0553144164732
* storag:0.0438570908791
* gener:0.0359849727992
* retriev:0.0336040693104
* neural-network:0.032170028987
* algorithm:0.0317733136851
* attractor:0.0302537908892
* multilay:0.0271779335742
* rule:0.027014308741
* recognit:0.0247732657439
* properti:0.0247035341418
* use:0.0232553192182
---
* A multi-output-layer perceptron:5.24672796362
* Discrete chaos:4.74780669623
* ATTRACTORS IN THE FULLY ASYMMETRIC SK-MODEL:4.60219239239
* A SIMPLE-MODEL WITH STRONG ASYMMETRIC COUPLINGS:3.6343641502
* STORAGE CAPACITY OF A POTTS-PERCEPTRON:3.59372478679
* OPTIMAL CAPACITY OF GRADED-RESPONSE PERCEPTRONS:3.56209146658
* ROBOT ADAPTIVITY:3.54703148915
* CLIPPED-HEBBIAN TRAINING OF THE PERCEPTRON:3.51698637046
* Bayes-optimal performance in a discrete space:3.49334122257
* RANDOM NEURAL-NETWORK WITH LOCAL GAUGE-SYMMETRY:3.47227398407
### community5 count2419(7.4%)
---
* brain:0.0927409423192
* connect:0.076892874775
* network:0.0628078376894
* synchron:0.0409938011058
* model:0.0404404433428
* schizophrenia:0.0358634843951
* eeg:0.0354241561833
* dynam:0.034507352683
* reson:0.0341506803342
* causal:0.0324794415026
* oscil:0.0310471957296
* activ:0.0296433952051
* coupl:0.0292211508706
* studi:0.0289317694832
* analysi:0.0277911234625
* epilepsi:0.0276765210109
* read:0.0265333769752
* synchroni:0.0237962203588
* stimul:0.0236802613749
* neuron:0.0235045831757
---
* Adaptive stochastic resonance:4.58234191207
* Stochastic resonance:4.58234191207
* statistical mechanical problem?:3.94760030155
* Soft threshold stochastic resonance:3.66081363601
* Circular inferences in schizophrenia:3.51928348522
* It's about time:3.46285068009
* Visual perception and aging:3.35655788538
* The neural bases of attentive reading:3.33729354545
* Stochastic resonance in electrical circuits - II: Nonconventional stochastic resonance:3.32378942345
* Interictal perceptual function in epilepsy:3.27451250937
### community0 count2076(6.3%)
---
* problem:0.150847935706
* network:0.117976058907
* optim:0.106552739637
* solv:0.0908048893831
* algorithm:0.0606912933583
* hopfield:0.0529726469947
* program:0.0528698370321
* use:0.0523969639458
* approach:0.047761024361
* applic:0.0450087100944
* chao:0.0445294105754
* model:0.0435044914309
* recurr:0.0426459216176
* neural-network:0.041383119537
* system:0.0409766069499
* control:0.0379002939461
* linear:0.0345228554601
* comput:0.0317035928361
* dynam:0.03024146494
* base:0.0291671008588
---
* On the computational power of winner-take-all:5.73724679606
* A GLOBAL COMPETITIVE NEURAL-NETWORK:4.89725651468
* A GENERAL MEAN-BASED ITERATIVE WINNER-TAKE-ALL NEURAL-NETWORK:4.89725651468
* ON A CONSTANT-TIME, LOW-COMPLEXITY WINNER-TAKE-ALL NEURAL-NETWORK:4.89725651468
* PHYSICAL COMPUTATION:4.30768999688
* Neurodynamical optimization:4.2788883239
* Pseudo-Boolean optimization:4.2788883239
* A discrete-time dynamic K-winners-take-all neural circuit:3.99136258788
* Dissociation as complex adaptation:3.7700523098
* CLUSTERING FOR VEHICLE-ROUTING WITH A COMPETITIVE NEURAL-NETWORK:3.67505454111
### community6 count2068(6.3%)
---
* respiratori:0.0699429563729
* gener:0.062038021724
* pattern:0.0614169246274
* control:0.0591192799484
* locomot:0.0573423093715
* neuron:0.0570602933753
* motor:0.0543543089389
* activ:0.0529023797955
* circuit:0.0485098609832
* modul:0.0434306007623
* network:0.0406321330543
* develop:0.0401671309557
* cord:0.0396984962843
* model:0.0380470363315
* system:0.0377234384767
* mechan:0.0298566171539
* behavior:0.0282599919857
* rhythm:0.0280667374752
* interneuron:0.0266395578991
* robot:0.0264296518773
---
* NEURAL ARCHITECTURES FOR ADAPTIVE-BEHAVIOR:4.76703331376
* Multifunctional pattern-generating circuits:3.96362759279
* Evolutionary and developmental modules:3.82181876342
* Central nervous mechanisms of cough:3.80434933442
* Robotics and Neuroscience:3.61057326198
* Electrophysiological, molecular and genetic identifications of the pre-Botzinger complex:3.49907554766
* Theory in motion:3.48778489284
* Optogenetic manipulation of neural and non-neural functions:3.40677348932
* Sparse and powerful cortical spikes:3.40532991018
* Neuron-astrocyte communication and synaptic plasticity:3.3559504255
### community9 count1190(3.6%)
---
* cnn:0.187170032446
* cellular:0.139845707161
* network:0.109651558157
* imag:0.0687762137719
* implement:0.061393330819
* design:0.0518573184593
* system:0.0486878102441
* base:0.0471425018183
* applic:0.0469391957035
* nonlinear:0.038202672675
* analog:0.0380690904248
* use:0.0379636414917
* pattern:0.0355381832036
* algorithm:0.0347757004847
* process:0.0343180464265
* circuit:0.0342335539444
* stabil:0.0340281110425
* analysi:0.0339814443181
* wave:0.0323817218292
* model:0.0306162291719
---
* Current-mode programmable piecewise-linear neural synapses:4.78875971339
* Passivity and complexity:3.6656270552
* Neural computation with cellular cultures:3.42244890538
* Toward CNN chip-specific robustness:3.20392979142
* Bio-inspired nano-sensor-enhanced CNN visual computer:3.12248503244
* Locally active Hindmarsh-Rose neurons:3.11082612847
* DYNAMIC BEHAVIOUR OF PIEZOELECTRIC SOLID VIA CNN APPROACH:2.90634818774
* FUNCTIONAL TESTING FOR CELLULAR NEURAL NETWORKS:2.88580630907
* On binary output of cellular neural networks:2.83116139751
* THE ANALOGIC CELLULAR NEURAL-NETWORK AS A BIONIC EYE:2.81147023023
### community10 count1139(3.5%)
---
* model:0.107498364556
* learn:0.100160269755
* connectionist:0.0671398481226
* network:0.0554268238153
* recurr:0.0532993883367
* control:0.0527076244154
* languag:0.0525035089199
* movement:0.0516396504884
* comput:0.0459936673055
* system:0.0453257440253
* motor:0.0399685847595
* develop:0.0383964527576
* robot:0.0337562223077
* gener:0.0330358875528
* simul:0.0323164509672
* use:0.028986295183
* represent:0.0268707627468
* process:0.0233520333527
* dynam:0.0227587596931
* approach:0.0209701826274
---
* TOWARD A NONCOMPUTATIONAL COGNITIVE NEUROSCIENCE:5.29737350081
* Neural and super-Turing computing:4.28906730665
* Cerebellar circuitry as a neuronal machine:3.90062391562
* Feedback-dependent generalization:3.87474059237
* Connectionist neuroimaging:3.77821992303
* A 3RD SOURCE OF DEVELOPMENTAL DIFFERENCES:3.71860943845
* Computational perspectives on cognitive development:3.4673466521
* Methods for binary multidimensional scaling:3.45044804233
* A virtual machine for neural computers:3.38247085636
* MODEL-BASED NEUROIMAGING FOR COGNITIVE COMPUTING:3.32310337729
### community7 count1023(3.1%)
---
* model:0.100567015336
* learn:0.0650455921556
* network:0.0622027132173
* segment:0.0586418914102
* oscil:0.0575162917912
* recognit:0.0539773634419
* object:0.0467071767209
* use:0.0359034496378
* code:0.0352629877945
* attent:0.034502430458
* map:0.0344569808839
* imag:0.0337747245059
* oscillatori:0.0325807065409
* field:0.0325736197713
* develop:0.0324353212926
* cortex:0.0316774747976
* coupl:0.031185540811
* synchron:0.0301507956508
* neuron:0.0294808381252
* comput:0.0281517471067
---
* Internal representation of two-dimensional shape:3.53146798303
* A self-organizing map with homeostatic synaptic scaling:3.35563454476
* THE PRINCIPAL COMPONENTS OF NATURAL IMAGES:3.15937024139
* Cortical direction selectivity without directional experience:3.04176748253
* Temporal segmentation in a neural dynamic system:3.03922322002
* RHYTHMIC AND PATTERNED NEURONAL FIRING IN VISUAL-CORTEX:3.01644156553
* DISCOVERING PREDICTABLE CLASSIFICATIONS:2.81546744389
* ARTIFICIAL VERSUS REAL NEURAL NETWORKS:2.80446290361
* A learning-style theory for understanding autistic behaviors:2.79078768797
* Neural networks for consciousness:2.70754075393
### community8 count592(1.8%)
---
* bifurc:0.284221437034
* delay:0.171691943578
* hopf:0.139904803037
* network:0.107258441479
* system:0.0995611306074
* chao:0.096952378656
* analysi:0.0955398482645
* stabil:0.0913704880645
* model:0.0693894691796
* oscil:0.0675218166047
* neuron:0.0624548971296
* coupl:0.0613882192215
* dynam:0.0612485166016
* solut:0.0534380058066
* equat:0.050990042049
* hopfield:0.0507212909252
* class:0.0425336288235
* time:0.0425026224556
* synchron:0.0411982681513
* bam:0.0364297550033
---
* STOCHASTIC SINGLE NEURONS:3.07572587017
* Symbolic functions from neural computation:2.86367033133
* LIVING MACHINES:2.67659294294
* Convergence under dynamical thresholds with delays:2.57252714497
* 2-DIMENSIONAL MOVEMENT CONTROLLED BY A CHAOTIC NEURAL-NETWORK:2.49304924503
* Hopf Bifurcation in a Chaotic Associative Memory:2.38140210561
* CHAOS IN AN EFFECTIVE 4-NEURON NEURAL NETWORK:2.3525120627
* Chaos in a three dimensional neural network:2.3525120627
* Chaos in two-loop negative feedback systems:2.31888377355
* Chaos and transient chaos in simple Hopfield neural networks:2.28903223397
### community11 count144(0.4%)
---
* integr:0.0975797007537
* model:0.091563481405
* neuron:0.0532802537275
* role:0.0514413904433
* activ:0.0477660906215
* code:0.0474317158934
* network:0.0440335535026
* space:0.0409604992234
* enhanc:0.0400989222222
* brain:0.0388812828032
* interact:0.038043580734
* epilepsi:0.0366894081805
* inform:0.0345127987145
* percept:0.0322328861687
* signal:0.0320429330971
* respons:0.0312646198795
* represent:0.0295588169061
* studi:0.0280432086535
* cortex:0.0278247014773
* modul:0.026822897872
---
* Seizure-Induced Oxidative Stress in Temporal Lobe Epilepsy:3.12215664116
* The glial perspective of autism spectrum disorders:2.54090820021
* A digital implementation of neuron-astrocyte interaction for neuromorphic applications:2.471073548
* Neuroprotective role of fibronectin in neuron-glial extrasynaptic transmission:2.24270556133
* Diffusive Feedback Influences on Hierarchical Information Processing:2.15873917396
* Local intracortical circuitry not only for feature binding but also for rapid neuronal responses:2.14707978868
* Astrocytes and the evolution of the human brain:2.04693914233
* Neural bases of peri-hand space plasticity through tool-use: Insights from a combined computational-experimental approach:2.02075106869
* Transient impact of spike on theta rhythm in temporal lobe epilepsy:1.9898480303
* A novel digital implementation of neuron-astrocyte interactions:1.95340499135
### community12 count66(0.2%)
---
* condit:0.235391129298
* model:0.129371251695
* approach:0.116996878305
* learn:0.113214815975
* map:0.105717191529
* stimulu:0.10394592158
* set:0.0985418339323
* hippocampu:0.0898290202744
* function:0.0746906746933
* inhibit:0.0698735320997
* network:0.0679480602262
* time:0.0612845312976
* lesion:0.0517559200547
* mechan:0.0488690658598
* cognit:0.0474057177452
* role:0.0473405202822
* dysfunct:0.0429771870595
* schizophrenia:0.0413524521092
* attent:0.0401479391533
* process:0.0401146569571
---
* Hippocampal dysfunction in schizophrenia:3.51067117158
* Conditioning and cognition:3.17116144398
* The transition from automatic to controlled processing:2.95898955027
* Hippocampal lesions interfere with Pavlovian negative occasion setting:2.60108877007
* Occasion setting in Pavlovian ambiguous target discriminations:2.3716831823
* Quantitative models of Pavlovian conditioning:2.31503272992
* The Role of Associative Processing in Cognitive Computing:2.24575798832
* Stimulus configuration, long-term potentiation, and the hippocampus:2.19597506884
* Three-dimensional cognitive mapping with a neural network:2.13442848931
* STIMULUS CONFIGURATION, SPATIAL-LEARNING, AND HIPPOCAMPAL FUNCTION:2.12982543634
