#define the base class player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

#define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is batting.")

#create objectsvof Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each objects
batsman.play()
bowler.play()