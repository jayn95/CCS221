import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[0,0,0], [0,0,0],[0,0,0]])

def change(x, y, ColorVal, MoveDirection):
    if MoveDirection == 'u':
        two_d_arr[x][y] = ColorVal
        if x > 0:
            change(x-1, y, ColorVal, MoveDirection)
    elif MoveDirection == 'd':
        two_d_arr[x][y] = ColorVal
        if x < two_d_arr.shape[0]-1:
            change(x+1, y, ColorVal, MoveDirection)
    elif MoveDirection == 'r':
        two_d_arr[x][y] = ColorVal
        if y > 0:
            change(x, y-1, ColorVal, MoveDirection)
    elif MoveDirection == 'l':
        two_d_arr[x][y] = ColorVal
        if y < two_d_arr.shape[1]-1:
            change(x, y+1, ColorVal, MoveDirection)
    else:
        print('Please Try again')
    
    img = plt.imshow(two_d_arr, interpolation='none', cmap='plasma')
    img.set_clim([0,80])
    plt.colorbar()
    plt.show()

def main():
    x_coord = int(input("Enter X coordinate:"))
    y_coord = int(input("Enter Y coordinate:"))
    ColorVal = int(input("Select a Color Value (0-80)"))
    MoveDirection = input("Direction (u for up, d for down, l for left, or r for right):")
    change(x_coord, y_coord, ColorVal, MoveDirection)

main()