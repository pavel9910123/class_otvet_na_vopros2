# add your code from task 1 between the lines
#---------------------------------------------------------------------------
class Things():
    pass
class Inanimate(Things):
    pass

class Animate(Things):
    # example of a class function
    def exist(self):
        print('Cogito ergo sum')

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    # TODO - create three functions for this class: move(), eat(), breathe()
    def duhanie(self):
        print('duschat')
    def dwigat(self):
        print('dwigat')
    def est(self):
        print('est')

    
class Mammals(Animals):
    # TODO - create one function for this class: feed_baby_with_milk()
    def kormit_molokom(self):
        print('kormit molokom')
    

class Giraffes(Mammals):
    # TODO - create one function for this class: eat_leaves_from_trees()
    def ediat_listia(self):
        print('est listia')
#---------------------------------------------------------------------------

# TODO 
# 1 create a Giraffes object 'reginald'
# 2 make reginald move, breathe and eat leaves from trees
# 3 create another object 'infusorium' - which class does it refer to?
# 4 make your infusorium exist
# 5 check if infusorium can move, eat or breathe

reginald=Giraffes()
reginald.dwigat()
reginald.duhanie()
reginald.ediat_listia()
invusoria=Animate()
invusoria.exist()
invusoria.dwigat()
invusoria.duhanie()
invusoria.ediat_listia()
