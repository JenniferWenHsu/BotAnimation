from terrain import Terrain 
import unittest

class TestTerrain(unittest.TestCase): 

	def test_getYValue(self): 
		terrain1 = Terrain()
		terrain2 = Terrain()
		set1 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
		set2 = [0, 0.8, 0.5, 0.4, 0.1, 0.1, 0.7, 0.8, 0.9, 1]
		terrain1.setPointList(set1)
		terrain2.setPointList(set2)
		self.assertEqual(terrain1.getYValue(6.5), 0.5)
		self.assertEqual(terrain2.getYValue(0.5), 0.4)


if __name__ == '__main__': 
	unittest.main()
