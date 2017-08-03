class HeatIndex(object):
    def __init__(self, daily_temp, daily_humidity):
        print 'Created HeatIndex'

    @classmethod
    def heat_index(cls, temp, humidity):
        return round(1.98*(temp-(.55-.0055*humidity)*(temp-58))- 56.83, 1)
    
    def max_for_location(self, location):
      
      th_dict = map_temp_humidity(location)  #calls the helper function with location as argument
      heat_indexes = []

      for key, value in th_dict.items(): #helper function returns dictionary of temp/humidity pairs
        hi = self.heat_index(int(key), value) #temp is the key, humidity is the value, heat_index method called
        heat_indexes.append(hi) #heat index added to list of all heat indexes for location

      return max(heat_indexes) #max is returned
        
    def min_for_location(self, location):
        
      th_dict = map_temp_humidity(location)  
      heat_indexes = []

      for key, value in th_dict.items(): 
        hi = self.heat_index(int(key), value) #temp is the key, humidity is the value
        heat_indexes.append(hi)

      return min(heat_indexes)


temps=["SJC,81,81,82,83,84,85,83",
       "LAX,74,75,76,78,79,81,82",
       "OAK,78,77,79,81,83,83,82",
       "TPA,66,68,69,71,73,75,77"]

humidity=["LAX,26,26,26,26,27,27,27",
          "TPA,81,82,83,84,85,92,98",
          "MIA,71,73,75,78,82,82,81",
          "SJC,50,51,52,53,54,55,56"]

heat_index = HeatIndex(temps, humidity)


#added this helper function to map temperature and humidity with location and separate out functionality
#since we will need the same look up for min or max  
def map_temp_humidity(location):

  temp_keys = None
  hum_values = None

  for t in temps: #two loops to look up temperatures and humidities for a given location
    t = t.split(",") #creates a new list out of each location/temp item
    if t[0] == location: 
      temp_keys = t[1:] #updates temp variable with index of temperature for location


  for h in humidity: 
    h = h.split(",") #creates a new list out of each location/humidity item
    if h[0] == location:
      hum_values = h[1:] #updates humidity variable with index of humidity for location

  out_temp_hum = {} #create a dictionary to map all of the humidities and temperatures for days in a certain location

  for i in range(len(temp_keys)):
    out_temp_hum[temp_keys[i]] = int(hum_values[i])


  return out_temp_hum #returns a dictionary with temp/humidity key/value pairs for location to min and max methods


# TODO: Uncomment asserts and write code to make them pass.
assert heat_index.max_for_location('SJC') == 98.2
assert heat_index.min_for_location('LAX') == 76.8
    
    