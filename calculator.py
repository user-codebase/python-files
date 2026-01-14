import logging
logging.basicConfig(level=logging.INFO)


def get_user_input():
    type_of_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    input_numbers = []
    i = 1
    while len(input_numbers) < 2:
        user_input = input(f"Podaj składnik {i}. ")
        try:
            number = float(user_input)
            input_numbers.append(number)
            i += 1
        except ValueError:
            logging.warning(f"Podałeś niepoprawne dane. Wymagane jest podanie liczby.")
    return {type_of_operation: input_numbers}


def display_information_about_operation(data_for_operation):
    operation_id = list(data_for_operation.keys())[0]
    numer_inputs = f"{data_for_operation[operation_id][0]} i {data_for_operation[operation_id][1]}"
    if operation_id == "1":
        logging.info(f"Dodaję {numer_inputs}")
    elif operation_id == "2":
        logging.info(f"Odejmuję {numer_inputs}")
    elif operation_id == "3":
        logging.info(f"Mnożę {numer_inputs}")
    elif operation_id == "4":
        logging.info(f"Dzielę {numer_inputs}")
    else:
        logging.info("Niepoprawne ID operacji.")

def perform_operation(data_for_operation):
    operation_id = list(data_for_operation.keys())[0]
    list_with_numbers = data_for_operation[operation_id]
    if operation_id == "1":
        return list_with_numbers[0] + list_with_numbers[1]
    elif operation_id == "2":
        return list_with_numbers[0] - list_with_numbers[1]
    elif operation_id == "3":
        return list_with_numbers[0] * list_with_numbers[1]
    elif operation_id == "4":
        if data_for_operation[operation_id][1] == 0:
            logging.error("Operacja nie może być zrealizowana, ponieważ nie można dzielić przez zero.")
            return "Error"
        return list_with_numbers[0] / list_with_numbers[1]


if __name__ == "__main__":
    user_input = get_user_input()
    display_information_about_operation(user_input)
    result = perform_operation(user_input)
    logging.info(f"Wynik: {result}")