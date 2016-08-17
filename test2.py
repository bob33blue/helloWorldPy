#自定义函数

##函数定义的第一行被称作函数头（header）； 其余部分被称作函数体（body）。 函数头必须以冒号结尾，而函数体必须缩进。 按照惯例，缩进总是4个空格。 函数体能包含任意条语句。
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
    
#打印语句中的字符串被括在双引号中。单引号和双引号的作用相同；大多数人使用单引号，上述代码中的情况除外，即单引号（同时也是撇号）出现在字符串中时。

print(print_lyrics)       #<function print_lyrics at 0x00000000005C8F28>
print(type(print_lyrics)) #<class 'function'>

#函数的调用
print_lyrics()

#也可以定义另一个函数，来调用上面那个函数
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
print("now let's beign repeat:\n")
repeat_lyrics()

def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('Spam'*4)

result = print_twice('Bing') #会打印2次Bing
print(result)                #打印结果为"None"，因为函数print_twice无返回值

#None 这个值和字符串'None'不同。这是一个自己有独立类型的特殊值：
print(type(None))        #<class 'NoneType'>
print(type('None'))      #<class 'str'>

print(len('None'))       #4 字符串长度为4

def kuang():
    print('+'+'-'*4+'+'+'-'*4+'+')
def shu():
    print('|'+' '*4+'|'+' '*4+'|')
    print('|'+' '*4+'|'+' '*4+'|')
    print('|'+' '*4+'|'+' '*4+'|')
    print('|'+' '*4+'|'+' '*4+'|')
kuang()
shu()
kuang()
shu()
kuang()
#print('\n+', '-')

#print默认是换行的，可以加end，阻止换行，例如 以下2条语句打印结果为："+,-"，中间用逗号分隔
print('+', end=',')
print('-')