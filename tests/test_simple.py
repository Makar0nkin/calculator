from main import calculate

class TestSimpleExpressions:
    def test_add(self):
        expr: str = '2 + 2'
        assert calculate(expr) == eval(expr)
        
    def test_subtract(self):
        expr: str = '2 - 2'
        assert calculate(expr) == eval(expr)

    def test_multiply(self):
        expr: str = '2 * 2'
        assert calculate(expr) == eval(expr)
        
    def test_devide(self):
        expr: str = '2 / 2'
        assert calculate(expr) == eval(expr)
        
    def test_power(self):
        expr: str = '2 ** 2'
        assert calculate(expr) == eval(expr)
        
    def test_fractional_power(self):
        expr: str = '2 ** (1/2)'
        assert calculate(expr) == eval(expr)
        
    def test_calc_order_1(self):
        expr: str = '2 + 2 * 2'
        assert calculate(expr) == eval(expr)
        
    def test_calc_order_2(self):
        expr: str = '2 / 2 + 2'
        assert calculate(expr) == eval(expr)
        
    def test_longer_numbers(self):
        expr: str = '999 / 11'
        assert calculate(expr) == eval(expr)