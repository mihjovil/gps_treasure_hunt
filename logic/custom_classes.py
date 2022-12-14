from dataclasses import dataclass, field
from typing import List
import geopy.distance

@dataclass
class Location:
    latitude: float
    longitude: float
    visited: bool = False

@dataclass(order=True)
class Hunt:
    sort_index: str = field(init=False, repr=False)
    name: str
    locations: List[Location]
    current_goal: Location = None
    current_index: int = 0
    threshold: float = 0

    def __post_init__(self):
        self.sort_index = self.name
        self.current_index = 0
        self.current_goal = self.locations[self.current_index]

    def validate(self) -> bool:
        """ Validates whether the hunt is over or not

        This function will go through all the locations of the hunt and check if they have been visited.
        If they have, then the hunt is over, otherwise the hunt is still missing some clues.
        :return: True if the hunt is over False otherwise.
        """
        for location in self.locations:
            if not location.visited:
                return False
        return True

    def check_location(self, query_location: Location) -> bool:
        """ Checks for a location to see if the user is in the correct spot in order to validate a location.

        This funtion calculates the distance between the described location and the proposed location from the user
        and determines if the user is at the correct place. If so, it updates the location form the tresure hunt and
        informs the user.
        :return: True if the user is at the correct location, False otherwise.
        """
        # TODO calculate distance between locations
        comparison_coordinates = (self.current_goal.latitude, self.current_goal.longitude)
        query_coordinates = (query_location.latitude, query_location.longitude)
        distance = geopy.distance.geodesic(comparison_coordinates, query_coordinates).km * 1_000
        if distance < self.threshold:
            self.locations[self.current_index].visited = True
            self.current_index += 1
            self.current_goal = self.locations[self.current_index]
            return True
        else:
            return False


@dataclass
class User:
    # region attributes
    name: str
    password: str
    hunts: Hunt = None
        
    def add_hunt(self, new_hunt: Hunt):
        self.hunts.append(new_hunt)
        
   def remove_hunt(self, delete_hunt: Hunt):
        self.hunts.pop(delete_hunt)
        
    # endregion
