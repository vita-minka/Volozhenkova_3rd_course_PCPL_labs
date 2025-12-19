from operator import itemgetter
from typing import List, Tuple


class House:
    """Дом"""
    def __init__(self, id: int, number: str, floors: int, street_id: int):
        self.id = id
        self.number = number  # номер дома
        self.floors = floors  # количество этажей
        self.street_id = street_id


class Street:
    """Улица"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class HouseStreet:
    """'Дома на улицах' для реализации связи многие-ко-многим"""
    def __init__(self, street_id: int, house_id: int):
        self.street_id = street_id
        self.house_id = house_id


class DataManager:
    """Менеджер данных для работы с домами и улицами"""
    
    def __init__(self, streets: List[Street], houses: List[House], houses_streets: List[HouseStreet]):
        self.streets = streets
        self.houses = houses
        self.houses_streets = houses_streets
    
    def get_one_to_many(self) -> List[Tuple[str, int, str]]:
        """Соединение данных один-ко-многим"""
        return [
            (h.number, h.floors, s.name)
            for s in self.streets
            for h in self.houses
            if h.street_id == s.id
        ]
    
    def get_many_to_many(self) -> List[Tuple[str, int, str]]:
        """Соединение данных многие-ко-многим"""
        many_to_many_temp = [
            (s.name, hs.street_id, hs.house_id)
            for s in self.streets
            for hs in self.houses_streets
            if s.id == hs.street_id
        ]
        
        return [
            (h.number, h.floors, street_name)
            for street_name, street_id, house_id in many_to_many_temp
            for h in self.houses
            if h.id == house_id
        ]
    
    def task_g1(self) -> List[Tuple[str, List[str]]]:
        """Список всех улиц, начинающихся на 'А', и домов на них"""
        one_to_many = self.get_one_to_many()
        result = []
        
        for s in self.streets:
            if s.name.startswith('А'):
                s_houses = list(filter(lambda i: i[2] == s.name, one_to_many))
                if len(s_houses) > 0:
                    result.append((s.name, [house_num for house_num, _, _ in s_houses]))
        
        return result
    
    def task_g2(self) -> List[Tuple[str, int]]:
        """Список улиц с максимальной этажностью домов на каждой улице"""
        # ВАЖНО: Используем many_to_many, чтобы включить ВСЕ улицы
        # (включая Профсоюзную, которая есть только в many_to_many)
        many_to_many = self.get_many_to_many()
        result_unsorted = []
        
        # Для каждой улицы ищем дома в many_to_many
        for s in self.streets:
            s_houses = list(filter(lambda i: i[2] == s.name, many_to_many))
            if len(s_houses) > 0:
                s_floors = [floors for _, floors, _ in s_houses]
                max_floors = max(s_floors)
                result_unsorted.append((s.name, max_floors))
        
        return sorted(result_unsorted, key=itemgetter(1), reverse=True)
    
    def task_g3(self) -> List[Tuple[str, int, str]]:
        """Список всех связанных домов и улиц, отсортированный по улицам"""
        many_to_many = self.get_many_to_many()
        return sorted(many_to_many, key=itemgetter(2))


def create_test_data():
    """Создание тестовых данных"""
    streets = [
        Street(1, 'Арбат'),
        Street(2, 'Ленинский проспект'),
        Street(3, 'Тверская'),
        Street(4, 'Авиамоторная'),
        Street(5, 'Профсоюзная'),
    ]
    
    houses = [
        House(1, '15', 5, 1),
        House(2, '25', 9, 2),
        House(3, '10', 12, 3),
        House(4, '8', 3, 4),
        House(5, '42', 16, 2),
        House(6, '7', 7, 3),
        House(7, '3', 2, 4),
    ]
    
    houses_streets = [
        HouseStreet(1, 1),
        HouseStreet(2, 2),
        HouseStreet(2, 5),
        HouseStreet(3, 3),
        HouseStreet(3, 6),
        HouseStreet(4, 4),
        HouseStreet(4, 7),
        HouseStreet(5, 1),
        HouseStreet(5, 3),
    ]
    
    return streets, houses, houses_streets


def main():
    """Основная функция"""
    streets, houses, houses_streets = create_test_data()
    data_manager = DataManager(streets, houses, houses_streets)
    
    print('Задание Г1')
    res_1 = data_manager.task_g1()
    print(res_1)
    
    print('\nЗадание Г2')
    res_2 = data_manager.task_g2()
    print(res_2)
    
    print('\nЗадание Г3')
    res_3 = data_manager.task_g3()
    print(res_3)


if __name__ == '__main__':
    main()