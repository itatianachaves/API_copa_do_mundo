
from exceptions import ImpossibleTitlesError
from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError

def data_processing(selection_info):
    titles = selection_info.get('titles')
    first_cup = int(selection_info.get('first_cup')[:4])

    if titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if first_cup < 1930 or (first_cup - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    
    max_possible_titles = (2023 - first_cup) // 4 + 1
    if titles > max_possible_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

    return True