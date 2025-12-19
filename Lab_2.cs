using System;

// Абстрактный класс Геометрическая фигура
public abstract class GeometricFigure
{
    public virtual double CalculateArea()
    {
        return 0;
    }
}

// Интерфейс IPrint
public interface IPrint
{
    void Print();
}

// Класс Прямоугольник
public class Rectangle : GeometricFigure, IPrint
{

    public double Width { get; set; }
    
    public double Height { get; set; }
    
    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }
    
    /// Переопределение метода вычисления площади
    public override double CalculateArea()
    {
        return Width * Height;
    }
    
    /// Переопределение метода ToString()
    public override string ToString()
    {
        return $"Прямоугольник: ширина = {Width:F2}, высота = {Height:F2}, площадь = {CalculateArea():F2}";
    }
    
    /// Реализация метода Print() из интерфейса IPrint
    public void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

// Класс Квадрат
public class Square : Rectangle, IPrint
{
    /// Конструктор квадрата по длине стороны
    public Square(double side) : base(side, side)
    {
    }
    
    /// Переопределение метода ToString()
    public override string ToString()
    {
        return $"Квадрат: сторона = {Width:F2}, площадь = {CalculateArea():F2}";
    }
    
    /// Реализация метода Print() из интерфейса IPrint
    public new void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

// Класс Круг
public class Circle : GeometricFigure, IPrint
{

    public double Radius { get; set; }
    
    public Circle(double radius)
    {
        Radius = radius;
    }

    public override double CalculateArea()
    {
        return Math.PI * Radius * Radius;
    }
    
    /// Переопределение метода ToString()
    public override string ToString()
    {
        return $"Круг: радиус = {Radius:F2}, площадь = {CalculateArea():F2}";
    }
    
    /// Реализация метода Print() из интерфейса IPrint
    public void Print()
    {
        Console.WriteLine(this.ToString());
    }
}

// Основной класс программы
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Демонстрация работы с геометрическими фигурами");
        Console.WriteLine("=============================================");
        
        // Создание массива фигур
        GeometricFigure[] figures = new GeometricFigure[4];
        
        // Создание различных фигур
        figures[0] = new Rectangle(5, 3);
        figures[1] = new Square(4);
        figures[2] = new Circle(2.5);
        figures[3] = new Rectangle(7.5, 2);
        
        // Вывод информации о фигурах через метод Print()
        Console.WriteLine("\nВывод информации через метод Print():");
        Console.WriteLine("-------------------------------------");
        
        foreach (var figure in figures)
        {
            if (figure is IPrint printable)
            {
                printable.Print();
            }
        }
        
        // Демонстрация работы с отдельными фигурами
        Console.WriteLine("\nДемонстрация работы с отдельными фигурами:");
        Console.WriteLine("------------------------------------------");
        
        Rectangle rect = new Rectangle(10, 5);
        Square square = new Square(6);
        Circle circle = new Circle(3);
        
        rect.Print(); 
        square.Print();
        circle.Print();
        
        // Вычисление общей площади всех фигур
        Console.WriteLine("\nСтатистика:");
        Console.WriteLine("-----------");
        
        double totalArea = 0;
        foreach (var figure in figures)
        {
            totalArea += figure.CalculateArea();
        }
        
        Console.WriteLine($"Общая площадь всех фигур: {totalArea:F2}");
        
        Console.WriteLine("\nНажмите любую клавишу для выхода...");
        Console.ReadKey();
    }
}