import unittest
import diarios
import os

class TseTests(unittest.TestCase):
    def test_getDiarioMd5PorData_diarioExisteNaData_retornaHash(self):
        self.assertEqual(diarios.getDiarioMd5PorData('12/02/2019'), '78addcf872a1fcfbb10384da4b8ba696')

    def test_getDiarioMd5PorData_diarioNaoExisteNaData_retornaNone(self):
        self.assertEqual(diarios.getDiarioMd5PorData('10/02/2019'), None)

    def test_getIdDiarioPorData_diarioExisteNaData_retornaId(self):
        self.assertEqual(diarios.getIdDiarioPorData('12/02/2019'), '96642')

    def test_getIdDiarioPorData_diarioNaoExisteNaData_retornaNone(self):
        self.assertEqual(diarios.getIdDiarioPorData('10/02/2019'), None)

    def test_baixaDiarioPorId_diarioExiste_arquivoSalvoComNomePadrao(self):
        diarios.baixaDiarioPorId('96642')
        self.assertTrue(os.path.isfile("TSE-30_2019.pdf"))

    def test_baixaDiarioPorId_diarioExisteComNomeEspecificado_arquivoSalvoComNomeEspecificado(self):
        diarios.baixaDiarioPorId('96642', 'diario_96642.pdf')
        self.assertTrue(os.path.isfile("diario_96642.pdf"))
        
    def test_baixaDiarioPorId_diarioNaoExiste_arquivoNaoSalvo(self):
        diarios.baixaDiarioPorId('96643', 'diario_96643.pdf')
        self.assertFalse(os.path.isfile("diario_96643.pdf"))

unittest.main()