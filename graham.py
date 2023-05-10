import math
import json

def anguloPolar(pOne, pTwo):
	return math.atan2(pTwo[1]-pOne[1], pTwo[0]-pOne[0])

