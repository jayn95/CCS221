import matplotlib.pyplot as plt

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1,y1,x2,y2):
    
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    print(f"x = {x}, y = {y}")
    
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        
        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2 
    
    plt.plot(xcoordinates, ycoordinates)
    plt.plot(xMid, yMid, 'ro')
    plt.show()

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1 
    dy = y2 - y1

    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2 

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc

    
    plt.plot(xMid, yMid, 'bo')
    plt.show()


def midpoint(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

   
    d  = dy - (dx/2)
    x = x1
    y = y1

    print(f"x = {x}, y = {y}")
   
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
 
        if (d<0):
            d = d + dy

    
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        print(f"x = {x}, y = {y}")

    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2 
    
    plt.plot(xcoordinates, ycoordinates)
    plt.plot(xMid, yMid, 'ro')
    plt.show()

def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))
    color = ".r"

    bres(x1, y1, x2, y2)
    DDALine(x1, y1, x2, y2, color)
    midpoint(x1, y1, x2, y2, color)


if __name__== "__main__":
    main()
