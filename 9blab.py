from numpy import random, mean
def main():
    world = World()
    for agent in world.agents:
        agent.run()
    print('world landsacpe: 1 as Agent, 0 as empty')
    world.report()
    print('done')


class World():
    def __init__(self, grid=(10,10), num_agents=80):
        self.grid_size = grid
        self.grid = self.build_grid(grid)
        self.agents = self.build_agents(num_agents)

    def report(self):
        for i in range(self.grid_size[0]):

            for j in range(self.grid_size[1]):
                if self.grid[(i,j)] is not None:
                    print('1 ', end='')
                else:
                    print('0 ', end='')
            print('\n')
    def build_grid(self, world_size):
        """create the world that the agents can move around on"""
        locations = [(i,j) for i in range(world_size[0]) for j in range(world_size[1])]
        return {l:None for l in locations}

    def build_agents(self, num_agents):
        """generate a list of Agents that can be iterated over"""
        agents = [Agent(self) for i in range(num_agents)]
        return agents

    def find_vacant(self):
        """finds all empty patches on the grid and returns a random one, unless kwarg return_all==True,
        then it returns a list of all empty patches"""

        empties = [loc for loc, occupant in self.grid.items() if occupant is None]
        return empties




class Agent():
    def __init__(self,world):
        self.world = world
        self.location = None
    def find_vacant(self):
        empties = self.world.find_vacant()
        return empties
    def run(self):
        vacancies = self.find_vacant()
        if len(vacancies) > 0:
            self.location = vacancies[random.choice(range(len(vacancies)))]
            self.world.grid[self.location] = self
        else:
            print('No vacancies')







if __name__ == '__main__':
    main()