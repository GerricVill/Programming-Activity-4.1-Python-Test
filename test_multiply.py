import unittest
def multiply(x,y):
    return x*y

class mytest(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(2,6),6)

if __name__=='__main__':
    unittest.main()