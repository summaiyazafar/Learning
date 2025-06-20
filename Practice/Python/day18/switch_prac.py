# day = 8
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("Friday")
#     case 5:
#         print("Thursday") 
#     case 6:
#         print("Saturday")        
#     case 7:
#         print("Sunday")
#     case 8:
#         print("No will be print")

# status=400
# def myfunc(status):
#     match status:
#         case 340:
#             return "Something will be happen."
#         case 380|400:
#             return "Something will not b e happen."
#         case 420|440:
#             return "Don't use bad languag."
#         case 480|500:
#             return "default value."
# gull=myfunc(status)
# if gull is not None:
#     print(gull)
# point=(3, 7)
# match point:
#     case (0, 0):
#         print("Origin")
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#     case (x, y):
#         print(f"X={x}, Y={y}")

# class point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     def myfunc(self):
#         match self:
#             case point (x=0, y=1):
#                 print("no")
#             case point(x=2, y=0):
#                 print("yes")
#             case point(x=x, y=y):
#                 print("s")
# result=point(1,6)
# result.myfunc()

class Point:
    __match_args__ = ('x', 'y')  # Match ke liye x aur y use honge

    def __init__(self, x, y):
        self.x = x
        self.y = y
points = [Point(0, 0), Point(0, 5)]  # is list ko match karna hai
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
point = Point(3, 3)  # is point ko match karna hai
match point:
    case Point(x, y) if x == y:
        print(f"Y = X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal, X = {x}, Y = {y}")

class point:
    __match__args__ = ("x","y")
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
points =[points(0,0), points(0,5)]

















