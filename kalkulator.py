"""
Masuk ke dalam Style guide
"""


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i


"""
pycodestyle kalkulator.py
membantu mengecek kode terkait gaya penulisan kode dengan konvensi PEP8.
"""
"""
pylint kalkulator.py
analisis kode Python, mengecek untuk kesalahan (error) pemrograman, 
memaksakan standar penulisan kode dengan mengecek penulisan kode 
yang tidak baik, serta memberikan saran untuk refactoring sederhana.
"""

"""
flake8 kalkulator.py
yang membungkus sejumlah kemampuan aplikasi lain, seperti pycodestyle, 
pyflakes, dan (skrip/fitur) lainnya.
"""
"""
black kalkulator.py
autopep8 kalkulator.py
Cara kerja autopep8 dapat memberi saran kode ke layar terminal atau 
seperti black yang akan mengubah langsung isi file kalkulator.py.
Jika Anda ingin autopep8 memberikan saran kode, silakan jalankan kode berikut.
Jika Anda ingin mengubah kode file secara langsung, silakan jalankan kode 
berikut dan periksa kembali file kode Anda.
autopep8 --in-place --aggressive --aggressive kalkulator.py
"""
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)

class DivideByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed"):
        super().__init__(message)
def divide_numbers(a, b):
    if b == 0:
        raise DivideByZeroError("cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10,2)
except DivideByZeroError as e:
    print(f"Error: {e}")