from dataclasses import dataclass
from typing import List

@dataclass
class Location:
    latitude: float
    longitude: float
    visited: bool = False

@dataclass
class Hunt:
    name: str
    locations: List[Location]
    current_goal: Location | None
    current_index: int
    threshold: float = 0

    def __post_init__(self):
        self.current_index = 0
        self.current_goal = self.location[self.current_index]

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
        distance = 0
        if distance < self.threshold:
            self.locations[current_index].visited = True
            self.current_index += 1
            self.current_location = self.locations[self.current_index]
            return True
        else:
            return False

@dataclass
class User:
    # region attributes
    name: str
    password: str
    hunts: Hunt | None
    # endregion
