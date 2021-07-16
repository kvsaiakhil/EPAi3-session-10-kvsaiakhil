import math
from fractions import Fraction
from PIL import Image, ImageDraw
from PIL import ImagePath 

class Polygon:
    ''' Polygon class that form a polygon 
        of the given number of sides and circum-radius 
    '''
    def __init__(self, n, cir_rad):
        if n<=2:
            raise ValueError("n must be greater than 2 to form a polygon, I'm neither a mathematician not a magician ")
        if cir_rad <= 0:
            raise ValueError("circum-radius must be positive integer, I'm not a mathamatician")
        self.n = n
        self.cir_rad = cir_rad
        self.properties()
    
    def properties(self):
        self.edges = self.n
        self.vertices = self.n
        self.int_angle = (self.n-2) * 180/2
        self.edge_len = 2 * self.cir_rad * (math.sin(math.pi/self.n))
        self.apothem = self.cir_rad * (math.cos(math.pi/self.n))
        self.area = Fraction(1,2) * self.n * self.apothem * self.edge_len
        self.perimeter = self.n * self.edge_len
    
    def print_properties(self):
        properties_dict = { 
                            "no. of edges": self.edges, 
                            "no. of vertices": self.vertices, 
                            "internal angle": self.int_angle,
                            "length of each side": self.edge_len,
                            "length of apothem": self.apothem,
                            "area": self.area,
                            "perimeter": self.perimeter
                            }
        print(properties_dict)

    def draw(self):
        xy = [
            ((math.cos(th) + 1) * 60,
            (math.sin(th) + 1) * 60)
            for th in [i * (2 * math.pi) / self.n for i in range(self.n)]
            ]  
        
        image = ImagePath.Path(xy).getbbox()  
        size = list(map(int, map(math.ceil, image[2:])))
        
        img = Image.new("RGB", size, "#ffffff") 
        img1 = ImageDraw.Draw(img)  
        img1.polygon(xy, fill ="#ffffff", outline ="black") 
        
        img.show() 

    def __repr__(self) -> str:
        return f"Polygon(n = {self.n}, cir_rad = {self.cir_rad})"

    def __eq__(self, polygon2):
        if not isinstance(polygon2, Polygon):
            raise TypeError(f"should be of type Polygon, not {type(polygon2).__name__}")
        return self.n == polygon2.n and self.cir_rad == polygon2.cir_rad
        
    def __gt__(self, polygon2):
        if not isinstance(polygon2, Polygon):
            raise TypeError(f"should be of type Polygon, not {type(polygon2).__name__}")
        return self.n > polygon2.n
