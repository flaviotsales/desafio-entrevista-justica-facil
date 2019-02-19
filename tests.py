import unittest
import diarios

class TseTests(unittest.TestCase):
    def test_hashDiarioPorData_diarioExisteNaData_retornaHash(self):
        self.assertEqual(diarios.getDiarioMd5PorData('2018-12-02'), '78addcf872a1fcfbb10384da4b8ba696')

    def test_hashDiarioPorData_diarioNaoExisteNaData_retornaNone(self):
        self.assertEqual(diarios.getDiarioMd5PorData('2018-10-02'), None)

unittest.main()