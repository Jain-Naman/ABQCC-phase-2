import json
import numpy as np

with open('west.westpp.save/westpp.json','r') as f:
    data = json.load(f)

y = np.array(data['output']['L']['K00001']['local_factor'],dtype='f8')
x = np.array([i+1 for i in range(y.shape[0])])

loc_data = np.column_stack([x,y])
np.savetxt("localization_westpp.txt", loc_data, fmt=["%d","%f"])

y = np.array(data['output']['L']['K00001']['ipr'],dtype='f8')
x = np.array([i+1 for i in range(y.shape[0])])

ipr_data = np.column_stack([x,y])
np.savetxt("ipr_westpp.txt", ipr_data, fmt=["%d","%f"])

