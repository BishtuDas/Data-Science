import math;

def circle(radius):
    area = math.pi*(radius**2)
    cricuference = 2*math.pi*radius
    diameter = 2*radius;

    return area,cricuference,diameter

    if __name__ == '__main__':
      r = input("entre your redious")
      r = float(r)

      area,c , d = circle(r)
      print(f"area {area},cricuference{c},diameter{d}")