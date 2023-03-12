import streamlit as st
import matplotlib.pyplot as plt

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
#         fig = plt.plot(int(x1), int(y1), color)
        fig, ax = plt.subplots(x1, y1, figsize=(8, 10). tight_layout=True)
        ax.plot(x1, y1)
        x1 += Xinc
        y1 += Yinc
        
        #scatter plot
        ax[2].scatter(x=[80, 85, 90], y=[85, 90, 95], c='g', label='Multiple Points')
        
        return fig
        
#         st.pyplot(fig=None, clear_figure=None, **kwargs)
#     result = non_optional_func(*args, **kwargs)
#     fig.savefig(image, **kwargs)


# def main():
x1 = st.number_input("Enter the Starting point of x: ")
y1 = st.number_input("Enter the Starting point of y: ")
x2 = st.number_input("Enter the end point of x: ")
y2 = st.number_input("Enter the end point of y: ")
color = ".r"

# value = DDALine(x1, y1, x2, y2, color)
# st.write(DDALine(x1, y1, x2, y2, color))

st.pyplot(DDALine(x1, y1, x2, y2, color))
