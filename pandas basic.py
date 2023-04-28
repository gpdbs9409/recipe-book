import numpy as np 
import pandas as pd

_li=[1,2,3,4]
_tp=(5,6,7,8)

li_sr=pd.Series(_li)
np_sr=pd.Series(np.array(_li))
tp_sr=pd.Series(_tp)

_index=['a','b','c','d']

li_sr=pd.Series(_li,index=_index)

print(li_sr,li_sr.values,li_sr.index)