# SHARMISHTHA GUPTA - 2016193
# MEGHNA GUPTA - 2016056

import unittest
from a4 import *

class testa4(unittest.TestCase):

	def testMatrixRank(self):
		self.assertEqual(MatrixRank([[1,2,3],[0,0,1],[4,5,6]]),3)
		self.assertEqual(MatrixRank([[0,0,0],[0,0,0],[0,0,0]]),0)
		self.assertEqual(MatrixRank([[0,0,0],[0,0,2]]),1)
		self.assertEqual(MatrixRank([[1,2,3],[4,5,6],[7,8,9]]),3)
		self.assertEqual(MatrixRank([[4,2,2],[2,1,1],[1,1,0]]),3)
		self.assertEqual(MatrixRank([[1,1,1],[1,2,1]]),2)

	if __name__ == '__main__':
		unittest.main()