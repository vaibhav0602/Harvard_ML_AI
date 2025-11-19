import random

from networkx.algorithms.flow import cost_of_flow
from networkx.classes import neighbors


class Space():
    def __init__(self,height,width,num_hospitals):
        self.height=height
        self.width=width
        self.num_hospitals=num_hospitals
        self.house=[]
        self.hospitals=[]
        self.image_prefix='hospitals'
        self.log=True

    def add_house(self,loc_x,loc_y):
        self.house.append((loc_x,loc_y))

    def calculate_cost(self,hospital):
        cost=0

        return cost

    def find_neighbours(self,hospital):
        neighbour=hospital

        return neighbour

    def hill_climb(self,image_prefix,log):
        self.image_prefix=image_prefix
        self.log=log
        for i in range(self.num_hospitals):
            self.hospitals.append((random.randrange(self.height), random.randrange(self.width)))

        best_cost=self.calculate_cost(self.hospitals)
        cost=float('inf')

        while best_cost>0 or cost>best_cost:
            k=0
            for hospital in self.hospitals:

                neighbours=self.find_neighbours(hospital)
                for neighbour in neighbours:
                    cost=self.calculate_cost(neighbour)
                    if cost<best_cost :
                        best_cost=cost
                        self.hospitals[k]=neighbour



        return self.hospital

s = Space(height=10, width=20, num_hospitals=3)
for i in range(15):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

# Use local search to determine hospital placement
hospitals = s.hill_climb(image_prefix="hospitals", log=True)