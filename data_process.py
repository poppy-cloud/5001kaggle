
import pandas as pd


def readtrain():
    data = pd.read_csv('train.csv')

    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y %H:%M')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['hour'] = data['date'].dt.hour
    data['weekday'] = data['date'].dt.weekday
    data['quarter'] = data['date'].dt.quarter
    data['dayofyear'] = data['date'].dt.dayofyear
    data['daysinmonth'] = data['date'].dt.daysinmonth
    data['weekofyear'] = data['date'].dt.weekofyear
    data['isholiday'] = 0

    # the feature of 2017 holiday
    for i in range(0, 8750):
        if data.loc[i]['weekday'] == 6:
            data.loc[i, 'isholiday'] = 0.5
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 28:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 30:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 31:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 4:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 14:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 15:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 17:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 3:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 30:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 7 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 5:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 28:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 25:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 26:
            data.loc[i, 'isholiday'] = 1

    # the feature of 2018 holiday
    for i in range(8750,14006):
        if data.loc[i]['weekday'] == 6:
            data.loc[i, 'isholiday'] = 0.5
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 16:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 17:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 19:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 3 and data.loc[i]['day'] == 30:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 3 and data.loc[i]['day'] == 31:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 5:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 22:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 6 and data.loc[i]['day'] == 18:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 7 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 9 and data.loc[i]['day'] == 25:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 17:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 25:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 26:
            data.loc[i, 'isholiday'] = 1


    return data.loc[:,['year','month','hour','weekday','quarter','dayofyear','daysinmonth','weekofyear','isholiday']], data.loc[:,'speed']

def readtest():
    data = pd.read_csv('test.csv')

    data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y %H:%M')
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['hour'] = data['date'].dt.hour
    data['weekday'] = data['date'].dt.weekday
    data['quarter'] = data['date'].dt.quarter
    data['dayofyear'] = data['date'].dt.dayofyear
    data['daysinmonth'] = data['date'].dt.daysinmonth
    data['weekofyear'] = data['date'].dt.weekofyear
    data['isholiday'] = 0

    # the feature of 2018 holiday
    for i in range(0,3504):
        if data.loc[i]['weekday'] == 6:
            data.loc[i, 'isholiday'] = 0.5
        if data.loc[i]['month'] == 1 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 16:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 17:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 2 and data.loc[i]['day'] == 19:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 3 and data.loc[i]['day'] == 30:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 3 and data.loc[i]['day'] == 31:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 4 and data.loc[i]['day'] == 5:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 5 and data.loc[i]['day'] == 22:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 6 and data.loc[i]['day'] == 18:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 7 and data.loc[i]['day'] == 2:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 9 and data.loc[i]['day'] == 25:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 1:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 10 and data.loc[i]['day'] == 17:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 25:
            data.loc[i, 'isholiday'] = 1
        if data.loc[i]['month'] == 12 and data.loc[i]['day'] == 26:
            data.loc[i, 'isholiday'] = 1

    return data.loc[:,['year','month','hour','weekday','quarter','dayofyear','daysinmonth','weekofyear','isholiday']]



def get_data():
    x_train, y_train = readtrain()

    test_data = readtest()

    return x_train, y_train, test_data



