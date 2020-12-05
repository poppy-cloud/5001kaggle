
import pandas as pd
from data_process import get_data
import xgboost as xgb
import csv

# load the data
x_train, y_train, x_val = get_data()

# train the model
reg = xgb.XGBRegressor()
reg.fit(x_train, y_train, eval_set=[(x_train[8000:14007], y_train[8000:14007])])

# prediction
y_pred = reg.predict(x_val)

test_result = []

for i in range(len(x_val)):
    test_result.append(y_pred[i])
print(test_result)

# write the result
result = csv.reader(open('test.csv', 'r'))
result = [i for i in result]
result[0].append('speed')
for i in range(1, len(result)):
    result[i].append(test_result[i - 1])
with open('result.csv', 'w', newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerows(result)

# write the final result
result = pd.read_csv('result.csv')
d = result.drop(['date'],axis=1)
d = pd.DataFrame(d.values,columns=['id','speed'])
d.to_csv('finalresult.csv',index=False)