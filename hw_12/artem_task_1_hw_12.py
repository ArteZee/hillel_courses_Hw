import time


def karaoke(text: str):
    """
    function output sentence by sentence with time limited 0,5 sec
    :param text: str
    :return: sentece
    """

    text_list: list  = text.split()
    for i in range(len(text_list)):

        yield text_list[i]



text_song = "Акулёнок я туту-туту-руру Акулёнок я туту-туту-руру Акулёнок я туту-туту-руру Я малыш"
lets_sing = karaoke(text_song)

for word in lets_sing:
    time.sleep(0.5)
    print(word)

def clicker():
    """
    funciotn with generator - when u call cl put +1 to your clicking
    :return: int
    """
    large_digits:list = [x for x in range(1, 10_000)]
    for elements in range(len(large_digits)):
        yield large_digits[elements]


cl = clicker()
print("Your number click is:", cl.__next__())
print("Your number click is:", cl.__next__())
print("Your number click is:", cl.__next__())
print("Your number click is:", cl.__next__())


user_inform = {"Name": "Artem", "Age": 22, "Phone": "+380669425964", "sex": "male"}
def step():
    """
    Generator dive info about user when we call them
    :return: str
    """
    for key, value in user_inform.items():
        yield f"{key} - {value}"


st = step()

print(st.__next__())
print(st.__next__())
print(st.__next__())
