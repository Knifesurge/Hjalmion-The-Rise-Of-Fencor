# Nick Mills
# Created: 2019-03-22
# Updated: 2019-03-22

import json

class Utils():

    # A list, that acts like a set, of loaded file data
    # Will contain Item, Enemy, Room, and Player data
    data = []

    @staticmethod
    def read_json(filename : str) -> bool:
        """
        ---------------------------------------------
        Reads JSON data from a file. Separate calls 
        to this function add None to the end of the 
        data to allow separation of the loaded data.
        Use: loaded = read_json(filename)
        ---------------------------------------------
        Parameters:
            filename - The name of the file to read (str)
        Returns:
            loaded - Whether the file data was successfully inserted
                    into the data cache (bool)
        ---------------------------------------------
        """
        loaded = False
        with open(filename, 'r') as f:
            contents = json.load(f)
            if contents not in Utils.data:
                Utils.data.append(contents)
                loaded = True
                Utils.data.append(None)
        return loaded

    @staticmethod
    def get_data() -> dict:
        """
        ---------------------------------------------
        Returns the data cache.
        Use: data = get_data()
        ---------------------------------------------
        Parameters:
            None
        Returns:
            data - A set of loaded file data (dict)
        ---------------------------------------------
        """
        return Utils.data

    @staticmethod
    def clear_data() -> None:
        """
        ---------------------------------------------
        Empties the data cache.
        ---------------------------------------------
        Parameters:
            None
        Returns:
            None
        ---------------------------------------------
        """
        Utils.data.clear()
        return