# coding:utf-8
'''
import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
'''
#以下程序由chatgpt生成

import turtle
import random

# 设置窗口的大小和背景颜色
turtle.setup(500, 500)
turtle.bgcolor("black")

# 定义绘制火花的函数，包括颜色、形状、速度和移动方向
def draw_firework(x, y, color):
    firework = turtle.Turtle()
    firework.shape("circle")
    firework.shapesize(0.25)
    firework.color(color)
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    firework.speed("fastest")
    firework.right(random.randint(0, 360))
    firework.forward(random.randint(50, 150))
    firework.hideturtle()

# 定义主函数，循环绘制烟花
def main():
    while True:
        # 获取鼠标位置，并绘制烟花
        x, y = turtle.position()
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
        draw_firework(x, y, color)

# 调用主函数并启动事件循环
if __name__ == "__main__":
    main()
    turtle.done()

