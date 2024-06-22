import unittest

class TestStringMethods(unittest.TestCase):
    # ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'),'dicoding')

    #test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    #test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')

if __name__ == '__main__':
    # test runner
    unittest.main()

''' contoh test user'''

import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db{}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    #test case 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif) #tidak aktif secara default
        putus_koneksi_db(db)

    #test case 2
    def test_user_is_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        dicoding.set_aktif() #aktifkan user baru
        self.assertTrue(dicoding,aktif)
        putus_koneksi_db(db)

if __name__ == "__main__":
    #test runner
    unittest.main()

'''versi teardown dan setUp'''
import unittest

def koneksi_ke_db():
    print("[terhubung ke db]")

def putus_koneksi_db(db):
    print("[tidak terhubung ke db{}]".format(db))

class User:
    username = ""
    aktif = False

    def __init__(self, db, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True

class TestUser(unittest.TestCase):
    #test fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")

    def tearDown(self):
        putus_koneksi_db(self.db)

    #test case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif) #tidak aktif secara dafault

    #test case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif() #aktifkan user baru
        self.assertTrue(self.dicoding.aktif)

if __name__ == "__main__":
    #test runner
    unittest.main()
