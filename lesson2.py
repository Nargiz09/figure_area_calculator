from area import cube, sphere
import triangle, circle, rectangle

while True:
    figure = int(input('0 - exit\n1 - sphere \n2 - cube \n3- circle \n4 - rectangle \n5 - triangle \nChoose a number: \n'))
    if figure == 0:
        break
    elif figure == 1:
        radius = float(input('Enter the radius of the sphere: '))
        print('The area of the rectangle: ', sphere.sphere_area(radius))
    elif figure == 2:
        side = float(input('Enter the side of the cube: '))
        print('The area of the triangle: ', cube.cube_area(side))
    elif figure == 3:
        radius = float(input('Enter the radius of the circle: '))
        print('The area of the circle: ', round(circle.circle_area(radius),2))
    elif figure == 4:
        a = float(input('Enter side 1 of the rectangle: '))
        b = float(input('Enter side 2 of the rectangle: '))
        print('The area of the rectangle: ', rectangle.rectangle_area(a, b))
    elif figure == 5:
        a = float(input('Enter the side of the triangle: '))
        h = float(input('Enter height of the rectangle: '))
        print('The area of the triangle: ', triangle.triangle_area(a, h))
    

