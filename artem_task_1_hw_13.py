class Robot:
    __instance = None

    # singleton - give us class which will have only 1 instance
    def __new__(cls, *arg, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        Robot.__instance = None

    def __init__(self, model: str, tall: float, position: str, cost: str):
        """
        function get data of robot options
        :param model: str
        :param tall: float
        :param position: str
        :param cost: str
        """
        self.model = model
        self.tall = tall
        self.position = position
        self.cost = cost

    def __call__(self):
        """
        function can call the object without ()
        :return: all options for instance
        """
        return vars(self)

    def __repr__(self):
        """
        function give info about have to create our class
        :return:
        """
        return "new_model_robot = Robot('model_robot','tall_robot', 'function_robot', cost_robot )"

    @property
    def all_data_info(self):
        """
        Getter
        output all arguments of methods init
        :return: str
        """
        return f"{self.model}, {self.tall}, {self.position}, {self.cost}"

    @all_data_info.setter
    def all_data_info(self, value: list):
        """
        Setter
        change parameter some of value
        :param value:list
        :return: str
        """
        self.position = value[0]
        self.cost = value[1]

    @all_data_info.deleter
    def all_data_info(self):
        """
        Deleter
        change all parameters to None
        :return: None
        """
        self.model = None
        self.tall = None
        self.position = None
        self.cost = None


robot_artemka = Robot("Artemka", 1.75, "junior", "1$")
robot_kirill = Robot("Kirill", 1.90, "middle", "2800$")

print(robot_artemka.all_data_info)

robot_artemka.all_data_info = ["senior", "10000$"]
print(robot_artemka.all_data_info)

del robot_artemka.all_data_info
print(robot_artemka.all_data_info)

print(id(robot_artemka))
print(id(robot_kirill))
