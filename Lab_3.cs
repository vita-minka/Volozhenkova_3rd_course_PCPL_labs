using System;
using System.Collections.Generic;
using System.Linq;

// Сотрудник
public class Employee
{
    public int EmployeeID { get; set; }      
    public string LastName { get; set; }     
    public int DepartmentID { get; set; }    
    
    public Employee(int id, string lastName, int departmentId)
    {
        EmployeeID = id;
        LastName = lastName;
        DepartmentID = departmentId;
    }
}

// Отдел
public class Department
{
    public int DepartmentID { get; set; }    
    public string Name { get; set; }         
    
    public Department(int id, string name)
    {
        DepartmentID = id;
        Name = name;
    }
}

// Сотрудники отдела
public class EmployeeDepartment
{
    public int EmployeeID { get; set; }      
    public int DepartmentID { get; set; }    
    
    public EmployeeDepartment(int employeeId, int departmentId)
    {
        EmployeeID = employeeId;
        DepartmentID = departmentId;
    }
}

class Program
{
    static void Main(string[] args)
    {
        
        // Создаем тестовые данные - отделы
        List<Department> departments = new List<Department>
        {
            new Department(1, "IT отдел"),
            new Department(2, "Бухгалтерия"),
            new Department(3, "Отдел кадров"),
            new Department(4, "Отдел продаж")
        };

        // Создаем тестовые данные - сотрудники
        List<Employee> employees = new List<Employee>
        {
            new Employee(1, "Иванов", 1),
            new Employee(2, "Петров", 1),
            new Employee(3, "Александров", 2),
            new Employee(4, "Андреев", 2),
            new Employee(5, "Абрамов", 3),
            new Employee(6, "Сидоров", 3),
            new Employee(7, "Анисимов", 4),
            new Employee(8, "Кузнецов", 4),
            new Employee(9, "Азорова", 4),
            new Employee(10, "Гаусс", 4),
            new Employee(11, "Селиманова", 2)
        };

        // Создаем данные для связи многие-ко-многим
        List<EmployeeDepartment> employeeDepartments = new List<EmployeeDepartment>
        {
            new EmployeeDepartment(1, 1),
            new EmployeeDepartment(2, 1),
            new EmployeeDepartment(3, 2),
            new EmployeeDepartment(4, 2),
            new EmployeeDepartment(5, 3),
            new EmployeeDepartment(6, 3),
            new EmployeeDepartment(7, 4),
            new EmployeeDepartment(8, 4),
            new EmployeeDepartment(1, 4), 
            new EmployeeDepartment(3, 1)  // Один сотрудник может быть в нескольких отделах
        };

        Console.WriteLine("один-ко-многим\n");

        //Список всех сотрудников, у которых фамилия начинается с буквы «А»
        Console.WriteLine("\nСотрудники с фамилией на 'А':");
        var query1 = from emp in employees
                     where emp.LastName.StartsWith("А")
                     select emp;

        foreach (var emp in query1)
        {
            Console.WriteLine($"   {emp.LastName}");
        }

        //Список всех отделов и количество сотрудников в каждом отделе
        Console.WriteLine("\nКоличество сотрудников по отделам (один-ко-многим):");
        var query2 = from emp in employees
                     group emp by emp.DepartmentID into g
                     join dep in departments on g.Key equals dep.DepartmentID
                     select new { Department = dep.Name, Count = g.Count() };

        foreach (var item in query2)
        {
            Console.WriteLine($"   Отдел: {item.Department} Сотрудников: {item.Count}");
        }

        
        Console.WriteLine("\nКоличество сотрудников по отделам (многие-ко-многим):");
        var query7 = from ed in employeeDepartments
                    join emp in employees on ed.EmployeeID equals emp.EmployeeID
                    join dep in departments on ed.DepartmentID equals dep.DepartmentID
                    group emp by dep into g
                    select new { Department = g.Key.Name, Count = g.Count() };

        foreach (var item in query7)
        {
            Console.WriteLine($"Отдел: {item.Department}, Сотрудников: {item.Count}");
        }


        // Демонстрация отличия между связями один-ко-многим и многие-ко-многим
        Console.WriteLine("СРАВНЕНИЕ РЕЗУЛЬТАТОВ:\n");




        Console.WriteLine("Количество сотрудников по отделам (один-ко-многим):");
        foreach (var item in query2.OrderBy(x => x.Department))
        {
            Console.WriteLine($"   {item.Department}: {item.Count} сотрудников");
        }

        
        
        Console.WriteLine("\nКоличество сотрудников по отделам (многие-ко-многим):");
        foreach (var item in query7.OrderBy(x => x.Department))
        {
            Console.WriteLine($"   {item.Department}: {item.Count} сотрудников");
        }
    }
}