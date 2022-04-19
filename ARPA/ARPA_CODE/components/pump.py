import json
class Pump:
    def __init__(self):
        config_file = open("ARPA_CODE/data/config.json", "r")
        config_info = json.load(config_file)
        self.retract_speed = config_info['Pump']['retract_speed']
        self.push_speed = config_info['Pump']['push_speed']
        self.push_speed = config_info['Pump']['push_speed']
        self.travel_distance = config_info['Pump']['travel_distance']
        self.reservoir_volume = config_info['Pump']['reservoir_volume']
        self.piston_s_a = config_info['Pump']['piston_s_a']
        config_file.close()
        self.distance_per_rev = config_info['Pump']['distance_per_rev']
    def dose(self, num_of_units):
        un_per_mm = (self.piston_s_a*100)
        secs_per_un = ((1/self.push_speed)) #0.4 seconds per 17.6un
        

        print(self.push_speed, un_per_mm, secs_per_un)
        
    def refill(self):   
        pass
