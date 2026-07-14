"""space_age challenge"""

ORBITAL_PERIODS_IN_EARTH_YEARS = {
    "Mercury" :	0.2408467,
    "Venus": 0.61519726,
    "Earth" : 1.0,
    "Mars" : 1.8808158,
    "Jupiter": 11.862615,
    "Saturn"	: 29.447498,
    "Uranus"	: 84.016846,
    "Neptune"	: 164.79132,
}


class SpaceAge:
    """
        Represents a person's age on different planets.

    Attributes:
        seconds (int): Age expressed in seconds.
    """
    
    YEARS_IN_SECONDS = 365.25 * 24 * 3600
    
    def __init__(self, seconds):
        """Initialize a SpaceAge object.

        Args:
            seconds (int): Age expressed in seconds.
        """
        self.seconds = seconds

    def _calculate_years(self, planet):
        """Return the age on the specified planet.

        Args:
            planet (str): Name of the planet.

        Returns:
            float: Age on the specified planet.
        """
        
        return round (
            self.seconds / (SpaceAge.YEARS_IN_SECONDS * ORBITAL_PERIODS_IN_EARTH_YEARS[planet]), 2)
        
    def on_earth(self):
        return self._calculate_years("Earth") 
    def on_mercury(self):
        return self._calculate_years("Mercury") 
    def on_venus(self):
        return self._calculate_years("Venus") 
    def on_mars(self):
        return self._calculate_years("Mars") 
    def on_saturn(self):
        return self._calculate_years("Saturn") 
    def on_neptune(self):
        return self._calculate_years("Neptune") 
    def on_uranus(self):
        return self._calculate_years("Uranus") 
    def on_jupiter(self):
        return self._calculate_years("Jupiter") 

    