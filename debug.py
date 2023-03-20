from lib.animal import *
from lib.zoo import *

# code here

pereguin_zoo = Zoo("Pereguin Zoo", "Bergenshire")
sample_zoo = Zoo("Sample", "SampleLoc")
pebble_zoo = Zoo("Pebble Zoo", "Bergenshire")

parakeet = Animal("parakeet", 5, "bobo", sample_zoo)
orangutan = Animal("orangutan", 23, "folasel", sample_zoo)
elephant = Animal("elephant", 240, "ellie", pereguin_zoo)
gnome = Animal("gnome", 1, "frederick", pereguin_zoo)
chicken = Animal("chicken", 6, "basil", sample_zoo)
gnome2 = Animal("gnome", 1, "periwinkle", pereguin_zoo)



# e.g.  
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )






# do not remove 
import ipdb; ipdb.set_trace()
