using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] my_list = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11};
            // var result= SuanFa.Binary_search(my_list,1);
            var result = SuanFa.findSmallest(my_list);
            Console.WriteLine(result);

            Console.ReadKey();
        }
    }
}
