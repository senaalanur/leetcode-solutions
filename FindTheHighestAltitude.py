class Solution:
    def largestAltitude(self, gain):
        altitude = 0          # starting altitude
        highest = 0           # highest altitude seen so far
        
        for g in gain:
            altitude += g     # update current altitude
            highest = max(highest, altitude)  # check if it's the new highest
            
        return highest
