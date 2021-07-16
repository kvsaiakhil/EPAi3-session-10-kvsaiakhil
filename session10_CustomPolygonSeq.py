from session10_Polygon import Polygon

class CustomPolygonSeq(Polygon):
    ''' CustomPolygonSeq class inherited from class Polygon, 
        creates a list of Polygons,
        from three sided polygon to n sided polygon, all with the same circum-radius
    '''
    
    def __init__(self, n, cir_rad):
        super().__init__(n, cir_rad)
    
    def __repr__(self) -> str:
        return f"Custom_Polygon_Seq(n = {self.n}, cir_rad = {self.cir_rad})"

    def max_efficiency(self):
        return max([(i.apothem, i) for i in list(self)], key=lambda x: x[0])[1]
    
    def __len__(self):
        return self.n - 2

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = self.n + s - 2
            if s < 0 or s > self.n - 3:
                raise IndexError
            else:
                return Polygon(s+3, self.cir_rad)
        elif isinstance(s, slice):
            start, stop, step = s.indices(self.n - 2)
            rng = range(start, stop, step)
            return [Polygon(i+3, self.cir_rad) for i in rng]
        else:
            raise TypeError(f"Custom_Polygon_Seq indices must be integers or slices, not {type(s).__name__}")