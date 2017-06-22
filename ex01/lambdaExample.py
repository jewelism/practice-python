print "lambda---------"
print filter(lambda x:x%2==0, range(10))
print reduce(lambda x,y:y+x,[0,1,2,3])
print

print "String---------"
x = 'boseokba'
print x[0]
print x[1:3]
print x[:4]
print x[4:]

print "list---------"
list = [2,3,7,11]

list.append(5)
print list

list.sort()
print list

del list[0]
print list

list[0] = 2
print list

list2 = ["boseok",["ku","ku2","ku3"],"boseok2"]
print list2
print list2[1]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print matrix

print "tuple-----------"

def tupletest(a,*test):
    print a, test

tupletest(1,'boseok',1,'kusob',2)

empty = ()
print empty

one = 5,
print one

del list
p = (1,2,3)
q = list(p) ### tuple->list
print p,q

q.append(4)
print q

p = tuple(q) ### list->tuple
print p

print "dictionary------------"

dic = {}
dic['boseok'] = 'boseok is incredible'
dic['python'] = 'python is funny'
print dic
print dic['python']

del dic['python']
print dic

dic['python'] = 'python is incredible'
dic['kusob'] = 'incredible programmer'
print dic

print dic.keys()
print dic.values()

print 'python' in dic, 'mac' in dic
