import streamlit as st
import matplotlib.pyplot as plt

plt.title("Bresenham Line and its Midpoint")
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
#     print(f"x = {x}, y = {y}")
    
    xcoordinates = [x]
    ycoordinates = [y]
    
    #midpoint
    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2 
    plt.plot(xMid, yMid, 'ro')

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        
#         print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)
    
    plt.plot(xcoordinates, ycoordinates)
    st.pyplot(plt)
    
def main():
    x1 = st.number_input("Enter the Starting point of x: ", min_value=0, max_value=1000, value=0)
    y1 = st.number_input("Enter the Starting point of y: ", min_value=0, max_value=1000, value=0)
    x2 = st.number_input("Enter the end point of x: ", min_value=0, max_value=1000, value=0)
    y2 = st.number_input("Enter the end point of y: ", min_value=0, max_value=1000, value=0)
    color = ".r"

    bres(x1, y1, x2, y2)


if __name__== "__main__":
    main()
