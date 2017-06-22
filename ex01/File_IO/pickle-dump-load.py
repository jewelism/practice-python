# -*- coding: utf-8 -*-
users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
import os
path = os.getcwd()+'/pickle.txt'
f = open(path, 'w')
print 'Path : '+path
import pickle
pickle.dump(users, f)
f.close()

f = open(path)
user = pickle.load(f)
print user

