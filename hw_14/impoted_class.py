class Jarvis:
    """
    This class help us to greet users by his name
    Also change name to robot
    """

    def __init__(self, user, name_robot):
        self.user = user
        self.name_robot = name_robot

    @property
    def welcome(self):
        """Getter"""
        return f"Hi {self.user}, My name {self.name_robot}, good day sir"

    @welcome.setter
    def welcome(self, value: tuple or list):
        """Setter"""
        self.user = value[0]
        self.name_robot = value[1]

    @welcome.deleter
    def welcome(self):
        """deleter"""
        self.user = None
        self.name_robot = None

# artem = Jarvis("Max", "Artem")
#
# if __name__ == "__main__":
#     print(artem.welcome)
