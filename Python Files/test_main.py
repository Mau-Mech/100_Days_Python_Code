import logging
import pytest
import math

class Triangle():
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return ((self.b*self.h)/2)
    
    def perimeter(self):
        return round((2*math.sqrt(((self.b**2)/4)+self.h**2) + self.b), 2)

@pytest.fixture(scope = "session", autouse= True) # De que trata esta linea ??
def triangle12():
    logging.info("Fixture triangle 1, 2")
    return Triangle(1,2)

@pytest.mark.Logs
@pytest.mark.Debug
def test_showLogging(): 
    #pytest.skip("Demo")
    logging.basicConfig(level = logging.INFO)
    logging.debug("This is a DEBUG")
    logging.info("This is a INFO")
    logging.warning("This is a WARNING")
    logging.error("This is an ERROR")

@pytest.mark.Triangle
class TestTriangle:

    def setup_class(self):
        logging.info("Set Up")
        self.triangle = Triangle(1,2)

    def teardown_class(self):
        logging.info("tear down")
        logging.info(self.triangle)
        del self.triangle
        #logging.info(self.triangle)

    def test_area(self):
        logging.debug(self.triangle.__dict__)
        assert self.triangle.area() == 1, "Triangle b =1, h = 1, area must be 1"

    @pytest.mark.Debug
    def test_areaType(self):
        assert type(self.triangle.area()) == float , "Triangle area must be float"

    def test_areabase(self):
        assert self.triangle.b == 1 , "Triangle base must be 1"

    @pytest.mark.parametrize("base, height, area", [[1,2,1],[2,3,3],[3,4,6],[4,5,10]])    
    def test_areaParametrize(self, base, height,area):
        logging.info(f"Triangle {base}, {height}")
        t1 = Triangle(base,height)
        assert t1.area() == area, "Triangle b = 1, h = 2, area must be 1"

    @pytest.mark.Debug 
    @pytest.mark.parametrize("base, height, perimeter",[[8,5,20.81],[10,6,25.62],[12,7,30.44],[11,5,25.87]])
    def test_perimeterParametrize(self,base,height, perimeter):
        logging.info(f"Triangle {base}, {height}")
        t2 = Triangle(base , height)
        assert t2.perimeter() == perimeter, "Triangle b = 1, h = 2, perimeter must be...."