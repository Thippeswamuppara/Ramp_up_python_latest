import math

class Shape:
    def calculate_area(self, *args):
        print("No shapes and length of argumets is matched")
        return 0

class Rectangle(Shape):
    def calculate_area(self, *args):
        if len(args)==2:

            return f"the rectangle area value is {args[0] *args[1]}"
        else:
            return super().calculate_area(*args)

class Triangle(Rectangle):
    def calculate_area(self, *args):
        if len(args)==3 and 'triangle' in args:

            return f"the triangle area value is {0.5 * base * height}"
        else:
            return super().calculate_area(*args)

class Circle(Triangle):
    def calculate_area(self, *args):
        if  len(args)==1:


            return math.pi * (args[0] ** 2)
        else:
            return super().calculate_area(*args)
C=Circle()


try:
    length_of_arguments = int(input("give value for length of arguments which should less than or equal to 3 \t"))
    if length_of_arguments<=3 and length_of_arguments>=1:
        if length_of_arguments==1:
            print("you are calling Circle method")
            radius = float(input("enter a radius value"))
            print(C.calculate_area(radius))
        elif length_of_arguments == 2:
            print("you are calling Rectangle method")
            length = float(input("enter length value of the rectangle"))
            width = float(input("enter width value of the rectangle"))
            print(C.calculate_area(length,width))
        elif length_of_arguments == 3:
            print("you are calling Triangle method")
            base = float(input("enter base value of  Triangle"))
            height = float(input("enter height value of  Triangle"))
            shape=input("enter 'triangle' word ").lower()
            print(C.calculate_area(base,height,shape))
    else:
        print("please give proper input")
except:
    print("please ensure about what you given instead of requirement")