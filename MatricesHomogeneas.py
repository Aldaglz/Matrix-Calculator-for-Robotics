'''Desarrollado por: Aldair Gonzalez Leyva'''

'''
rotar x 45
rotar  y 30
rotar z 60
traslacion 2, -1, 3

3,2,5 vector original

'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys

#Función para graficar vectores
def plot_vector(p, label, color):
    ax.quiver(0, 0, 0, p[0],p[1],p[2], color=color, label=label)

#Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#111 means 1 row, 1 column, and it's the 1st subplot

ax.set_xlim([-25,25])
ax.set_ylim([-25,25])
ax.set_zlim([-25,25])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()


#Función para rotación en eje X
def rotacion_X(Angle):
    angulo=np.radians(Angle)
    
    sin=np.sin(angulo)
    cos=np.cos(angulo)

    Rot_X= np.array([
        [1,0,0,0],
        [0,cos,-1*sin,0], 
        [0,sin,cos,0], 
        [0,0,0,1], 
    ])
    return Rot_X

#Función para rotación en eje Y
def rotacion_Y(Angle):
    angulo=np.radians(Angle)

    sin=np.sin(angulo)
    cos=np.cos(angulo)

    Rot_Y=np.array([
        [cos, 0, sin,0],
        [0,1,0,0], 
        [-1*sin,0,cos,0], 
        [0,0,0,1],
    ])
    return Rot_Y

#Función para rotación en eje Z
def rotacion_Z(Angle):
    angulo=np.radians(Angle)
    
    sin=np.sin(angulo)
    cos=np.cos(angulo)

    Rot_Z=np.array([
        [cos,-1*sin,0,0],
        [sin,cos,0,0], 
        [0,0,1,0], 
        [0,0,0,1], 
    ])
    return Rot_Z

#Función para desplazamiento
def traslacion(x,y,z):
    trans=np.array([
        [1,0,0,x],
        [0,1,0,y],
        [0,0,1,z],
        [0,0,0,1],
    ])
    return trans

#Función para capturar los valores del vector a afecta
def vector_OG(x,y,z):
    Vector=np.array([
        [x],
        [y],
        [z],
        [1],
    ])
    return Vector

#----------------------------------------------Codigo principal----------------------------------------------

#Valores iniciales para las matrices ingresadas por el usuario
rotacion_Valor = 0 
traslacion_Valor = 0
vector_Valor = 0

#Counter
n=0

#Colors2vectors
colors=["blue","red","yellow","Green","black"]

#Estado inicial de la decisión final
Finaldecision=0

while True:   

    #Selección de rotacion 
    choice = int(input("¿Hacia donde rotará? \n #1.- Rotar en X \n #2.- Rotar en Y \n #3.- Rotar en Z \n #4.- Solo trasladar\n\n"))
    if choice == 1:
        ang = int(input("Ingresa el angulo para rotacion en X: "))    
        rotacion_Valor=rotacion_X(ang)
    if choice == 2:
        ang = int(input("Ingresa el angulo para rotacion en Y: "))    
        rotacion_Valor=rotacion_Y(ang)
    if choice == 3:
        ang = int(input("Ingresa el angulo para rotacion en Z: "))    
        rotacion_Valor=rotacion_Z(ang)
    if choice == 4:    
        rotacion_Valor=traslacion(0,0,0) #Se utiliza aquí la función de traslación para crear una matriz
                                        #de identidad que multiplicará al vector de desplazamiento.

    print("\n NOTA: Sí solo rotará, ingrese 0 en cada componente del desplazamiento\n ")
    Xt = float(input("Ingresa el componente X de desplazamiento: "))
    Yt = float(input("Ingresa el componente Y de desplazamiento: "))
    Zt = float(input("Ingresa el componente Z de desplazamiento: "))

    traslacion_Valor=traslacion(Xt, Yt, Zt)
    
    #Componentes del vector a afectar
    if(Finaldecision!=1):
        Xv = float(input("Ingresa el componente X de tu vector: "))
        Yv = float(input("Ingresa el componente Y de tu vector: "))
        Zv = float(input("Ingresa el componente Z de tu vector: "))
    
        vector_Valor=vector_OG(Xv, Yv, Zv) 

    #Calculo de matriz homogenea
    MatrizHomogenea=traslacion_Valor@rotacion_Valor
    print("\nMatriz Homogenea: \n ",MatrizHomogenea)

    #Resultado
    MatrizFinal=MatrizHomogenea@vector_Valor

    print("\nMatriz Resultante: \n",MatrizFinal)
    
    #Agrgar al plot
    plot_vector(MatrizFinal, "Vector", colors[n]) 
    n=n+1

    Finaldecision = int(input("¿Qué quieres hacer ahora? \n #1.- Realizar más movimientos \n #2.- Probar otra matriz \n #3.- Mostrar gráfica \n #4.- Salir \n\n"))

    if(Finaldecision==4):
        sys.exit() #Detiene programa
    else:            
        if(Finaldecision==1):#Continua con mas movimientos con la matriz
            vector_Valor = MatrizFinal    
        elif(Finaldecision==2):#Prueba una nueva matriz
            rotacion_Valor = 0 
            traslacion_Valor = 0
            vector_Valor = 0
            n=0
        elif(Finaldecision==3):#Grafica la resultante  
            plt.show()



    







