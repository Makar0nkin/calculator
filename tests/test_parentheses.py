from main import calculate

class TestParentheses:
    def test_pair_1(self):
        expr: str = '2 + (2 * 2)'
        assert calculate(expr) == eval(expr)
        
    def test_pair_2(self):
        expr: str = '2 / (2 + 2)'
        assert calculate(expr) == eval(expr)
        
    def test_two_pairs_1(self):
        expr: str = '(22 + 99) / (12 - 1)'
        assert calculate(expr) == eval(expr)
        
    def test_two_pairs_2(self):
        expr: str = '(1 + 3) / 7 ** (1/3)'
        assert calculate(expr) == eval(expr)
        
    def test_nested_1(self):
        expr: str = '(999 * (77 - 13)) / 5'
        assert calculate(expr) == eval(expr)
        
    def test_nested_2(self):
        expr: str = '((3 - 1/2) ** 2 + (4 + 7) ** 2) ** (1/2)'
        assert calculate(expr) == eval(expr)