import settings
import obstacle

class Super_Coin(obstacle.Obstacle):
  def __init__(self):
    super().__init__(20, 1, "images/super_coin.png", settings.SPEED)