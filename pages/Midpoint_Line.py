import streamlit as st
import matplotlib.pyplot as plt

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midpoint(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

   
    d  = dy - (dx/2)
    x = x1
    y = y1

#     print(f"x = {x}, y = {y}")
   
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
#         print(f"x = {x}, y = {y}")

    xMid = (x1 + x2)/2
    yMid = (y1 + y2)/2 
    
    st.plot(xcoordinates, ycoordinates)
    st.plot(xMid, yMid, 'ro')
    st.pyplot

def main():
    x1 = st.number_input("Enter the Starting point of x: ")
    y1 = st.number_input("Enter the Starting point of y: ")
    x2 = st.number_input("Enter the end point of x: ")
    y2 = st.number_input("Enter the end point of y: ")
    color = ".r"

    midpoint(x1, y1, x2, y2, color)


if __name__== "__main__":
    main()
