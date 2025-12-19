using System;

class Program
{
    static void Main(string[] args)
    {
        double a = 0, b = 0, c = 0;
        
        // Обработка параметров командной строки
        if (args.Length >= 3)
        {
            if (!double.TryParse(args[0], out a) || 
                !double.TryParse(args[1], out b) || 
                !double.TryParse(args[2], out c))
            {
                Console.WriteLine("Ошибка в параметрах командной строки");
                return;
            }
        }
        else
        {
            // Ввод с клавиатуры
            a = ReadCoefficient("A");
            b = ReadCoefficient("B");
            c = ReadCoefficient("C");
        }
        
        SolveBiquadratic(a, b, c);
    }
    
    static double ReadCoefficient(string name)
    {
        double coefficient;
        while (true)
        {
            Console.Write($"Введите коэффициент {name}: ");
            if (double.TryParse(Console.ReadLine(), out coefficient))
                return coefficient;
            Console.WriteLine("Некорректное значение, попробуйте еще раз");
        }
    }
    
    static void SolveBiquadratic(double a, double b, double c)
    {
        // Биквадратное уравнение: a*x⁴ + b*x² + c = 0
        // Делаем замену: t = x², получаем квадратное уравнение: a*t² + b*t + c = 0
        
        double discriminant = b * b - 4 * a * c;
        
        if (discriminant < 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Действительных корней нет");
            Console.ResetColor();
            return;
        }
        
        Console.ForegroundColor = ConsoleColor.Green;
        
        double t1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
        double t2 = (-b - Math.Sqrt(discriminant)) / (2 * a);
        
        Console.WriteLine($"Корни уравнения:");
        
        if (t1 >= 0)
        {
            double x1 = Math.Sqrt(t1);
            double x2 = -Math.Sqrt(t1);
            Console.WriteLine($"x₁ = {x1:F4}, x₂ = {x2:F4}");
        }
        
        if (t2 >= 0 && t2 != t1)
        {
            double x3 = Math.Sqrt(t2);
            double x4 = -Math.Sqrt(t2);
            Console.WriteLine($"x₃ = {x3:F4}, x₄ = {x4:F4}");
        }
        
        Console.ResetColor();
    }
}