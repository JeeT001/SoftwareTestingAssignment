#This file has information about test cases which you need to test.

import unittest
from BowlingGame import BowlingGame  # Assuming BowlingGame is defined in BowlingGame.py

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        # Create a new instance of BowlingGame before each test
        self.game = BowlingGame()

    def testGutterGame(self):
        # Test a game where all rolls result in 0 pins knocked down (a "gutter game").
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0)
        
    def testAllOnes(self):
         # Test a game where all rolls result in 1 pin knocked down.
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)
        
    def testOneSpare(self):
        # Test a game with one spare (5 pins in the first frame, 3 in the next).
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16)
        
    def testOneStrike(self):
        # Test a game with one strike (all pins knocked down in the first frame).
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24)
        
    def testPerfectGame(self):
        # Test a perfect game with all strikes (12 strikes for 300 points).
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300)
        
    def testAllFives(self):
        # Test a game where all rolls result in 5 pins knocked down (a score of 150).
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150)
        
    def rollMany(self, pins,rolls):
        # Helper function to roll the same number of pins multiple times.
        for _ in range(rolls):
            self.game.roll(pins)
            
if __name__ == "__main__":
    unittest.main()