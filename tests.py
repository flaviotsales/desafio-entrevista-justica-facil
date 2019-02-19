import unittest
import diarios

class TseTests(unittest.TestCase):
    def test_getDiarioMd5PorData_diarioExisteNaData_retornaHash(self):
        self.assertEqual(diarios.getDiarioMd5PorData('12/02/2018'), '78addcf872a1fcfbb10384da4b8ba696')

    def test_getDiarioMd5PorData_diarioNaoExisteNaData_retornaNone(self):
        self.assertEqual(diarios.getDiarioMd5PorData('10/02/2018'), None)

    def test_getIdDiarioPorData_diarioExisteNaData_retornaHash(self):
        self.assertEqual(diarios.getIdDiarioPorData('12/02/2018'), '96642')

    def test_getIdDiarioPorData_diarioNaoExisteNaData_retornaNone(self):
        self.assertEqual(diarios.getIdDiarioPorData('10/02/2018'), None)

unittest.main()