from classes.bot import Bot 
from classes.terrain import Terrain 
from classes.environment import Environment
bot = Bot()
terrain = Terrain()
environment = Environment(bot, terrain)
environment.startAnimation()