import numpy as ty
a = ty.sin(ty.pi/2)
print(a)

b = ty.array([ty.pi/2, ty.pi/3, ty.pi/4, ty.pi/5])
c = ty.sin(b)
print(c)

#convert Degrees Into Radians
d = ty.array([90, 180, 270, 360])
e = ty.deg2rad(d)
print(e)

# Radians to Degrees
f = ty.array([ty.pi/2, ty.pi, 1.5*ty.pi, 2*ty.pi])
g = ty.rad2deg(f)
print(g)

#Finding Angles
h = ty.arcsin(1.0)
print(h)

# Angles of Each Value in arrays
i = ty.array([1, -1, 0.1])
j = ty.arcsin(i)
print(j)

# Hypotenues
k = 3
l = 4

m = ty.hypot(k, l)
print(m)