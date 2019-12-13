class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
      def __init__(self, a, b, c):
          self.a = a
          self.b = b
          self.c = c
class Circle:
    def __init__(self, centre_x, centre_y, radius):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.radius = radius


def findMirrorPoint(p, l):
    p.x = (-2*l.a*(l.a*(p.x) + l.b*(p.y) + l.c)//((l.a**2) + (l.b**2))) + p.x
    p.y = (-2*l.b*(l.a*(p.x) + l.b*(p.y) + l.c)//((l.a**2) + (l.b**2))) + p.y
    return (p.x, p.y)


def Checksides(p1, p2, l1, l2):
          findMirrorPoint(p1, l1)
          t1 = (l2.a)*(p2.x) + (l2.b)*(p2.y) + (l2.c)
          t2 = (l2.a)*(p1.x) + (l2.b)*(p1.y) + (l2.c)
          if t1 > t2 or t2 > t1:
              return "Both are on same side"
          else:
              return "Not on same side"
          
def checkIntersection(c1, c2):
    distance_between_centres = (((c1.centre_y) - (c2.centre_y))**2 + ((c1.centre_x) - (c2.centre_x))**2 )**0.5
    sum_of_radii = c1.radius + c2.radius
    dif_of_radii = abs(c1.radius - c2.radius)
    if sum_of_radii < distance_between_centres:
        return "The circles do not intersect"
    else:
        return "The circles intersect"


p = Point(1, 0)
l = Line(-1, 1, 0)
p1= Point(-2, 0)
p2 = Point(-1, 1)
l1 = Line(-1, 1, 0)
l2 = Line(-2, 1, -1)
c1 = Circle(-2, 0, 3)
c2 = Circle(4, 0, 3)
print(checkIntersection(c1, c2)) 
   
