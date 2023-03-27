import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class Linea:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def getLongitud(self):
        x1, y1 = self.punto1.get_x(), self.punto1.get_y()
        x2, y2 = self.punto2.get_x(), self.punto2.get_y()
        longitud = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return longitud
    
    def __str__(self):
        return f"Linea que une los puntos {self.punto1} y {self.punto2}"

class Poligono:
    def __init__(self, vertices):
        self.vertices = vertices
    
    def getPerimetro(self):
        perimetro = 0
        n = len(self.vertices)
        for i in range(n):
            punto1 = self.vertices[i]
            punto2 = self.vertices[(i+1)%n]
            linea = Linea(punto1, punto2)
            perimetro += linea.getLongitud()
        return perimetro
    
    def getArea(self):
        area = 0
        n = len(self.vertices)
        for i in range(n):
            punto1 = self.vertices[i]
            punto2 = self.vertices[(i+1)%n]
            x1, y1 = punto1.get_x(), punto1.get_y()
            x2, y2 = punto2.get_x(), punto2.get_y()
            area += x1*y2 - x2*y1
        return abs(area/2)
    
    def __str__(self):
        vertices_str = ""
        for punto in self.vertices:
            vertices_str += str(punto) + ", "
        vertices_str = vertices_str[:-2]
        return f"Poligono con vertices: {vertices_str}"


p1 = Punto(3, 4)
print(p1)
print(type(p1))

p2 = Punto(7, 8)
print(p2)

p3 = Punto(5, 5)
print(p3)

p4 = Punto(5, 0)
print(p4)

l = Linea(p1, p2)
print(l)
print(type(l))
print("longitud: " ,l.getLongitud()) 

vertices = [p1, p2, p3, p4]
poligono = Poligono(vertices)
print("perimetro: " ,poligono.getPerimetro()) 
print("area: " ,poligono.getArea()) 
print(poligono) 
