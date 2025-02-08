import logging
import pytest
import math

class Perimeter_Triangle():
    def __init__(self,b,h):
        self.b = b
        self.h = h
        
    def perimeter(self):
        return round((2*math.sqrt(((self.b**2)/4)+self.h**2) + self.b), 2)
    

@pytest.mark.Perimeter_Triangle
class TestPerimeter:   
    @pytest.mark.Debug 
    @pytest.mark.parametrize("base, height, perimeter",[[8,5,20.81],[10,6,25.62],[12,7,30.44],[11,5,25.87]])
    def test_perimeterParametrize(self,base,height, perimeter):
        logging.info(f"Triangle {base}, {height}")
        t2 = Perimeter_Triangle(base , height)
        assert t2.perimeter() == perimeter, "Triangle b = 1, h = 2, perimeter must be...."