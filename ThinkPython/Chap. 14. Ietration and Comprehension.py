
# Iterable object and Iterator object.

L = [1,2,3,4,5]

for item in L:
	print ('item : %d' % item)
	
	
iterator = iter(L)
print ('Item :%d' % next(iterator))
print ('Item :%d' % next(iterator))

# Manual Iteration

I = iter(L)
while True:
	try:
		x = next(I)
	except StopIteration:
		break
	print ('item : %d' % x)


d = dict(a=1, b=2, c=3)
I = iter(d)
while True:
	try:
		x = next(I)
	except StopIteration:
		break
	print 'dict key: %c' % x
	
I = iter(d.items())
while True:
	try:
		x,y = next(I)
	except StopIteration:
		break
	print 'dict d[%c]:  %d' % (x, y)

#range : manual iteration

for i in range(5):
	print i
	
i = range(5)
it = iter(i)

while True:
	try:
		d = next(it)
	except StopIteration:
		break
	print d
	
# list Comprehension 
l = [1,2,3,4,5]
for i in range(len(l)):
	l[i] += 10
print l
l = [1,2,3,4,5]
l = [i+10 for i in l]
print l


# list comprehension on files
f = open('data2.txt')
lines = f.readlines()
print lines
##
line = [line.rstrip() for line in lines ]
print line
print line[0]

## another comprehension
res=[]
for line in open('data2.txt'):
	if line[0] ==  '(':
		res.append(line.rstrip())
print res

## nested for loop

l = [x+y for x in 'abc' for y in '123']
print l

## 
print (sorted(open('data2.txt')))

print (list(enumerate(open('data2.txt'))))

print (tuple(open('data2.txt')))

## unpack by *

def pr(a,b,c,d): print(a,b,c,d)

pr(1,2,3,4)
#unpack list into argument
pr(*[1,2,3,4])

pr(*open('data3.txt'))

#unzip zipped list
x = ('a','b')
y = (1,2)

l = list(zip(x,y))
print l

print (zip(*l))
print (zip(*zip(x,y)))

# Range Iterable
r = range(10)
print ('range r :',r)
# next(r) ; error

ir = iter(r)
print ('next iterable value : next(ir): %d, next(ir) :%d' % \
       (next(ir),next(ir)))

print ('length of r : %d' % len(r)) # len(ir) : error

#map

m = map(abs, (-1, 0, 1))
print m

# 3.x 
# print ('map next value : %d %d %d' % (next(m), next(m), next(m)))
# 2.x : error


# iterable zip : automatically, manually

z = zip((1,2,3), (10,20,30))
print z
for pair in z: print pair   # exhausted after one pass


# multiple and single pass iterator 
r = range(10)

I1 = iter(r)

print (next(I1), next(I1))

I2 = iter(r)  ## Two iterators in one range
print (next(I2))


# 3.x zip map filter do not support multiple active iterators
z = zip(('x', 'y', 'z'), (1,2,3))
I1 = iter(z)
print (next(I1))
I2= iter(z)
print (next(I2))

# iterator with dictionary

d = dict(a=1, b=2, c=3)
k = d.keys()
print (k, k[0]) ## in 3.x, does not support indexing. because k is dict_key object, not a list
print (list(k), list(k)[0]) ## in 3.x, dict_key object must force to change to list

v = d.values()
print (v, v[0]) # in 3.x, dict_value object is not list
print (list(v), list(v)[0])

for k, v in d.items(): print ('{%c %d}' % (k, v))

iterd = iter(d)  ## iter(dictionary) ? = iteration with keys !!
## dictiionary iteration => return next key with each iteration

print ('iterable dict %c %c %c' % (next(iterd), next(iterd), next(iterd)))

for k in d: print ('iterable dict %c' % k)
for k in sorted(d): print ('sorted iterable dict %c', k)



