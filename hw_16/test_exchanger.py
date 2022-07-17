from exchanger import value


def check_course_currency(currency: str):
    if currency in list(value.keys()):
        return "Rate {} , AVAILABLE {}".format(value[currency]["course"], value[currency]['availability'])
    else:
        return "INVALID CURRENCY {}".format(currency)


def check_course_currency_USD():
    test_value = "Rate 27.3 , AVAILABLE 20000"
    assert check_course_currency("USD") == test_value


def check_exchange_value(currency: str, amount: int):
    available_UAH = value["UAH"]["availability"]
    available_USD = value["USD"]["availability"]

    if currency == "UAH":
        value_exchange = round(amount / value["USD"]["course"], 2)
        if value_exchange <= available_USD:
            value["USD"]["availability"] = available_USD - value_exchange
            return "USD - {}, RATE - {} ".format(value_exchange, value_exchange / 100)
        else:
            return "UNAVAILABLE, REQUIRED BALANCE USD {}, AVAILABLE {}".format(value_exchange, available_USD)

    if currency == "USD":
        value_exchange = round(amount * value["UAH"]["course"], 2)
        if value_exchange <= available_UAH:
            value["UAH"]["availability"] = available_UAH - value_exchange
            return "UAH - {}, RATE - {} ".format(value_exchange, value["UAH"]["course"])
        else:
            return "UNAVAILABLE, REQUIRED BALANCE UAH {}, AVAILABLE {}".format(value_exchange, available_UAH)


def check_exchange_value_USD_0():
    test_value = "UAH - 0.0, RATE - 27.1 "
    assert check_exchange_value("USD", 0) == test_value


if __name__ == "__main__":
    check_course_currency_USD()
    check_exchange_value_USD_0()