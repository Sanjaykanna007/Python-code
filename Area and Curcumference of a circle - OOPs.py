class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return circle.pi*self.radius*self.radius
    def circumference(self):
        return 2*circle.pi*self.radius
r=float(input("Enter radius of the circle: "))    
print("Radius: ",r)        
S=circle(r)
print("Area of the circle: ",S.area())
print("Circumference of the circle: ",S.circumference())

        
         
