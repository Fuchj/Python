using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApp1
{
    public class SuanFa
    {
        #region 二分查找
        /// <summary>
        /// 二分查找每个数
        /// </summary>
        /// <returns></returns>
        public static string Binary_search(int[] list, int item)
        {
            //定义查询需要的次数
            var num = 0;
            //查找范围的索引下限
            var low_index = 0;
            //查找范围的索引上限
            var high_index = list.Length - 1;
            //只要范围没有缩小到只包含一个元素
            while (low_index <= high_index)
            {
                num += 1;//没查询一次，次数加1
                var mid = (low_index + high_index) / 2;//2//向下取整 
                var guess = list[mid];//猜测的值
                if (guess == item)//当猜测的值和要查询的值相等时返回元素索引
                {
                    return $"的索引为{mid}查询次数为{num}";
                }
                else if (guess > item)//当猜测的值大于要查询的值相等时，说明猜测值的索引大于要查询值的索引，需要把查询范围的上限缩小
                {
                    high_index = mid - 1;
                }
                else//当猜测的值小于要查询的值相等时，说明猜测值的索引小于要查询值的索引，需要把查询范围的下限增大
                {
                    low_index = mid + 1;
                }
            }
            return $"值在数组中不存在,查询次数为{num}";
        }
        #endregion
        #region 选择排序
        /// <summary>
        /// 查找最小值的索引
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        public static int FindSmallest(int[] list)
        {
            var min_num = list[0];
            int min_index = 0;
            for (int i = 1; i < list.Length; i++)
            {
                if (list[i] < min_num)
                {
                    min_num = list[i];
                    min_index = i;
                }
            }
            return min_index;
        }
        /// <summary>
        /// 选择排序(从小到大)
        /// </summary>
        /// <param name="arry"></param>
        /// <returns></returns>
        public static int[] SelectSortMethod(int[] arry)
        {
            List<int> Arrylist = arry.ToList();
            List<int> ResultArry = new List<int>();
            while (Arrylist.Count > 0)
            {
                //找出数组中值最小的索引
                var min_index = FindSmallest(Arrylist.ToArray());
                ResultArry.Add(Arrylist[min_index]);
                Arrylist.RemoveAt(min_index);
            }
            return ResultArry.ToArray();
        }
        #endregion
    }
}
