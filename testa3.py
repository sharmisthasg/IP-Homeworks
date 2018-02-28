# IP - HOMEWORK 3
# SHARMISHTHA GUPTA - 2016193
# MEGHNA GUPTA - 2016056
import unittest
from a3 import *

class testa3(unittest.TestCase):


		def testoffByK(self):
			self.assertEqual(offByK("abc","Abc",1),True)
			self.assertEqual(offByK("aaaa","aaaa",0),True)
			self.assertEqual(offByK("aA12","aa12",0),False)
			self.assertEqual(offByK("meghna","anhgem",4),False)
			self.assertEqual(offByK("abcde","axcde",1),True)

		def testoffBySwaps(self):
			self.assertEqual(offBySwaps("meghna","hnagem"),True)
			self.assertEqual(offBySwaps("1234a","2a341"),True)
			self.assertEqual(offBySwaps("xexd","dexx"),True)
			self.assertEqual(offBySwaps("a","a"),True)
			self.assertEqual(offBySwaps("hello1","1ohell"),True)

		def testoffByKExtra(self):

			self.assertEqual(offByKExtra("helllooo","hellloooxxxsoo",6),True)
			self.assertEqual(offByKExtra("abcd","abcde",1),True)
			self.assertEqual(offByKExtra("yesao","yesao",0),True)
			self.assertEqual(offByKExtra("xyzie","xxyzie",2),False)
			self.assertEqual(offByKExtra("hey","h",2),True)

		def testListOfNearString(self):
			self.assertEqual(ListOfNearString("aahikl",new_list[:5],1),['aahing', 'aahs'])
			self.assertEqual(ListOfNearString("abduct",new_list[1:100],2),['aah', 'aahing', 'abacus', 'abased', 'abaser', 'abases', 'abated', 'abater', 'abates', 'abatis', 'abator', 'abbacy', 'abbe', 'abbess', 'abbeys', 'abbots', 'abbott', 'abbr', 'abbrev', 'abdicable', 'abdicate', 'abdicated', 'abdicates', 'abdicating', 'abdication', 'abdications', 'abdicator', 'abducted', 'abductor'])

			self.assertEqual(ListOfNearString("a",new_list[0:2],1),[])
			self.assertEqual(ListOfNearString("as",new_list[0:20],1),['a', 'aah', 'aahed', 'aahing', 'aahs', 'aardvark', 'aardvarks', 'aardwolf', 'ab', 'abaci', 'aback', 'abacus', 'abacuses', 'abaft', 'abalone', 'abalones', 'abandon', 'abandoned', 'abandonedly', 'abandonee'])

			self.assertEqual(ListOfNearString("ok",new_list[0:0],1),[])

		def testcompare_distr(self):
			self.assertEqual(compare_distr([1,4,2,2,1,7],[1,1,4,2,2,7],3),True)
			self.assertEqual(compare_distr([6,6,6],[3,3,3],1),True)
			self.assertEqual(compare_distr([1,0,0,2,0,0,1],[1,1,8,7,3,1,2],4),False)
			self.assertEqual(compare_distr([8,7,1,4,22],[7,8,1,1,44],2),False)
			self.assertEqual(compare_distr([4,6,7,2,4],[3,4,5,8,7],3),True)

	
if __name__ == '__main__':

	unittest.main()