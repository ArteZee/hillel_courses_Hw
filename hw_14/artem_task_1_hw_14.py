from impoted_class import Jarvis


class Robot:
    software_robot = "Microsoft"
    material = "aluminium"

    def check_atr(self, attribute: str):
        """
        function check if instance have the attribute
        :param:str  attribute:
        :return:bool
        """
        if not hasattr(self, attribute):
            return False
        return True

    def __init__(self, model: str, tall: float):
        self.model = model
        self.tall = tall

    @staticmethod
    def budget_capacity(budget_money: int):
        """
        Check how much robots can we buy
        :param: budget_money:int
        :return:int
        """
        price_1_robot = 1000
        county_robot = round(budget_money / price_1_robot)

        return f"You can afford: {county_robot} robots"

    @classmethod
    def change_software(cls, software_user: str):
        """
        Change software attribute of class
        :param software_user:str

        """
        cls.software_robot = software_user


robot_artem = Robot("artem", 1.75)
robot_kirill = Jarvis("Artem", "Kirill")

if __name__ == "__main__":
    print(robot_artem.budget_capacity(100000000))

    # check gow work our change attribute from class
    print(vars(Robot))
    robot_artem.change_software("IOS")
    print(f"{vars(Robot)} \n\n")
    # check function check_atr
    print(robot_artem.check_atr("material"))

    # how work our imported class Jarvis
    print("\n\n" + robot_kirill.welcome)
    robot_kirill.welcome = ("Max", "Jojo")
    print(robot_kirill.welcome)
