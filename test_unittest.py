#This file has information about test cases which you need to test.

import unittest
from BowlingGame import BowlingGame  # Assuming BowlingGame is defined in BowlingGame.py

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def testGutterGame(self):
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0)
        
    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)
        
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16)
        
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24)
        
    def testPerfectGame(self):
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300)
        
    def testOneSpare(self):
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150)
        
    def rollMany(self, pins,rolls):
        for _ in range(rolls):
            self.game.rolls(pins)
            
if __name__ == "__main__":
    unittest.main()