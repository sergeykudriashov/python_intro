lis = [100,200,300,'test']
lis[1] = 500
print(lis[1])
lis.append(700)
print(lis[4])

tpl =(100,200,300,'test')
# tpl[1] = 500 -- impossible
# tpl.append(700) -- impossible
print(tpl[1])

anothertpl = tuple("hello")
print(anothertpl[4])
print(anothertpl)

dict = { "key1" : "value1", "key2" : "value2" }
dict['key1'] = 'test'
print(dict['key1'])
print(dict)