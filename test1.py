#字符，运算，数学函数
message='hello'
n=17
pi=3.141592653589793
print(message,n,pi)
print(40+2)
print(6**2 + 7) # 双* 为乘方运算

first = 'throat'
second = 'warbler'
print(first + second); #加号运算符 + 可用于 字符串拼接（string concatenation）
print('Spam'*3) #乘法运算符* 也可应用于字符串；它执行重复运算。 例如，'Spam'*3的结果是'SpamSpamSpam'。 

#print('Spam'*'12')  此处是不合法的，如果其中一个运算数是字符串，则另外一个必须是整型,即不能是'12'。

print('hao'+str(n))

print(int(3.99999))  #结果为3 不四舍五入
print(int(-2.3))     #结果为-2 不四舍五入
print(float('3.14159'))
print(float(31))     #结果为31.0

#下面语句会报错：TypeError: unsupported operand type(s) for +: 'float' and 'str'
#print(float(32)+'3.14159')
#将float数值转型 为str即可
print(str(float(32))+'3.14159')

import math #此处若没import，会报错 undefined variable:math
degrees = 45
radians = degrees / 180 * math.pi
print(radians)
print(math.sqrt(2)) #1.4142135623730951

x = math.sin(degrees / 360.0 * 2 * math.pi)
print('x begin:'+str(x))
x = math.exp(math.log(x+1))
print('x after:'+str(x))
