import numpy as np
import random
import math
from csv import writer

q1 = np.random.randint(-141,51)
q2 = np.random.randint(-123,60)
q3 = np.random.randint(-173,173)
q4 = np.random.randint(-3,150)
q5 = np.random.randint(-175,175)
q6 = np.random.randint(-90,120)
q7 = np.random.randint(-175,175)

x1 = math.cos(q1)
y1 = math.sin(q1)

x2 = math.cos(q2)
y2 = math.sin(q2)

x3 = math.cos(q3)
y3 = math.sin(q3)

x4 = math.cos(q4)
y4 = math.sin(q4)

x5 = math.cos(q5)
y5 = math.sin(q5)

x6 = math.cos(q6)
y6 = math.sin(q6)

x7 = math.cos(q7)
y7 = math.sin(q7)


# rows,columns = (4,4)

mat1 = np.array([[x1,-y1,0,0],
                [y1,x1,0,0],
                [0,0,1,0],
                [0,0,0,1]])
# print(mat1)

mat2 = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0.27],
                [0,0,0,1]])
# print(mat1)

mat3 = np.array([[1,0,0,0.069],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])

#print(mat1)

mat4 = np.array([[1,0,0,0],
                [0,math.cos(-90),-math.sin(-90),0],
                [0,math.sin(-90),math.cos(-90),0],
                [0,0,0,1]])

# print(mat4)

#mat5 = np.array([[],[],[],[]])
mat5 = np.array([[x2,-y2,0,0],
                [y2,x2,0,0],
                [0,0,1,0],
                [0,0,0,1]])
# print(mat5)

mat6 = np.array([[1,0,0,0],
                [0,math.cos(90),-math.sin(90),0],
                [0,math.sin(90),math.cos(90),0],
                [0,0,0,1]])

mat7 = np.array([[x3,-y3,0,0],
                [y3,x3,0,0],
                [0,0,1,0],
                [0,0,0,1]])
# print(mat7)

mat8 = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0.364],
                [0,0,0,1]])

# print(mat8)

mat9 = np.array([[1,0,0,0.069],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])

mat10 = np.array([[1,0,0,0],
                [0,math.cos(-90),-math.sin(-90),0],
                [0,math.sin(-90),math.cos(-90),0],
                [0,0,0,1]])

# print(mat10)

mat11 = np.array([[x4,-y4,0,0],
                [y4,x4,0,0],
                [0,0,1,0],
                [0,0,0,1]])

# print(mat11)

mat12 = np.array([[1,0,0,0],
                [0,math.cos(90),-math.sin(90),0],
                [0,math.sin(90),math.cos(90),0],
                [0,0,0,1]])

# print(mat12)

mat13 = np.array([[x5,-y5,0,0],
                [y5,x5,0,0],
                [0,0,1,0],
                [0,0,0,1]])

# print(mat13)

mat14 = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0.374],
                [0,0,0,1]])

# print(mat14)

mat15 = np.array([[1,0,0,0.01],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])

# print(mat15)

mat16 = np.array([[1,0,0,0],
                [0,math.cos(-90),-math.sin(-90),0],
                [0,math.sin(-90),math.cos(-90),0],
                [0,0,0,1]])

# print(mat16)


mat17 = np.array([[x6,-y6,0,0],
                [y6,x6,0,0],
                [0,0,1,0],
                [0,0,0,1]])

# print(mat17)

mat18 = np.array([[1,0,0,0],
                [0,math.cos(90),-math.sin(90),0],
                [0,math.sin(90),math.cos(90),0],
                [0,0,0,1]])

# print(mat18)

mat19 = np.array([[x7,-y7,0,0],
                [y7,x7,0,0],
                [0,0,1,0],
                [0,0,0,1]])

# print(mat19)

mat20 = np.array([[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0.28],
                [0,0,0,1]])

# print(mat20)

a = mat1@mat2
b = a@mat3
c = b@mat4
d = c@mat5
e = d@mat6
f = e@mat7
g = f@mat8
h = g@mat9
i = h@mat10
j = i@mat11
k = j@mat12
l = k@mat13
m = l@mat14
n = m@mat15
o = n@mat16
p = o@mat17
q = p@mat18
r = q@mat19
trans = r@mat20

#print(trans)

x = round(trans[0][3],3)
y = round(trans[1][3],3)
z = round(trans[2][3],3)
print("q1 =",q1,"q2 = ",q2,"q3 =",q3,"q4 = ",q4,"q5 = ",q5,"q6 = ",q6,"q7 = ",q7)
print("x = ",x,"y = ",y,"z = ",z)