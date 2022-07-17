# variable that save our data of course and availability
value: dict = {"USD": {"course": 27.3, "availability": 20000},
               "UAH": {"course": 27.1, "availability": 25500},
               }


def course_value(currency: str):
    """
    function out put course of currency and her available
    if value do not have currency- out put it
    """
    if currency in list(value.keys()):
        return "Rate {} , AVAILABLE {}".format(value[currency]["course"], value[currency]['availability'])
    else:
        return "INVALID CURRENCY {}".format(currency)


def exchange_value(currency: str, amount: int):
    """
    function get from user currency and amount and get to another currency
    and this  difference save in value: dict

    if we do not have enough availability - return error text
    """

    available_UAH = value["UAH"]["availability"]
    available_USD = value["USD"]["availability"]

    if currency == "UAH":
        # count how many UAH will be in USD
        value_exchange = round(amount / value["USD"]["course"],2)
        # compare if we have enough UAH to USD do exchange
        if value_exchange <= available_USD:
            # save result of difference in value: dict
            value["USD"]["availability"] = available_USD - value_exchange
            return "USD - {}, RATE - {} ".format(value_exchange, value_exchange / 100)
        else:
            # return text error if availability not enough
            return "UNAVAILABLE, REQUIRED BALANCE USD {}, AVAILABLE {}".format(value_exchange, available_USD)

    if currency == "USD":
        # count how many USD will be in UAH
        value_exchange = round(amount * value["UAH"]["course"],2)
        # compare if we have enough USD to UAH do exchange
        if value_exchange <= available_UAH:
            # save result of difference in value: dict
            value["UAH"]["availability"] = available_UAH - value_exchange
            return "UAH - {}, RATE - {} ".format(value_exchange, value["UAH"]["course"])

        else:
            return "UNAVAILABLE, REQUIRED BALANCE UAH {}, AVAILABLE {}".format(value_exchange, available_UAH)
