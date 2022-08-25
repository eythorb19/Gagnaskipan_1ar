
import pbor_class
from pbor_class import * 

def reassign(param):
    #param = [0,1]
    param = 1   #Í þessu tilviki hefur hvorugt áhrif á ytri breytuna var
    print("param: " + str(param))
 
def change(param):
    #param.append(1)
    param += 1  #Í þessu tilviki hefur hvorugt áhrif á ytri breytuna var
    print("param: " + str(param))


# var = [0]
# class_inst = pbor_class(var) #erum að senda vísun hér.

# print("var before reassign: " + str(var))
# class_inst.reassign()
# print("var after reassign: " + str(var))

# print("var before change: " + str(var))
# class_inst.change()
# print("var after change: " + str(var))


# "Keyrsla - class_inst.reassign()" 
# var before change: [0]
# inst_var before change: [0]
# inst_var after change: [0, 1]
# var after change: [0, 1]


#Keyrsla - class_inst.change()
# var before change: [0]
# inst_var before change: [0]
# inst_var after cchange: [0, 1]
# var after change: [0]




# var = [0]
# var2 = var
# var2.append(1)  #vísun í sömu breytu hjá var og var2 svo append hefur áhrif á bæði og var = var2 = [0,1]
# var2 = [3,4,5]  #Gildisveiting fer fram hér, búin að kúpla aðra breytinguna frá hinni
# var2.append(9)  #Kemur bara aftan á var2 

# print("var2 " + str(var2)) 
# print("var: " + str(var))

# var = 0
# print("var: " + str(var))
# reassign(var)
# print("var: " + str(var))
# change(var)
# print("var: " + str(var))

