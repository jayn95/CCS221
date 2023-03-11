import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf

tf.compat.v1.disable_eager_execution()
#
def _plt_basic_object_(points):
    """Plots a basic object, assuming its convex and not too complex"""

    tri = Delaunay(points).convex_hull

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5)

    ax.set_zlabel("Z-Axis")
    ax.set_xlim3d(-10, 10)
    ax.set_ylim3d(-10, 10)
    ax.set_zlim3d(-10, 10)

    #Naming the Axis
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")

    #Graph title
    st.title("Diamond")
    st.pyplot(fig)

#shows/give points for cube (manipulate second method if you want to make other objects)
def _diamond_(bottom_lower=(0, 0, 0), side_length=3):
    """Create cube starting form the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)

    points = np.vstack([
        bottom_lower,
        bottom_lower + [-3, -3, 0], #P1 P1-P7 forms a 6 face pyramid  
        bottom_lower + [3, -3, 0], #P2
        bottom_lower + [3, 3, 0], #P3
        bottom_lower + [-3, 3, 0], #P4
        bottom_lower + [0, 0, -6], #P5
        bottom_lower + [-5, 0, 0], #P6
        bottom_lower + [5, 0, 0], #P7
        bottom_lower + [3, 2, 2], #P8
        bottom_lower + [-3, 2, 2], #P9
        bottom_lower + [3, -2, 2], #P10
        bottom_lower + [3, -2, 2], #P11
        bottom_lower + [-4, -2, 2], #P12
        bottom_lower + [4, -2, 2], #P13
        bottom_lower,
    ])

    return points

def translate_obj(points, amount):
    return tf.add(points, amount)

#points = cube, amount = what you want to manipulate
#tf.constant = numpy array, array, data type (float)
#when calling method from tensoflow call with session, close session to avoid problems after calling

init_cube_ = _diamond_(side_length=5)
points = tf.constant(init_cube_, dtype=tf.float32)

# _plt_basic_object_(init_cube_)

#Update the values here to move the cube around. x,y,z
translation_amount = tf.constant([0, 0, 0], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
    translated_cube = session.run(translated_object)

def main():

    _plt_basic_object_(translated_cube)

if __name__=='__main__':
    value = main()
    st.write(value)
