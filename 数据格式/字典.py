#字典类型
#创建字典
#空字典
var = dict()
print(var,type(var))
var = {}
print(var,type(var))

#创建具有多个数据的字典
#1.
var = {'黑':'black','白':'white','蓝':'blue'}
print(var,type(var))
#2.
var = dict({'黑':'black','白':'white','蓝':'blue'})
print(var,type(var))
#3.
var = dict(黑 = 'black',白 = 'white',蓝 = 'blue')
print(var,type(var))
#4.
var = [
   ['黑','black'],
   ['白','white'],
   ['蓝','blue']
   ]
result = dict(var)
print(result,type(result))
#5.
keys = ['黑','白','蓝']
values = ['black','white','blue']
result = dict(zip(keys,values))
print(result,type(result))
#元素 -> 键值对 -> 键+值
#基本操作
var = {'赵云':'子龙','庞统':'士元','郭嘉':'奉孝','鲁肃':'子敬'}
#访问字典:
print(var['赵云'])
#修改字典
var['郭嘉'] = '天妒'
print(var)
#删除元素
del var['郭嘉']
print(var)
#添加元素
var['周瑜'] = '公瑾'
print(var)
#序列操作
#成员检测 ->针对于键的操作而不是值
var = {'赵云':'子龙','庞统':'士元','郭嘉':'奉孝','鲁肃':'子敬'}
result = '士元' in var
print(result)
#len()  检测字典中元素的个数
var =  {'赵云':'子龙','庞统':'士元','郭嘉':'奉孝','鲁肃':'子敬'}
result = len(var)
print(result)
#max()  获取字典中最大的键如果不是数字键 获取最大编码的值
var = {'a':1,'b':2,'c':3,'d':12}
result = max(var)
print(result)
#min() 获取字典中最小的键如果不是数字键 获取最小编码的值
var = {'a':1,'b':2,'c':3,'d':12}
result = min(var)
print(result)
#字典的遍历
var = {'赵云':'子龙','庞统':'士元','郭嘉':'奉孝','鲁肃':'子敬'}
#方法1:先遍历键,再使用变量和键来获取对应的值
for i in var:
    print(i,var[i])
#方法2:同时遍历键和值
result = var.items()
print(result,type(result))#不是标准的列表类型
for k,v in var.items():
    print(k,v)
#字典相关函数
var = {'孙行者':'孙悟空','沙和尚':'沙悟净','猪八戒':'猪悟能'}
#clear 清空字典
var.clear()
print(var,id(var))
#copy() 复制字典
newvar = var.copy()
print(newvar,id(newvar))
#get()  获取字典中指定键的值
result = var.get('猪八戒','默认值')#result =var['猪八戒']
print(result)
#pop()  删除字典中指定的元素
result = var.pop('唐僧')
print(var)
print(result)
#popitem()  随机删除字典中的一个元素
result = var.popitem()
print(var)
print(result)
#keys()  获取字典中的所有键组成的容器
var = {'苹果':'Apple','梨':'pear'}
result = var.keys()
print(result)
for i in result:
    print(i)
#values()  获取字典中的所以值组成的容器
result = var.values()
print(result)
#items()  获取字典中的所有键和值组成的2级容器
result = var.items()
print(result)