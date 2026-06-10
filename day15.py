'''oops'''
'''classes and objects '''
# class Classy:
#     def method(self,par):
#         print("method",par)

# obj = Classy()
# obj.method(1)



# class Classy:
#     varia = 2 #variable is definedd 
#     def method(self):
#         print(self.varia, self.var)

# obj = Classy()
# obj.var = 3
# obj.method()

'''Constructors with Default Arguments'''
# class Classy:
#     def __init__(self, value = None):
#         self.var = value
# obj_1 = Classy("object")
# obj_2 = Classy()
# print(obj_1.var)  # Output: object
# print(obj_2.var)  # Output: None 






# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' in ' + self.galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)




'''inheriatnce'''
''' #two level inheritance'''
# # class Vehicle:
# #     pass
# # class LandVechile (Vehicle):
# #     pass
# # class TrackedVehicle (LandVehicle):
# #     pass



# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()






# class Super:
#     supVar = 1

# class Sub(Super):
#     subVar = 2

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)



# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub(Super):
#     def __init__(self):
#         super().__init__() #this line is important #parent ka constructor call nhi karenge toh kaam nhi karega 
#         self.subVar = 12

# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


'''three/Multi level inheritance'''
# class LevelL1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class LevelL2(LevelL1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()    #inheritance of level 1 in level 2
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class LevelL3 (LevelL2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = LevelL3()
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3()) 
