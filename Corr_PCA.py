import cal_func as cf
import pandas as pd
import talib
import seaborn as sns
import matplotlib.pyplot as plt
from igraph import Graph as IGraph
import igraph
from PIL import Image

def ROC(symbol):
    temp=cf.fetch_data(symbol)
    result=pd.DataFrame([])
    result[symbol]=talib.ROC(temp.close, timeperiod=1)
    result['time']=temp['time']
    result=result.set_index('time')
    print(symbol+' done!')
    return result

a0=ROC('a0')igraph.Graph
y0=ROC('y0')
m0=ROC('m0')
oi0=ROC('oi0')
rm0=ROC('rm0')
p0=ROC('p0')
cs0=ROC('cs0')
c0=ROC('c0')
ap0=ROC('ap0')
sr0=ROC('sr0')
cf0=ROC('cf0')
jd0=ROC('jd0')
ru0=ROC('ru0')
rb0=ROC('rb0')
hc0=ROC('hc0')
i0=ROC('i0')
j0=ROC('j0')
jm0=ROC('jm0')
zc0=ROC('zc0')
fg0=ROC('fg0')
sf0=ROC('sf0')
sm0=ROC('sm0')
l0=ROC('l0')
v0=ROC('v0')
pp0=ROC('pp0')
ta0=ROC('ta0')
ma0=ROC('ma0')
al0=ROC('al0')
zn0=ROC('zn0')
au0=ROC('au0')
ag0=ROC('ag0')
cu0=ROC('cu0')

total=a0.join([y0,m0,oi0,rm0,p0,cs0,c0,ap0,sr0,cf0,jd0,ru0,rb0,hc0,i0,j0,jm0,zc0,fg0,sf0,sm0,l0,v0,pp0,ta0,ma0,al0,zn0,au0,ag0,cu0],how='inner').dropna(axis=0)

corr=total.corr()

sns.heatmap(corr,xticklabels=1,yticklabels=1)
plt.show()

A=corr.values
g=igraph.Graph.Adjacency((A>0).tolist())
g.es['weight'] = A[A.nonzero()]
g.vs['label'] = corr.columns
cluster=IGraph.community_walktrap(g, g.es['weight'])

clusters = IGraph.community_walktrap(g, g.es['weight'],steps=10000).as_clustering(8)

nodes = [{"label": node["label"]} for node in g.vs]
community = {}

for node in nodes:
    idx = g.vs.find(label=node["label"]).index
    node["community"] = clusters.membership[idx]
    if node["community"] not in community:
        community[node["community"]] = [node["label"]]
    else:
        community[node["community"]].append(node["label"])
for c,l in community.items():
    print("Community ", c, ": ", l)

