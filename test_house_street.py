import unittest
from house_street_manager import House, Street, HouseStreet, DataManager, create_test_data


class TestHouseStreetManager(unittest.TestCase):
    """Тесты для менеджера домов и улиц"""
    
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.streets, self.houses, self.houses_streets = create_test_data()
        self.data_manager = DataManager(self.streets, self.houses, self.houses_streets)
    
    def test_task_g1_streets_starting_with_a(self):
        """Тест Г1: улицы, начинающиеся на 'А' и дома на них"""
        # Act
        result = self.data_manager.task_g1()
        
        # Assert
        self.assertEqual(len(result), 2, "Должно быть 2 улицы, начинающиеся на 'А'")
        
        street_names = [street for street, _ in result]
        self.assertIn('Арбат', street_names)
        self.assertIn('Авиамоторная', street_names)
        
        for street, houses in result:
            if street == 'Арбат':
                self.assertEqual(houses, ['15'])
            elif street == 'Авиамоторная':
                self.assertEqual(sorted(houses), ['3', '8'])
    
    def test_task_g2_max_floors_per_street(self):
        """Тест Г2: максимальная этажность на каждой улице"""
        # Act
        result = self.data_manager.task_g2()
        
        # Assert
        # Должно быть 4 улицы (Профсоюзная не включается, так как у нее нет домов в one_to_many)
        self.assertEqual(len(result), 4, "Должно быть 4 улицы с домами в связи 'один-ко-многим'")
        
        # Проверяем сортировку по убыванию этажности
        for i in range(len(result) - 1):
            self.assertGreaterEqual(result[i][1], result[i + 1][1],
                                   "Результат должен быть отсортирован по убыванию этажности")
        
        # Проверяем конкретные значения (только 4 улицы)
        result_dict = dict(result)
        self.assertEqual(result_dict['Ленинский проспект'], 16)
        self.assertEqual(result_dict['Тверская'], 12)
        self.assertEqual(result_dict['Арбат'], 5)
        self.assertEqual(result_dict['Авиамоторная'], 3)
        
        # Проверяем, что Профсоюзной НЕТ в результатах
        self.assertNotIn('Профсоюзная', result_dict, "Профсоюзная не должна быть в Г2 (нет домов в one_to_many)")
        
        # Проверяем порядок
        self.assertEqual(result[0][0], 'Ленинский проспект')
        self.assertEqual(result[0][1], 16)
        self.assertEqual(result[1][0], 'Тверская')
        self.assertEqual(result[1][1], 12)
        self.assertEqual(result[2][0], 'Арбат')
        self.assertEqual(result[2][1], 5)
        self.assertEqual(result[3][0], 'Авиамоторная')
        self.assertEqual(result[3][1], 3)
    
    def test_task_g3_all_relations_sorted_by_street(self):
        """Тест Г3: все связи домов и улиц, отсортированные по улицам"""
        # Act
        result = self.data_manager.task_g3()
        
        # Assert
        self.assertEqual(len(result), 9, "Должно быть 9 связей домов и улиц")
        
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i][2], result[i + 1][2],
                                "Результат должен быть отсортирован по названию улицы")
        
        street_names_in_result = set(item[2] for item in result)
        expected_streets = {'Арбат', 'Авиамоторная', 'Ленинский проспект', 'Тверская', 'Профсоюзная'}
        self.assertEqual(street_names_in_result, expected_streets)


if __name__ == '__main__':
    unittest.main(verbosity=2)