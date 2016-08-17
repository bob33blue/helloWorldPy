#接口设计
import turtle
bob = turtle.Turtle()
print(bob)

for i in range(4):
    bob.fd(100)
    bob.lt(90)
    
#fd 方法的实参是像素距离
#Turtle 对象中你能调用的其他方法还包括：让它向后走的 bk ，向左转的 lt ，向右转的 rt 。 lt 和 rt 这两个方法接受的实参是角度。
#mainloop 告诉窗口等待用户操作，尽管在这个例子中，用户除了关闭窗口之外，并没有其他可做的事情。
#turtle.mainloop()   #此处在liclipse里会报编译错，但新建脚本用python命令是可以执行的

for i in range(4):
    print('Hello!')