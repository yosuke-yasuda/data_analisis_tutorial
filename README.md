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
* nltk==3.0.4
* nose==1.3.7
* numpy==1.9.2
* pbr==1.3.0
* pyparsing==2.0.3
* python-dateutil==2.4.2
* python-louvain==0.4
* pytz==2015.4
* scikit-learn==0.16.1
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

* Cognitive Demands of Lower Paleolithic Toolmaking:0.233634094551
* Decision-related loss: Regret and disappointment:0.233634094551
* The units of thought:0.233634094551
* Ictal singing: case report and reappraisal of the literature:0.233634094551
* The functional anatomy of gaze-evoked tinnitus and sustained lateral gaze:0.233634094551
* The neurobiology of psychopathy:0.233634094551
* Hemispheric asymmetry in the fusiform gyrus distinguishes Homo sapiens from chimpanzees:0.233634094551
* An early attentional bias to BEGIN-stimuli of the smoking ritual is accompanied with mesocorticolimbic deactivations in smokers:0.233634094551
* The neuroethology of friendship:0.233634094551
* Functional parcellation of the inferior frontal and midcingulate cortices in a flanker-stop-change paradigm:0.233634094551
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

* The Neuronal Replicator Hypothesis:0.226796293258
* Brain-Machine Interfaces beyond Neuroprosthetics:0.226796293258
* Moving the goal posts: a reply to Dawson and Piercey:0.226796293258
* Heteroclinic contours in neural ensembles and the winnerless competition principle:0.226796293258
* Mesoscopic neurodynamics:0.226796293258
* Semiconductor Nanomembrane Tubes: Three-Dimensional Confinement for Controlled Neurite Outgrowth:0.226796293258
* Buildup and decay of a three-dimensional rotational aftereffect obtained with a three-dimensional figure:0.226796293258
* Basal ganglia physiology and pathophysiology: A reappraisal:0.226796293258
* JS Bach's Passacaglia and Walter Benjamin's Das Passagen-Werk - literary montage as mosaic in Memorandum. A story with paintings (2006):0.226796293258
* NEUROPOIESIS - PROPOSAL FOR A CONNECTIONISTIC NEUROBIOLOGY:0.226796293258
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

* On pth moment exponential stability of stochastic Cohen-Grossberg neural networks with time-varying delays:0.337605018989
* A proof of Kaszkurewicz and Bhaya's conjecture on absolute stability of neural networks in two-neuron case:0.40108155958
* Exponential stability preservation in discrete-time analogues of artificial neural networks with distributed delays:0.41501164654
* Delay-Dependent Stability Criterion of Caputo Fractional Neural Networks with Distributed Delay:0.41501164654
* GUARANTEED COST STABILIZATION OF CELLULAR NEURAL NETWORKS WITH TIME-VARYING DELAY:0.41501164654
* Razumikhin-type theorems on stability of stochastic neural networks with delays:0.41501164654
* pth moment exponential stability of stochastic cohen-grossberg neural networks with time-varying delays:0.41501164654
* Global exponential stability of time-varying delay neural networks via razumikhin technique:0.41501164654
* On a general decay stability of stochastic Cohen-Grossberg neural networks with time-varying delays (vol 219, pg 2289, 2012):0.41501164654
* Exponential stability of impulsive high-order Hopfield-type neural networks with time-varying delays:0.41501164654
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

* A Neural Networks-Based Hybrid Routing Protocol for Wireless Mesh Networks:0.27153344637
* Conducting swift heavy ion track networks:0.276570109299
* STABILITY-CAPACITY DIAGRAM OF A NEURAL NETWORK WITH ISING BONDS:0.276570109299
* Immune networks: multitasking capabilities near saturation:0.276570109299
* COMPUTER-MODEL OF A SENSE OF HUMOR .2. REALIZATION IN NEURAL NETWORKS:0.276570109299
* EXTENSIONS OF A SOLVABLE FEED FORWARD NEURAL NETWORK:0.290567112541
* A MAXIMUM OVERLAP NEURAL NETWORK FOR PATTERN-RECOGNITION:0.290567112541
* LYAPUNOV EXPONENTS AND DIMENSIONS OF CHAOTIC NEURAL NETWORKS:0.290567112541
* Categorization ability in a biologically motivated neural network:0.290567112541
* Quantifying the osteocyte network in the human skeleton:0.290567112541
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

* Cultural neurolinguistics:0.238361664921
* Small worlds: How and why:0.238361664921
* Interactive rTMS protocols in psychiatry:0.238361664921
* Harmony in the small-world:0.238361664921
* Are proprioceptive-induced reflex seizures epileptically-enhanced stretch reflex manifestations?:0.238361664921
* NORMAL ANATOMY AND NEUROPHYSIOLOGY OF THE HIPPOCAMPAL-FORMATION:0.238361664921
* Electromyographic Permutation Entropy Quantifies Diaphragmatic Denervation and Reinnervation:0.238361664921
* Python as a Federation Tool for GENESIS 3.0:0.238361664921
* What Is a Seizure Focus?:0.238361664921
* Self-emergence of knowledge trees: Extraction of the Wikipedia hierarchies:0.238361664921
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

* ONE-LAYER FEEDFORWARD NEURAL NETWORK FOR FAST MAXIMUM MINIMUM DETERMINATION:0.301985608262
* Neural Network for Nonsmooth, Nonconvex Constrained Minimization Via Smooth Approximation:0.301985608262
* Minimum energy configurations of the 2-dimensional HP-model of proteins by self-organizing networks:0.304217851297
* Decomposition co-ordination artificial neural network for satellite broadcast scheduling:0.304217851297
* Fair TDMA scheduling in wireless multihop networks:0.310127202088
* EASING THE CONSCIENCE OF THE GUILTY NET:0.323689692225
* Self-annealing and self-annihilation: unifying deterministic annealing and relaxation labeling:0.323689692225
* The concave-convex procedure:0.323689692225
* Time-adaptive vector A/D conversion:0.323689692225
* HOPFIELD-TANK NEURAL NET - WALSH TO FOURIER-TRANSFORM:0.323689692225
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

* New neural nets:0.240776592733
* Acute carbon dioxide avoidance in Caenorhabditis elegans:0.240776592733
* RESPIRATORY-RELATED NEURAL ASSEMBLIES IN THE BRAIN-STEM MIDLINE:0.240776592733
* Closed-loop optogenetic intervention in mice:0.240776592733
* Electroporation loading of calcium-sensitive dyes into the CNS:0.240776592733
* THE COMPUTATIONAL LEECH:0.240776592733
* BRAIN-STEM NEUROMODULATION AND REM-SLEEP:0.240776592733
* Checks and balances in neuromodulation:0.240776592733
* Flapping flexible fish - Periodic and secular body reconfigurations in swimming lamprey, Petromyzon marinus:0.240776592733
* Neuronal pacemaker for breathing visualized in vitro:0.240776592733
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

* A cellular neural network for clustering-based adaptive quantization in subband video compression:0.333502755659
* Homogenization of periodic electrical networks including voltage to current amplifiers:0.333502755659
* A DIGITAL MULTIPROCESSOR HARDWARE ACCELERATOR BOARD FOR CELLULAR NEURAL NETWORKS - CNN-HAC:0.333502755659
* Toward visual microprocessors:0.341528090611
* A bio-inspired two-layer mixed-signal flexible programmable chip for early vision:0.341528090611
* Issues of nanoelectronics: A possible roadmap:0.341528090611
* The spatiotemporal prisoner's dilemma:0.341528090611
* Considerations about nanoelectronic GSI processors:0.341528090611
* A low-power orientation-selective vision sensor:0.341528090611
* EXPERIMENTAL-VERIFICATION OF HORSESHOES FROM ELECTRONIC-CIRCUITS:0.341528090611
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

* SHADOWING ON FRACTALS:0.261449920619
* THE ADAPTIVE-CONTROL OF A 4-DEGREES-OF-FREEDOM STEREO CAMERA HEAD:0.261449920619
* A NEURAL COMPILER:0.261449920619
* Artificial life and Piaget:0.261449920619
* A defence of functional modularity:0.261449920619
* LINEAR-SYSTEMS WITH SIGN-OBSERVATIONS:0.261449920619
* Hypercomputation:0.261449920619
* Rethinking eliminative connectionism:0.261449920619
* Dominant-language replacement: The case of international adoptees:0.261449920619
* Artificial life and Piaget:0.261449920619
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

* A DEEPER UNITY - SOME FEYERABENDIAN THEMES IN NEUROCOMPUTATIONAL FORM:0.255925512388
* Cognitive conflict without explicit conflict monitoring in a dynamical agent:0.255925512388
* Elemental operations in vision:0.255925512388
* Bistable neuromodules:0.255925512388
* Boundary completion in illusory contours: Interpolation or extrapolation?:0.255925512388
* Synchronisation in neural assemblies:0.255925512388
* Slice sampling - Discussion:0.255925512388
* Optimal extraction of hidden causes:0.255925512388
* Chemical kinetics is turing universal:0.255925512388
* THE MOD-2 NEUROCOMPUTER SYSTEM-DESIGN:0.255925512388
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

* Evaluating Lyapunov exponent spectra with neural networks:0.470180030258
* Evolved neurocontrollers for pole-balancing:0.474945024198
* Evolving neurocontrollers for balancing an inverted pendulum:0.474945024198
* Special issue in honor of Pauline van den Driessche - Preface:0.474945024198
* Common non-trivial invariant closed cones for commuting contractions:0.474945024198
* High-dimensional chaotic neural network under external sinusoidal force:0.50849923763
* TWO KINDS OF HORSESHOES IN A HYPERCHAOTIC NEURAL NETWORK:0.50849923763
* Zero singularities in a ring network with two delays:0.516043119851
* Bifurcation analysis in the delayed Leslie-Gower predator-prey system (Retracted article. See vol. 37, pg. 9451, 2013):0.570717894175
* RECURSIVE CONSTRUCTION OF PERIODIC STEADY-STATE FOR NEURAL NETWORKS:0.592466766033
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

* Tools for the body (schema):0.25609037034
* All vertebrates started out with a glial blood-brain barrier 4-500 million years ago:0.25609037034
* Thyroid hormone and astrocyte morphogenesis:0.25609037034
* OPINION Disentangling calcium-driven astrocyte physiology:0.25609037034
* Depletion of Extracellular Ca2+ Prompts Astroglia to Moderate Synaptic Network Activity:0.435660471121
* Physiology of neuronal-glial networking:0.501381964856
* Subthreshold Membrane Depolarization as Memory Trace for Perceptual Learning:0.699863732861
* Rab22B Is Expressed in the CNS Astroglia Lineage and Plays a Role in Epidermal Growth Factor Receptor Trafficking in A431 Cells:0.737399111505
* Optical imaging of visually guided reaching in macaque posterior parietal cortex:0.740886009411
* Regulation of Local Ambient GABA Levels via Transporter-Mediated GABA Import and Export for Subliminal Learning:0.749309789782
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

* Latent learning, shortcuts and detours: a computational model:0.704983082896
* Escape, avoidance, and imitation: A neural network approach:0.752674976697
* Latent Inhibition and Compound Conditioning: A Reply to Holmes and Harris (2009):0.807487857143
* Effect of distracter preexposure on the reset of an internal clock:0.81539246228
* Stimulus specificity of concurrent recovery in the rabbit nictitating membrane response:0.855092582102
* Proteus caught in a (neural) net. Animal learning and cognition: A neural network approach:0.918380445651
* Expression of the CS- and US-pre-exposure effects in the conditioned taste aversion paradigm and their abolition following systemic amphetamine treatment in C57BL6/J mice:0.919193900684
* HIPPOCAMPECTOMY DISRUPTS THE TOPOGRAPHY OF THE RAT EYEBLINK RESPONSE DURING ACQUISITION AND EXTINCTION OF CLASSICAL-CONDITIONING:0.920334289996
* Water maze performance, exploratory activity, inhibitory avoidance and hippocampal plasticity in aged superior and inferior learners:0.925408039058
* Disruption of learned irrelevance in acute schizophrenia in a novel continuous within-subject paradigm suitable for fMR1:0.975511293935
