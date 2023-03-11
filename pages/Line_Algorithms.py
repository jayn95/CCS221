import streamlit as st
import matplotlib.pyplot as plt

# st.title("Bresenham Algorithm")
# # plt.xlabel("X Axis")
# # plt.ylabel("Y Axis")

# def bres(x1,y1,x2,y2):
#     x,y = x1,y1
#     st.write(x, y)
#     dx = abs(x2 - x1)
#     st.write(dx)
#     dy = abs(y2 -y1)
#     st.write(dy)
#     gradient = dy/float(dx)
#     st.write(gradient)

#     if gradient > 1:
#         dx, dy = dy, dx
#         st.write(dx, dy)
#         x, y = y, x
#         st.write(x, y)
#         x1, y1 = y1, x1
#         st.write(x1, y1)
#         x2, y2 = y2, x2
#         st.write(x2, y2)

#     p = 2*dy - dx
#     st.write(p)
#     st.write(f"x = {x}, y = {y}")
#     # Initialize the plotting points
#     xcoordinates = [x]
#     ycoordinates = [y]

#     for k in range(2, dx + 2):
#         if p > 0:
#             y = y + 1 if y < y2 else y - 1
#             p = p + 2 * (dy - dx)
#         else:
#             p = p + 2 * dy

#         x = x + 1 if x < x2 else x - 1

#         print(f"x = {x}, y = {y}")
#         xcoordinates.append(x)
#         ycoordinates.append(y)


#     fig = plt.plot(xcoordinates, ycoordinates)
#     st.pyplot(fig)

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
#     st.write(dx)
    dy = y2 - y1
#     st.write(dy)
    st.write(x2)
    st.write(y2)

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
#     st.write(steps)

    Xinc = float(dx / steps)
#     st.write(Xinc)
    Yinc = float(dy / steps)
#     st.write(Yinc)

    for i in range(0, int(steps + 1)):
        fig = plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
        st.write(x1)
        st.write(y1)
    st.pyplot(fig)


# def main():
x1 = st.number_input("Enter the Starting point of x: ")
y1 = st.number_input("Enter the Starting point of y: ")
x2 = st.number_input("Enter the end point of x: ")
y2 = st.number_input("Enter the end point of y: ")
color = ".r"
# st.write(color)

DDALine(x1, y1, x2, y2, color)
value = DDALine(x1, y1, x2, y2, color)
st.write(value)

#     bres(x1, y1, x2, y2)
    # midpoint(x1, y1, x2, y2)


# if __name__ == "__main__":
# main()


