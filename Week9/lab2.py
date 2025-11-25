def square(point1,point2):
  """
  square 的 计算重合的面积
  
  :param point1: (左上角横坐标，左上角纵坐标，右下角横坐标，右下角纵坐标 )
  :param point2: (左上角横坐标，左上角纵坐标，右下角横坐标，右下角纵坐标 )
  """
  x1_max=max(point1[0],point2[0])
  y1_max=max(point1[1],point2[1])
  x2_min=min(point1[2],point2[2])
  y2_min=min(point1[3],point2[3])
  #计算宽和高
  width=x2_min - x1_max
  height=y1_max - y2_min
  #计算面积
  if width <= 0 or height <= 0:
        return 0
  else:
        return width * height

r1 = (0, 0, 4, 4)
r2 = (2, 2, 6, 6)
print(f"交叉面积: {square(r1, r2)}")

