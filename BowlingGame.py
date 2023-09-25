#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment
class BowlingGame:
    def __init__(self):
        """
        Initializes a new bowling game.
        """
        self.rolls=[] # A list to store the number of pins knocked down in each roll

    def roll(self,pins):
        """
        Records the number of pins knocked down in a roll.
        
        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates and returns the total score for the bowling game.

        Returns:
            int: The total score of the game.
        """
        result = 0 # Initialize the result to 0
        rollIndex=0 # Index to keep track of the current roll
        
        for _ in range(10): # Loop through 10 frames in a standard game
            if self.isStrike(rollIndex):
                # If it's a strike, add 10 plus the next two rolls' scores to the result
                result += 10 + self.strikeScore(rollIndex)
                rollIndex += 1 # Move to the next frame
            elif self.isSpare(rollIndex):
                # If it's a spare, add 10 plus the next roll's score to the result
                result += 10 + self.spareScore(rollIndex)
                rollIndex +=2 # Move to the next frame
            else: 
                # If it's an open frame, add the sum of the two rolls to the result
                result += self.frameScore(rollIndex)
                rollIndex +=2 # Move to the next frame
            
        return result

    def isStrike(self, rollIndex):
        """
        Checks if a roll is a strike.

        Args:
            roll_index (int): The index of the roll to check.

        Returns:
            bool: True if it's a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        """
        Checks if a frame is a spare.

        Args:
            roll_index (int): The index of the first roll in the frame.

        Returns:
            bool: True if it's a spare, False otherwise.
        """

        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def strikeScore(self,rollIndex):
        """
        Calculates the score for a strike frame.

        Args:
            roll_index (int): The index of the first roll in the strike frame.

        Returns:
            int: The score for the strike frame.
        """
        return self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """
        Calculates the score for a spare frame.

        Args:
            roll_index (int): The index of the first roll in the spare frame.

        Returns:
            int: The score for the spare frame.
        """

        return self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for an open frame.

        Args:
            roll_index (int): The index of the first roll in the frame.

        Returns:
            int: The score for the open frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.