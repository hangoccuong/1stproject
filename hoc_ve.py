#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#bước 1: import modune
import turtle
#bước 2: tạo đối tượng
tl= turtle.Turtle()
tl.shape('turtle')
# cỡ bút
tl.pensize(1)
# màu của bút
tl.pencolor('#808000')
# tốc độ chuột
tl.speed(1)
# điền mầu
tl.fillcolor('blue')
#bước 3: điều khiển
tl.begin_fill() # bắt đầu tô mầu
tl.forward(200) # tiến lên trước 200 pixel
tl.right(90) # sang phải 90 pixel
tl.backward(100) # quay lại 200 pixel
tl.right(90) #sang phải 90 pixel
tl.forward(200) # tiến lên 200
tl.left(90) # sang trái 90
tl.forward(100) # tiến lên 200
tl.end_fill() #kết thúc tô màu
tl.penup() # nhấc bút lên
tl.forward(50)
tl.pendown() # đặt bút xuống
tl.fillcolor("yellow")
tl.begin_fill()
tl.circle(50)
tl.end_fill()
tl.penup()
tl.right(200)
turtle.done()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




