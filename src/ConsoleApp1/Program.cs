using System;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] my_list = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11};
            int[] my_list1 = { 11, 10, 11, 5, 7, 6, 5, 4, 3, 2, 1, 0 };
            // var result= SuanFa.Binary_search(my_list,1);
            // var result = SuanFa.findSmallest(my_list);
            var ResultArry=  SuanFa.SelectSortMethod(my_list1);
            //var a = my_list1.OrderBy(s=>s);
            foreach (var item in ResultArry)
            {
                Console.WriteLine($"{item}");
            }
            //Console.WriteLine();
            //Console.WriteLine("--------------------------------------");
            //foreach (var item in a)
            //{
            //    Console.Write($"|{item}|");
            //}
            Console.ReadKey();
        }
    }
}
