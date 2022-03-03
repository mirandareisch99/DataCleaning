import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.utils import resample

#for x in range(0,1):

audio1_tr = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Prep/All_audio3_phq.csv")
audio1_te = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Prep/All_audio3_phq.csv")

audio2_tr = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Prep/All_audio4_phq.csv")
audio2_te = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Prep/All_audio4_phq.csv")

aud_short_id = audio1_tr.num.to_list()




#train_short, test_short = train_test_split(short_id, shuffle=True)
train, test = train_test_split(aud_short_id, shuffle=True)


for i in train:

    audio1_te = audio1_te[audio1_te.num != i]
    audio2_te = audio2_te[audio2_te.num != i]
    #audio4_short = audio4_short[audio4_short.audio_features !=i]
for i in test:
    audio1_tr =audio1_tr[audio1_tr.num != i]
    audio2_tr = audio2_tr[audio2_tr.num!=i]
    #audio4_short_test=audio4_short_test[audio4_short_test.audio_features !=i]

# upsampling
#Count 1s and 0s
ones = len(audio1_tr.loc[audio1_tr['Label'] == 1])
zeros = len(audio1_tr.loc[audio1_tr['Label'] == 0])
if ones >= zeros:
    majority = 1
    minority = 0
else:
    majority = 0
    minority = 1

# Upsample TrainingSet
train_majority = audio1_tr[audio1_tr.Label==majority]
train_minority = audio1_tr[audio1_tr.Label==minority]

# Upsample minority class
train_minority_upsampled = resample(train_minority,
                                 replace=True,     # sample with replacement
                                 n_samples=len(train_majority),    # to match majority class
                                 random_state=42) # reproducible results

# Combine majority class with upsampled minority class
audio1_tr = pd.concat([train_majority, train_minority_upsampled])

ones = len(audio2_tr.loc[audio2_tr['Label'] == 1])
zeros = len(audio2_tr.loc[audio2_tr['Label'] == 0])
if ones >= zeros:
    majority = 1
    minority = 0
else:
    majority = 0
    minority = 1

# Upsample TrainingSet
train_majority = audio2_tr[audio2_tr.Label==majority]
train_minority = audio2_tr[audio2_tr.Label==minority]

# Upsample minority class
train_minority_upsampled = resample(train_minority,
                                 replace=True,     # sample with replacement
                                 n_samples=len(train_majority),    # to match majority class
                                 random_state=42) # reproducible results

# Combine majority class with upsampled minority class
audio2_tr = pd.concat([train_majority, train_minority_upsampled])

audio1_te.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Audio3_test.csv")
audio1_tr.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Audio3_train.csv")

audio2_te.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Audio4_test.csv")
audio2_tr.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Experiments/Audio4_train.csv")

'''
audio1 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio1_scripts.csv")
audio1_short = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio1_short.csv")
audio2 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio2_scripts.csv")
audio2_short = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio2_short.csv")
audio3 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts.csv")
audio4 = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio4_scripts.csv")


audio1_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio1_scripts.csv")
audio1_short_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio1_short.csv")
audio2_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio2_scripts.csv")
audio2_short_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio2_short.csv")
audio3_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts.csv")
audio4_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio4_scripts.csv")
'''
'''
audio3_short = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts_short.csv")
audio4_short = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio4_scripts_short.csv")
audio3_short_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio3_scripts_short.csv")
audio4_short_test = pd.read_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/audio4_scripts_short.csv")
#sessionid = demographics.sessionid.to_list()
'''

'''
short_id = audio1_short.id.to_list()
long_id = audio1.id.to_list()'''
'''
frames = [audio1_te, audio1_tr]
result = pd.concat(frames)
result2 = pd.concat(frames)'''

'''
for i in test_short:
    audio1_short=audio1_short[audio1_short.id != i]
    audio2_short=audio2_short[audio2_short.id != i]
    audio3 = audio3[audio3.id != i]
    audio4 = audio4[audio4.id != i]

for i in train_short:
    audio1_short_test=audio1_short_test[audio1_short_test.id != i]
    audio2_short_test=audio2_short_test[audio2_short_test.id !=i]
    audio3_test = audio3_test[audio3_test.id !=i]
    audio4_test = audio4_test[audio4_test.id !=i]

for i in test_long:
    audio1 = audio1[audio1.id !=i]
    audio2 = audio2[audio2.id !=i]

for i in train_long:
    audio1_test = audio1_test[audio1_test.id != i]
    audio2_test = audio2_test[audio2_test.id != i]

'''

'''
audio1.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio1.csv")
#audio1_short.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio1_short.csv")
audio2.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio2.csv")
#audio2_short.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio2_short.csv")
#audio3.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio3.csv")
#audio4.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_audio4.csv")
audio1_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio1.csv")
#audio1_short_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio1_short.csv")
audio2_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio2.csv")
#audio2_short_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio2_short.csv")
#audio3_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio3.csv")
#audio4_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio4.csv")
'''
'''
audio3_short.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio3_short.csv")
audio3_short_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio3_short.csv")
audio4_short.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Test_Audio4_short.csv")
audio4_short_test.to_csv("/Users/miranda/PycharmProjects/pythonProject9/new_architecture/Train_Audio4_short.csv")'''
