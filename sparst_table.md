```
http://blog.csdn.net/alongela/article/details/8143016
```

Sparse Table算法，简称ST算法，可以用来求解RMQ（区间最值查询）问题。
RMQ问题的形式一般是：存在一个大数组，要求对于给定的起点和终点，迅速回答出这段区间的最大值或最小值。
朴素的方式是扫描起点到终点的所有数，维护其中的最值，这样的复杂度是O(n^2)的，速度太慢。ST算法是使用的是类似于二分的动态规划思想，其复杂度是O(nlogn)，因此查询速度非常快。

ST算法的执行过程（以求最大值为例）：

1、初始化：
设原数组为x[N]。

开辟一个数组dp[N][33]。其中dp[i][j]表示的是从下标为i的元素开始，到下标为(i + 2^j - 1)的元素为止，这些元素中的最大值。对于整型而言，其值不会超过2^32，因此第二维大小为33已经足够。
因此dp[i][0]表示的是元素本身，因此可以初始化为dp[i][0] = x[i]。

对于其他的dp[i][j]，可以采用动态规划的方式求出，递推式为dp[i][j] = max(dp[i][j - 1], dp[i + 2 ^ (j - 1)][j - 1])，其实就是把一段区间切成两段大小相等的区间，当前区间的最大值就是两个子区间的最大值中的较大者。

初始化的复杂度为O(nlogn)。

2、求解：
对于给定的起点beg及终点end，可以得出区间大小为range = end - beg + 1。

因此可以找到一个整数k = (int)(log(range) / log2)。这样区间就可以被划分为子区间1，即[beg, beg + (2 ^ k) - 1]，子区间2，即[end - (2 ^ k) + 1, end]。这两个可能会有重叠，但重叠不会影响最大值的求解。因此对于beg和end，可以得到解为res = max(dp[beg][k], dp[end - (2 ^ k) + 1][k])。
求解的复杂度为O(1)。

值得注意的是使用log求解k的速度比较慢，可以使用乘法来计算k，这样速度会相对快一些。

具体方法是：
```
k = 0, x = 2, range = end - beg + 1;
while (x <= range)
{
k++;
x <<= 1;
} 
```

对于某个RMQ问题，总的复杂度为
```
O(nlogn) + n * O(1) = O(nlogn)
```
，因此可以在足够快的时间内得到区间的最大值或最小值。
