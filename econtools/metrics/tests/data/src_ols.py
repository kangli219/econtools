import pandas as pd
import numpy as np

class regout(object):

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)



stat_names=['coeff', 'se', 't', 'p>t', 'CI_low', 'CI_high']
var_names=['mpg', 'length', '_cons']
ols_std = regout(
summary=pd.DataFrame(np.array([
[-173.7021808338409,
87.72302250337235,
-1.980120792431237,
.0515663415672996,
-348.6169197618126,
1.212558094130884,
],
[21.2860458491607,
22.79323097079149,
.9338757579580457,
.3535331991049651,
-24.16236587682247,
66.73445757514388,
],
[5864.305369862909,
5888.102571587057,
.9959584260914575,
.3226526347216224,
-5876.237701947869,
17604.84844167369,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[7695.328677127171,
1591.153916453681,
-462919.1285307264,
],
[1591.153916453681,
519.5313780878485,
-131524.0736134961,
],
[-462919.1285307264,
-131524.0736134961,
34669751.89353012,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=.2290527372803057,
r2_a=.2073359129783425,
mss=145463467.3336591,
tss=np.nan,
rss=489601928.7879626,
kappa=np.nan,
F=10.5472482576377,
pF=.0000975833702397,
)
ols_robust = regout(
summary=pd.DataFrame(np.array([
[-173.7021808338409,
93.80219372722709,
-1.851792308173086,
.0682136435170329,
-360.7384429056157,
13.33408123793402,
],
[21.2860458491607,
21.20589282528531,
1.003779752379953,
.3188935780499417,
-20.99730350906205,
63.56939520738347,
],
[5864.305369862909,
5717.802704310564,
1.025622196694877,
.3085513725020204,
-5536.669411046915,
17265.28015077273,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[8798.851548040242,
1633.917275339252,
-498349.1012917472,
],
[1633.917275339252,
449.6898905174871,
-117930.1824765652,
],
[-498349.1012917472,
-117930.1824765652,
32693267.7654212,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=.2290527372803057,
r2_a=.2073359129783425,
mss=145463467.3336591,
tss=np.nan,
rss=489601928.7879626,
kappa=np.nan,
F=11.5135888333688,
pF=.0000466848172678,
)
ols_hc2 = regout(
summary=pd.DataFrame(np.array([
[-173.7021808338409,
97.21204492200658,
-1.786838050502923,
.0782322400502068,
-367.5374930807868,
20.13313141310505,
],
[21.2860458491607,
21.56883774243083,
.986888867325762,
.3270484242895609,
-21.72099511949763,
64.29308681781903,
],
[5864.305369862909,
5853.494773364005,
1.001846861903439,
.3198198219533746,
-5807.231712205273,
17535.84245193109,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[9450.181677918226,
1730.421139321048,
-529860.3681375212,
],
[1730.421139321048,
465.2147615593085,
-122836.5407396346,
],
[-529860.3681375212,
-122836.5407396346,
34263401.06179972,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=.2290527372803057,
r2_a=.2073359129783425,
mss=145463467.3336591,
tss=np.nan,
rss=489601928.7879626,
kappa=np.nan,
F=11.09650055630861,
pF=.0000640566634589,
)
ols_hc3 = regout(
summary=pd.DataFrame(np.array([
[-173.7021808338409,
103.361133224103,
-1.680536729964323,
.0972477731557754,
-379.7984269190491,
32.39406525136741,
],
[21.2860458491607,
22.45860917052743,
.9477900295399642,
.3464511745327737,
-23.49514895744938,
66.06724065577079,
],
[5864.305369862909,
6140.199945409585,
.9550674932413342,
.3427841225640869,
-6378.905588532597,
18107.51632825841,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[10683.52386137078,
1926.610875841512,
-592480.6250128914,
],
[1926.610875841512,
504.3891258744989,
-134225.4636307235,
],
[-592480.6250128914,
-134225.4636307235,
37702055.36960787,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=.2290527372803057,
r2_a=.2073359129783425,
mss=145463467.3336591,
tss=np.nan,
rss=489601928.7879626,
kappa=np.nan,
F=10.22956063950845,
pF=.0001247705276063,
)
ols_cluster = regout(
summary=pd.DataFrame(np.array([
[-173.7021808338409,
93.45787726027342,
-1.858614660699952,
.0715077012033695,
-363.4317584173695,
16.02739674968774,
],
[21.2860458491607,
19.73552996926437,
1.078564694351308,
.2881592082933156,
-18.77921000966515,
61.35130170798657,
],
[5864.305369862909,
5224.131729286396,
1.122541634428495,
.2692740174602261,
-4741.245871985581,
16469.8566117114,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[8734.374821996333,
1348.973303185951,
-439213.4813662018,
],
[1348.973303185951,
389.4911431677319,
-98196.75311345223,
],
[-439213.4813662018,
-98196.75311345223,
27291552.32493687,
],
]),
columns=var_names,
index=var_names),
N=74,
r2=.2290527372803057,
r2_a=.2073359129783425,
mss=145463467.3336591,
tss=np.nan,
rss=489601928.7879626,
kappa=np.nan,
F=8.116658671734747,
pF=.0012706397120666,
)