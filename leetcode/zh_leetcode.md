## 191. Number of 1 Bits (Easy)
### **链接**：
题目：https://leetcode.com/problems/number-of-1-bits/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
计算一个数二进制里 1 的个数。
### **分析**：
跟 [190. Reverse Bits (Easy)]https://github.com/illuz/leetcode/tree/master/solutions/190.Reverse_Bits) 一样。  
1. 先转 string 再计算
2. 或者用位运算来算 （Java 实现时要用 `>>>` 来进行位移，因为 `>>` 是会移到符号位的，`>>>` 是用来操作 unsigned 数的）
3. C++ Trick: 用 `bitset` 的 `count`
4. Python Trick: 用 `bin()` 和 `count()`
## 190. Reverse Bits (Easy)
### **链接**：
题目：https://leetcode.com/problems/reverse-bits/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
将一个 32 位无符号的数的二进制反转。
### **分析**：
1. 正常都是想先转 string 再转回去
2. 或者用位运算来反转
3. C++ Trick: 用 `bitset`
4. Python Trick: 用 `bin()` 和 `zfill()`
5. Java Trick: 用 `Integer.reverse()`
## 189. Rotate Array (Easy)
### **链接**：
题目：https://leetcode.com/problems/rotate-array/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一个数组左旋转 k 步。如 `[1,2,3,4,5,6,7]` is rotated to `[5,6,7,1,2,3,4]`。
### **分析**：
这题很容易，模拟一下就能出来了。  
不过如果要用 O(1) 的空间就要想想了。  
把 `[0, n-k-1]` 和 `[n-k,n-1]` 看成一个单词，这样就和 [151 Reverse Words in a String](https://github.com/illuz/leetcode/tree/master/solutions/151.Reverse_Words_in_a_String) 一样可以 O(1) 的空间完成了。
## 188. Best Time to Buy and Sell Stock IV (Hard)
### **链接**：
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个数组，prices[i] 表示第 i 天的交易值，也就是你在这天买入或卖出的交易值。  
你可以买入及卖出**最多k轮**，不过你一个时间只能拥有一个股票，求最大盈利。
### **分析**：
只要理解了 [`123. Best Time to Buy and Sell Stock III `](https://github.com/illuz/leetcode/tree/master/solutions/123.Best_Time_to_Buy_and_Sell_Stock_III) 的那个 O(1) 空间的算法，这个也可以那样变形过来。  
注意，如果 k 大于数组的大小的一半，那就可以每相邻两天都能买了，所以可以直接用 III 版本的算法 O(n) 解决。
## 183. Customers Who Never Order (Easy)
### **链接**：
题目：https://leetcode.com/problems/customers-who-never-order/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
从两个表中得到从没买过东西的家伙。
## 184. Department Highest Salary (Medium)
### **链接**：
题目：https://leetcode.com/problems/department-highest-salary/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给俩表，求各个部门的最高工资的人。
### **分析**：
直接 SELECT JOIN MAX 一通用就行了。
## 180. Consecutive Numbers (Medium)
### **链接**：
题目：https://leetcode.com/problems/consecutive-numbers/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
查询一个表中连续出现 3 次一上的 Num。
### **分析**：
1. 用 JOIN 三个表可以做，不过要跑 1800 ms，而且只有在 id 都是连续的情况下才可行。
2. 有更好的解法，就是用 CASE，不过也是要跑 1600 ms。
## 178. Rank Scores (Medium)
### **链接**：
题目：https://leetcode.com/problems/rank-scores/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给分数排名。
### **分析**：
1. 把 SELECT 套进去。
2. 用 CASE 和 变量，逐行处理，速度比 1 变了很多。
## 177. Nth Highest Salary (Medium)
### **链接**：
题目：https://leetcode.com/problems/nth-highest-salary/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求第 N 大的工资。
### **分析**：
[176.Second_Highest_Salary](https://github.com/illuz/leetcode/tree/master/solutions/176.Second_Highest_Salary) 的变形题。  
算法题做多了，我一下就写了个递归，然后被告知 SQL 不能用递归。  
可以用 `ORDER BY` 排序，再用 `LIMIT` 返回第 N 大值。  
题目要求返回值是 INT 或 NULL，所以我们可以用 `DISTINCT` 或用 `IFNULL(..., NULL)`。
## 173. Binary Search Tree Iterator (Medium)
### **链接**：
题目：https://leetcode.com/problems/binary-search-tree-iterator/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
实现一个 BST 的类。
### **分析**：
1. **(C++)** 初始化的时候就将中序遍历处理好，保存在 queue 里
2. **(Python)** 用 stack 做，一边求一边处理即可。
3. Morris Travese Tree，可以用 O(1) 的空间解决这题，详见 [099. Recover Binary Search Tree (Hard)](https://github.com/illuz/leetcode/blob/master/solutions/099.Recover_Binary_Search_Tree)
## 199. Binary Tree Right Side View (Medium)
### **链接**：
题目：https://leetcode.com/problems/binary-tree-right-side-view/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
假设你站在一棵树的右边，问从上到下看到的节点。
### **分析**：
其实就是求树每一层的最右边节点。  
1. **(Python)** 可以直接 DFS 遍历一遍，维护最右节点就行了。
2. **(C++)** 也可以用两个 queue 来实现层次遍历。
## 166. Fraction to Recurring Decimal (Medium)
### **链接**：
题目：https://leetcode.com/problems/fraction-to-recurring-decimal/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
计算除法循环节。
### **分析**：
直接模拟即可。
## 164. Maximum Gap (Hard)
### **链接**：
题目：https://leetcode.com/problems/maximum-gap/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给你一个无序的数列，问在排序中相邻两数之差的最大值是多少，要求线性时间复杂度。
### **分析**：
比较排序的下限都是 O(nlogn)，如果要排序的话，就不能用比较排序了。  
那就不能排序了吗？不，我们可以考虑非比较排序：桶排序。  
很明显：相邻两数之差最小是 `bucketLen=(max-min)/(len-1)`。  
我们可以把数据范围(min~max)，分为 `(max-min)/bucketLen + 1` 个区间，而两数之差的最大值一定在区间之间产生。  
我们只需统计区间的最大最小值，然后判断后区间最小值和前区间最大值之差即可。
## 154. Find Minimum in Rotated Sorted Array II (Hard)
### **链接**：
题目：https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在一个旋转过的有序数组中找最小的数。不过里面的数有重复。
### **分析**：
与[上一题](https://github.com/illuz/leetcode/tree/master/solutions/153.Find_Minimum_in_Rotated_Sorted_Array) 差不多，不过在判断到前后相同时，不能一下子就判断，要把范围向内缩。  
因此，这个解法复杂度最坏是 O(n) 是全部都一样的数的。
## 153. Find Minimum in Rotated Sorted Array (Medium)
### **链接**：
题目：https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在一个旋转过的有序数组中找最小的数。
### **分析**：
跟 [033. Search in Rotated Sorted Array](https://github.com/illuz/leetcode/tree/master/solutions/033.Search_in_Rotated_Sorted_Array) 很像，同样是二分的变形。  
二分的时候分类讨论就行了。
## 151. Reverse Words in a String (Medium)
### **链接**：
题目：https://leetcode.com/problems/reverse-words-in-a-string/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
反转句子里的单词。
### **分析**：
1. **(C++)** 用 stringstream 可以很方便求出来，不过空间还是用得不少。时间复杂度 O(n)，空间 O(n)。
2. **(Java)** 用 `String` 的 `trim` 和 `split` 分成字符串数组，再处理
3. **(Python)** 一句话就行了。
4. **(C)** 如何达到 O(1) 空间？这才是这题真正考察的地方。其实只要反转每个单词，最后再反转整个句子就行了。时间复杂度同样是 O(n)。
## 150. Evaluate Reverse Polish Notation (Medium)
### **链接**：
题目：https://leetcode.com/problems/evaluate-reverse-polish-notation/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求一个逆波兰式的值。
### **分析**：
很经典的栈应用。  
对字符串的处理，Python: `int()`，C++/C: `atoi()`，Java: `Integer.parseInt()`。  
需要注意的是 Python 的 `/` 操作。
## 148. Sort List (Medium)
### **链接**：
题目：https://leetcode.com/problems/sort-list/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给链表排序，只能用 O(nlogn) 时间和 O(1) 空间。
### **分析**：
把排序算法筛选一遍吧：  
非比较排序如桶排和计数排序需要不少的空间，pass。  
冒泡复杂度不够，pass。  
插入排序可以用二分实现 O(nlogn)，但没辅助空间，链表无法实现随机存取，pass。  
堆排也要堆做辅助空间，拿原链表做堆也不成，链表不好实现堆，pass。  
快排要递归，要用最坏的 O(n) 栈空间，pass。  
分治好像很靠谱，不过也要递归，要 O(logn) 栈空间，pass。  
没算法了...  
不，分治已经很靠谱了，如果能变成非递归的版本就可以了。  
你还记得当年 [143. Reorder List](https://leetcode.com/problems/Reorder-List/) 的 merge 递归转非递归吗？  
没错，用这思路就可以了。  
这里引用[大神的解释](https://leetcode.com/discuss/10264/my-o-n-log-n-time-o-1-space-solution)下：  
> Round #1 block_size = 1  
> (a1, a2), (a3, a4), (a5, a6), (a7, a8)  
> Compare a1 with a2, a3 with a4 ...  
> Round #2 block_size = 2  
> (a1, a2, a3, a4), (a5, a6, a7, a8)  
> merge two sorted arrays (a1, a2) and (a3, a4), then merge tow sorted arrays(a5, a6) and (a7, a8)  
> Round #3 block_size = 4  
> (a1, a2, a3, a4, a5, a6, a7, a8)  
> merge two sorted arrays (a1, a2, a3, a4), and (a5, a6, a7, a8)  
PS：这题的 Python 用 O(1) 去做很难过的，见 [Anyone solve this in Python](https://leetcode.com/discuss/3344/anyone-solve-this-in-python)
## 149. LRU Cache (Hard)
### **链接**：
题目：https://leetcode.com/problems/lru-cache/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
实现一个 LRU 缓冲区的类。
### **分析**：
LRU 不难理解，问题是要怎么高效地去实现它。  
LRU 会有频繁的读改操作，所以要有合适的数据结构来让 set 和 get 的复杂度很小，最好近 O(1)。  
已经有人讨论过这个问题了：[What is the best way to Implement a LRU Cache? - Quora](http://www.quora.com/What-is-the-best-way-to-Implement-a-LRU-Cache)。  
1. 用 Splay 实现，Splay 是棵 BST，同时在查找和修改的时候会让那个节点上浮到根节点，不过操作都是 O(log(n)) 级别的，而且有个问题，就是这棵树可能会变成一条链（正常节点都是按查询频率从上到下，所以很快，均摊小于 O(log(n))）。Splay 太麻烦，这里就不给出。
2. 用双链表和 HashMap 实现，链表的作用是记录节点的使用顺序。正常情况下 LRU 都是用这种做法的。
    1. HashMap 实现用 key 找到 List 中的节点对象（C++ 中就是迭代器了），找不到就在 List 中增加节点，并插入 HashMap。
    2. 按照要求得到或修改节点的 value。
    3. 修改节点的使用时间，也就是把 List 中的节点拉到 List 头部。
    4. 在第一步时如果节点个数大于可用容量，就将 List 的最后一个节点删去。  
用 Python 的 OrderedDict 可以一下将 HashMap 和 List 都实现。
## 139. Word Break (Medium)
### **链接**：
题目：https://leetcode.com/problems/word-break/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个字符串和一个字典，问这个字符串能否用字典中的单词拼接成。
### **分析**：
1. 直接暴力地把字符串切割了，是 O(2^n) 复杂度，必须超时。（这里用 DFS 实现）
2. 很明显，暴力做了太多的重复问题，所以可以在 DFS 时记忆化一下，当然也可以用 DP 转移公式来做：`dp[i][j] = dp[i][k] && dp[k][j]，(i<k<j)`，复杂度是 `O(n^3)`
3. 还有另外一种 DP，`dp[i]` 表示 `S{0~i}` 是否有解，公式就是 `dp[i] = true (if s{j~i} in dict and dp[j] is true)`。
## 138  Copy List with Random Pointer
### **链接**：
题目：https://leetcode.com/problems/copy-list-with-random-pointer/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求一个链表的完全复制。
### **分析**：
刚开始想，每个节点两个指针，这不跟二叉树一样吗？但是太天真，树是没有环的，这个又没说有没有环，有环也是合法的。  
1. **(Python)**深复制不是很难，只要把 `<label, newNode>` 都保存下来，要用的时候拿来用就可以了。不过这要花上 O(n) 的空间，不是很值。（用 Python 可以用 `collections.defaultdict` 一气呵成）
2. **(C++)** 递归 + Hash 节点，不过不仅要用到 O(n) 的 Hash 空间，还要有栈的花费，还不知道会不会太深爆栈，不是很好的解。
3. **(Java)** 不会 O(1) space 解法 QAQ，Discuss 里倒是有不少自称 O(1) space，其实都是用了 O(n) space 的。不过思路是不错，就是在每个旧节点后面插一个新节点，再复制一遍，再去掉旧节点，共三次遍历。（这里用的是 Java，所以去掉旧节点时不用特地去释放旧节点，因为有 GC 机制，不过用的 C/C++ 时，最好手动去 release，不然内存泄露）
(1) 空间的解法请不要吝啬来教我。</s>  
Discuss 上的人说，这个题目要完全复制，所以至少要 O(n) 的空间来放节点，所以可以不去考虑节点的空间。  
这样一来，1，2 的解法还是 O(n) 空间，因为要用到 hash 表，不过 3 的解法就是 O(1) 没错了。  
## 200. Number of Islands (Medium)
### **链接**：
题目：https://leetcode.com/problems/number-of-islands/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
算一张 01 里面有几个 1 块。
### **分析**：
直接 BFS 就行了。  
当然 DFS 也可以，这题没太大数据会卡 DFS。
## 134. Gas Station (Medium)
### **链接**：
题目：https://leetcode.com/problems/gas-station/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
提供数组 gas、cost，gas表示第i个点的汽油量，cost表示从i到i+1所需的汽油量，问是否有一点，出发能驶过所有点(路径是环)。
### **分析**：
1. 暴力枚举每个点，走一遍。复杂度是 O(n^2)，不理想。
2. 考虑从 i 点出发，只能走到 j 点，其原因是从 i 到 j 积累的汽油量 `sum_gas[i~j]` 不够从 j 到 j+1 的费用 `cost[j]`，因为 gas，cost 都是非负的，所以即使从 [i,j] 中的一个点出发，积累的汽油量也不会大于 `sum_gas[i~j]` 的，所以从 [i,j] 出发是徒劳的，一旦走失败了，就可以跳过 [i,j] 从 j+1 开始，这样就可以很大的优化了。复杂度是 O(n)。
## 132. Palindrome Partitioning II (Hard)
### **链接**：
题目：https://leetcode.com/problems/palindrome-partitioning-ii/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一个字符串分割，使每一部分都是回文。问最少的割数。
### **分析**：
1. **(C++)** 跟上题一样，递归求过去，不过会 TLE
2. 优化一，考虑对 1 进行优化，可以预处理子串是否是回文，就不用在这步重复算了
3. 优化二，既然可以用 DFS，当然可以记忆化了
4. **(Java)** 既然可以用记忆化，当然可以写成 DP 了
5. **(C++)** 在 DP 的时候，可以不用预处理判断是否回文，直接分奇偶讨论，见：[not need a table for palindrome](https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space)
## 131. Palindrome Partitioning (Medium)
### **链接**：
题目：https://leetcode.com/problems/palindrome-partitioning/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一个字符串分割，使每一部分都是回文。
### **分析**：
1. **(C++)** 递归，找到回文，然后递归后面部分
2. **(Python)** 对 1 进行优化，预处理每个位置对应的回文
## 130. Surrounded Regions (Medium)
### **链接**：
题目：https://leetcode.com/problems/surrounded-regions/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个地图，把地图里被 X 包围的 O 块填充为 X。
### **分析**：
1. 找到 O 点就 DFS 填充。不过 DFS 递归是要占用栈的，最糟的空间复杂度是 O(n*n)，这题会卡爆栈，所以 DFS 会 Memory Limit Exceed。  
2. 找到 O 点就 BFS 填充。BFS 才是正解。  
不过一找到 O 就开始处理的话，如果来个全是 O 的，时间复杂度就会变成 O(n*n) 了，就会 TLE，有两种解决方案：1. 开个数组来记录是否访问过，需要 O(n*n) 的空间；2. 遍历 O 的时候把遍历过的 O 而不用变 X 的点变成 +，全部处理后再变回来，这样就不用另开空间了。  
在上面的“把遍历过的 O 而不用变 X 的点变成 +”这个方法中，如果正常去做就要先来一遍 BFS 看看有没有被包围，再一遍 BFS 变点。能不能把两遍 BFS 缩成一遍呢？其实是可以的，我们还是把不用变的化作 '+'，那反过来想，我们只要处理需要化作 '+' 的点不就行了，找到边界的点再 BFS 把 O 变成 +，最后处理时还是 O 的就是可以填充的点了。  
## 127. Word Ladder (Medium)
### **链接**：
题目：https://leetcode.com/problems/word-ladder/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给出起点，终点的单词，每次变换要从 dict 中找到一个单词，且只变换一个字母。  
问从起点到终点的最短变换路径长度。
### **分析**：
这是图论的题，把每个单词看成点，能变换就在点间连一条边，这样就出现一张无向图了。  
1. BFS 一遍就行了。
2. 从起点和终点一起开始 BFS，就是 双端BFS(two-end BFS)。  
对于图，可以先构造，也可以在 BFS 的时候再判断。
## 124. Binary Tree Maximum Path Sum (Hard)
### **链接**：
题目：https://leetcode.com/problems/binary-tree-maximum-path-sum/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求一棵二叉树上的最大路径。
### **分析**：
直接 DFS 就可以了，返回以这一棵子树且一端在上的最大路径，然后维护一个最大路径就行了。
## 123. Best Time to Buy and Sell Stock III (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
给一个数组，`prices[i]` 表示第 i 天的交易值，也就是你在这天买入或卖出的交易值。  
你可以买入及卖出**最多两轮**，不过你一个时间只能拥有一个股票，求最大盈利。  
  
### **分析**：  
  
可以最多求两次，所以可以把它变成子问题，也就是枚举分界点，求左右两个子串的只能交易一次的最大值。  
子问题要递归解决吗？NO！跟 `121. Best Time to Buy and Sell Stock` 一样，子问题的解决是需要 O(n) 的，总的就是 O(n^2) 这跟暴力没有区别。  
所以我们就要用空间换时间了，只要预处理左子序列和右子序列的单次交易值 left[n] 和 right[n] 就行了，然后枚举分界点求 `max(left[i], right[i+1])` 就行了。总的复杂度是 O(n)。  
  
有没有办法不用 O(n) 的空间？  
大神告诉我们，有的：https://leetcode.com/discuss/18330/is-it-best-solution-with-o-n-o-1。  
假设刚开始持有 0 元，只用 4 个变量，分别是两次交易买入后和卖出后所持钱的最大值，一遍扫过去，维护这些变量就行了。  
其实还是不太好理解的。  
## 122. Best Time to Buy and Sell Stock II (Medium)
### **链接**：
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个数组，`prices[i]` 表示第 i 天的交易值，也就是你在这天买入或卖出的交易值。  
你可以买入及卖出多轮，不过你一个时间只能拥有一个股票，求最大盈利。
### **分析**：
刚开始以为一天只能交易一次，没想到同一天你可以先卖出再买入。  
这样就很容易了，贪心就行了，考虑 [1, 2, 3]，你可以 [-1, +2-2, +3]，跟 [-1, +3] 是一样的，也就是说只要比前一天多，你就可以在前一天买入，接下去一天卖出，这样稳赚不赔。  
用 Python 可以用一句话解决~
## 121. Best Time to Buy and Sell Stock (Medium)
### **链接**：
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个数组，`prices[i]` 表示第 i 天的交易值，也就是你在这天买入或卖出的交易值。  
你只能买入及卖出一轮，求最大盈利。
### **分析**：
只要 `profit = prices[sell] - prices[buy] && buy < sell` 就行了，遍历一遍，维护 `profit` 即可。
## 114. Flatten Binary Tree to Linked List (Medium)
### **链接**：
题目：https://leetcode.com/problems/flatten-binary-tree-to-linked-list/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一棵树变成一长条。
### **分析**：
1. (**C++**)DFS，先把左右两边的子树处理好，再合并。
2. (**Java**)不递归而用 Stack 来做。  
这两种做法的时间复杂度和最坏空间都是 O(n)。
## 198.House Robber (Easy)
### **链接**：
题目：https://leetcode.com/problems/house-robber/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在一个序列中取数，不能连续取，求最大和。
### **分析**：
很明显的 DP，公式是 `dp[i] = max(dp[i - 1], dp[i - 2] + num[i])`。  
你可以开个 DP 数组，不过这样就要用 O(n) 的空间了。  
从公式中很容易看出这是可以降维的，滚动地 DP 只要 O(1) 的空间。
## 115. Distinct Subsequences (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/distinct-subsequences/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
问有 S 中有几个子串是 T，S 的子串定义为在 S 中任意去掉 0 个或者多个字符形成的串。  
  
### **分析**：  
  
很明显得用 DP。  
有两种 DP 思路：  
  
1. 首先想到化为子问题：`dp[i][j]` 表示 `S[i...j]` 中有几个 `T`，但是转移不好想，而且 `dp[i][j]` 需要 O(n*n) 的空间，如果 S 长度大点就不行了。  
2. 正解：`dp[i][j]` 表示 `S[1...i]` 与 `T[1...j]` 匹配的个数。转移公式就是：`dp[i][j]=dp[i][j-1]{(if S[i]==T[j])+dp[i-1][j-1]}`。这思路也可以用记忆化来想，也是子问题。  
3. 对 2 进行优化，用滚动数组来减小空间，倒着滚可以降成一维。  
  
复杂度都是 O(n*m)。  
PS：听说开数组时从小到大开比较快，如 `dp[10][1000]` 会比 `dp[1000][10]` 快。（虽然我这没这样开）  
  
C++ 实现了空间 O(n*m) 的 DP 和 O(m) 的一维 DP。  
Python 实现了空间 O(2m) 的 DP。  
## 109. Convert Sorted List to Binary Search Tree (Medium)
### **链接**：
题目：https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
为一个排过序的链表建一棵平衡的 BST。
### **分析**：
1. 跟上一题一样找中间数递归，不过由于这题是链表，所以要用双指针找中间数
2. 还有种思路是中序遍历，再一一加节点。
## 107. Binary Tree Level Order Traversal II (Midium)
### **链接**：
题目：https://leetcode.com/problems/binary-tree-level-order-traversal-ii/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求层次遍历，不过这题要按层数从下到上。
### **分析**：
可以直接用 Binary Tree Level Order Traversal 的代码。
## 108. Convert Sorted Array to Binary Search Tree (Medium)
### **链接**：
题目：https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
为一个排过序的数组建一棵平衡的 BST。
### **分析**：
要平衡，只要取中间的那个数做根就行了。递归下去即可。
## 106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)
### **链接**：
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
从中序后序遍历建树。
### **分析**：
用递归直接模拟就可以了。  
这里可以倒着来，这样就跟 `105. Construct Binary Tree from Preorder and Inorder Traversal` 一样了，不用再想一遍。
## 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
### **链接**：
题目：https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
从前序中序遍历建树。
### **分析**：
用递归直接模拟就可以了。
## 103. Binary Tree Zigzag Level Order Traversal (Midium)
### **链接**：
题目：https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
跟 `Binary Tree Level Order Traversal` 一样，求层次遍历，不过这题要让奇数层反着。
### **分析**：
可以直接用 Binary Tree Level Order Traversal 的代码。
## 102. Binary Tree Level Order Traversal (Midium)
### **链接**：
题目：https://leetcode.com/problems/binary-tree-level-order-traversal/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求层次遍历。
### **分析**：
1. 用 BFS 遍历，放在数组中。
2. 用 DFS 时放到指定层数数组中。
## 099. Recover Binary Search Tree (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/recover-binary-search-tree/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
一棵 BST 有两个节点的值不小心互换了，要你把这棵树恢复了。  
  
### **分析**：  
  
**解法1**  
  
先得到中序遍历结果，再找出那俩节点，交换值就行了，不过要用 O(n) 的空间  
  
**解法2**  
  
好好想想要怎么才能不用 O(n) 的空间来得到中序遍历结果？  
Knuth 大神曾提出过这个问题，然后 Morris 大神用 [Threaded binary tree](http://en.wikipedia.org/wiki/Threaded_binary_tree) 实现了！  
下面这张图来自 Threaded binary tree 的 Wikipedia，让人一目了然。  
  
![Threaded binary tree](http://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Threaded_tree.svg/330px-Threaded_tree.svg.png)  
  
你可能想：  
不就是不开空间吗？直接递归不就行了？  
K 神当初可不是做这题而提出的问题，因为递归在内存的栈中可是要占最坏 O(n) 的空间的！他问的是非递归算法。  
非递归我只会用栈递归 Orz...  
而 Morris 的 Threaded binary tree 可以用 O(1) 的空间实现非递归中序遍历，在 Wikipedia 上有详细的 Python 版本。  
  
参考：  
  
- [Threaded binary tree - Wikipedia](http://en.wikipedia.org/wiki/Threaded_binary_tree)  
- [[LeetCode] Recover Binary Search Tree 解题报告 ](http://fisherlei.blogspot.com/2012/12/leetcode-recover-binary-search-tree.html)  
  
## 098.Validate_Binary_Search_Tree
### **链接**：
题目：https://leetcode.com/problems/validate-binary-search-tree/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
判断一个树是否是搜索二叉树 (BST)  
### **分析**：
有几种解法：  
1. 直接 DFS ，判断这棵子树是否是在 [maxval, minval] 范围中
2. 中序遍历下，判断序列是否是递增的
3. DFS ，每次返回最大值或最小值，再进行判断  
都不是很难实现。  
这里用的是第一种方法，需要注意的坑是 maxval 和 minval 会有超 int 的情况，所以用 long long 类型。
## 197  Rising Temperature Easy
### **链接**：
题目：https://leetcode.com/problems/rising-temperature/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
1. 这题可以连接两个表来做，Date 类型的比较用 `TO_DAYS()` 来实现。
2. 如果先排序再用 `CASE-WHEN` 来做也可以，不过不知道怎么搞的，MySQL 的 `:=` 符号的优先级居然比 `AND\OR` 来得低，DEBUG 了半天才找到这个问题，郁闷。这样做快多了，速度跻身前列。
## 095. Unique Binary Search Trees II (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/unique-binary-search-trees-ii/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求 {1, 2, ..., n} 的所有 BST。  
  
### **分析**：  
  
递归即可。  
理解了“Unique Binary Search Trees”后应该不难解出这题。  
  
Java 和 Python 的解法和 C++ 一样，这里就不写出。  
## 097. Interleaving String (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/interleaving-string/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
问 s3 是否是 s1 和 s2 交错得到的。  
  
### **分析**：  
  
s3 中的一个字母 s1 和 s2 都有，那这算谁的？  
不同的决策会得到不同的结果，所以这个问题第一眼就感觉要搜索或 DP。  
  
1. 搜索，当遇到 s1[i] = s2[j] = s3[i+j] 时，分类讨论，一种判给 s1，再搜索下去，另一种判给 s2 再搜。复杂度是 O(2^n)  
2. 可以考虑对 1 算法进行记忆化，复杂度 O(n*m)  
3. (**C++**)DP。 `dp[i][j]` 表示 s1[i], s2[j] 时是否匹配 s3[i+j]，这样两种都会判断到了，公式：`dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s1[j-1] == s3[i+j-1])`。时间复杂度 O(n^2)，空间 O(n^2)  
4. (**Java**)对 3 进行优化：使用滚动数组，减小空间复杂度为 O(n)  
5. 在 Discuss 里看到有个大神机智地用 BFS 解决了这题，太形象了！有兴趣可以观摩下：[C++ solution using BFS, with explanation](http://leetcode.com/discuss/19973/8ms-c-solution-using-bfs-with-explanation)  
## 096. Unique Binary Search Trees (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/unique-binary-search-trees/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求 {1, 2, ..., n} 的 BST 个数。  
  
### **分析**：  
  
DP 公式为：  
`dp[i] = dp[k] * dp[i-k-1] { 0<=k<=i-1 }`  
可以这样理解：  
求 {1, 2, ...., i} 的 BST，我们拿其中的一个数作根（假设为 k），根据 BST 的特性，左子树就是 {1, 2, ..., k-1}，右子树就是 {k+1, k+2, ..., i} 了。  
而很明显 {k+1, k+2, ..., i} 化 BST 的可能性和 {1, 2, ..., i-(k+1)} 是一样的。  
记 {1, 2, ..., n} 的 BST 个数为 f(n)，上述就可以表达为 `f(i) = f(k-1) * f(i-k-1)`。  
而我们选择的 k 就是 {1, 2, ...., i} 中的任意一个，而不同的 k 等到的 BST 是不会重复的。  
## 093.Restore_IP_Addresses
### **链接**：
题目：https://leetcode.com/problems/restore-ip-addresses/  
代码(github)：https://github.com/illuz/leetcode  
### **题意**：
给一个都是字母的字符串，加上点后可能会变成合法的 IP 地址，求一个字符串的所有合法地址。  
### **分析**：
不是很难的题目。  
1. DFS 过去，注意要处理一些细节  
2. 因为只有四个域，只要枚举每个域的长度，然后拆开字符串一个个判断就行了。  
这里用的是第二种方法，比较容易理解。  
Python 有方便的 str() 和 int()，可以很方便的用 lambda 和 map 实现判断部分。  
## 087. Scramble String (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/scramble-string/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
  
一个字符串递归分成一棵树：  
  
```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   a 
           / \
          a   t
```
  
一个 scramble 操作就是将一个非叶子节点的子节点翻转。  
下面是将 `gr` 节点翻转的结果：  
  
```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```
  
当然你可以对多个节点进行翻转。  
  
现在给出俩字符串，问 s1 能否通过 scramble 操作后得到 s2。  
  
### **分析**：  
  
1. (**C++**)暴力递归必然超时，复杂度是 O(3^n)。  
2. (**C++**)在 1 的基础上进行记忆化，开三维数组来存： `dp[i][j][len]` 表示 `s1[i~(i+len)]` 和 `s2[j~(j+len)]` 是否能匹配。复杂度是 O(n^4)。（这里的复杂度网上很多博客都写错了，数组中每个数会算一次，也就是会进入函数一次，函数里会 for 一遍 (length-1) 次，所以复杂度是 O(n^4)）。  
3. (**C++\Java**)在 1 的基础上进行剪枝，每次判断两个字符是否字母个数一样，这样就可以过了。（这个解法用 Java 的 `Arrays.sort` 和 `Arrays.equals` 来做很爽）  
4. (**Python**)能用记忆化搜索做，那肯定可以用 DP 做了，复杂度一样是 O(n^4)，从记忆化搜索做法中的 if 条件中可以看出转移式： `f[n][i][j] =  (f[k][i][j] && f[n-k][i+k][j+k]) || (f[k][i][j+n-k] && f[n-k][i+k][j])` 。  
  
## 085. Maximal Rectangle (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/maximal-rectangle/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求一个 01 矩阵的全是 1 的子矩阵的最大规模。  
  
### **分析**：  
  
很有挑战性的题目。  
一眼看过去就感觉要用 DP 做，可是从前个位置的答案和当前位置的行列延伸值的转移无法保持最优性。  
  
看了下 discuss，发现提到了上一题 [084. Largest Rectangle in Histogram (Hard)](https://github.com/illuz/leetcode/tree/master/solutions/084.Largest_Rectangle_in_Histogram)，想了下，简直机智得不得了！  
我们可以转化为：求矩阵前 x 行，以第 x 行为底的最大矩形，这不就直接是上一题了吗。  
Largest Rectangle in Histogram 的复杂度是 O(n)，所以这题的复杂度是 O(n^2)，矩阵条（直方图）的处理可以用 O(n) 的空间来搞定。  
  
Largest Rectangle in Histogram 我写了两 AC 的算法，一个用 stack 的是 O(n)，一个暴力加优化的 O(n^2)，这题直接用上题的函数，都过了 = =b。  
（这里不得不提下 Discuss 上的一个[数组 DP 的算法](DP solution)，其实它的思想跟直方图很像的）
## 084. Largest Rectangle in Histogram (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/largest-rectangle-in-histogram/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求一些宽为 1 的矩形条的最大矩形。  
  
### **分析**：  
  
跟 [Container With Most Water](./solutions/011.Container_With_Most_Water) 很像。  
  
暴力：以每个矩形条为最高，维护最低向前找内含的矩形，O(n*m)，肯定会超时的啦。（听说优化下，只处理峰顶就能过，不过复杂度还是没变的）  
  
有好多种做法，O(nlogn) 到 O(n) 的都有，具体可以看[这篇文章](http://blog.csdn.net/arbuckle/article/details/710988)。  
这里我简单翻译总结下：  
  
1. 分治 + 线段树。线段树存每个区间的最小值，每次处理一个区间时，找到区间最小值，然后分治两边的区间，答案肯定是 `(最小值 * 区间长度)` 和分治得到的结果中的。复杂度 O(nlogn)  
2. 线性处理 + 线段树。对每个矩形条，向左向右找最近的比它小的位置，以它为最低的矩形就可以求出来了，处理每个矩形条就行了，复杂度 O(nlogn)。（这里它说找位置是 O(logn) 复杂度，我没想出来，我只想到二分来找位置，复杂度 O(lognlogn)，总的复杂度就是 O(nlognlogn) 了）  
3. 排序 + 扫描线。先排序，再从上向下扫，维护一个区间链，扫到的矩形条的**原位置**加入区间链，该合并时就合并，每次区间最大长度就是当前高度的最宽区间了。因为排序，所以这个算法复杂度是 O(nlogn)。  
4. 用单调栈来做，很巧妙，只要扫一遍就行了，在把数从栈中挤出去的时候，计算两个矩形条间的矩形面积。复杂度 O(n)。  
5. 将单调栈做法改写成递归，其实就是把函数栈当成单调栈来用。  
6. 三个矩形条为一个窗口，有几个操作：更新最大值，合并其中两个矩形条为一个新的矩形条（高度为较小的那个，宽度为两宽度的和），窗口左移和右移。（具体见原文）  
这里用 C++ 实现了暴力 + 优化过的，用 Java 实现算法 4 的单调栈做法。
## 076. Minimum Window Substring (Hard)
### **链接**：
题目：https://leetcode.com/problems/minimum-window-substring/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个原字符串 S，和一个匹配串 T，求 S 最小的子串（窗口）包含全部 T 的字符。  
### **分析**：
跟 '030.Substring_with_Concatenation_of_All_Words' 很像，思路和做法是一样的。  
用快慢指针，快指针跑到匹配的位置，再向前缩慢指针。  
计算匹配可以利用 Hash 来计算有效的字母，Hash 可以用 HashMap(Java)，unordered_map(C++)，也可以直接用数组。用数组会比较快。  
这里 Java 和 Python 的写法和 C++ 的基本一样，就不给出了。  
## 068.Text_Justification (Hard)
### **链接**：
题目：https://leetcode.com/problems/text-justification/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给出一些单词和一个宽度，要你把单词打包成宽度一样的字符串数组。  
要求：  
1. 每个字符串尽可能包含多个单词，多余的位置用空格代替。  
2. 单词间空格尽量平均，不能平分的话，前面的空格要比后面的多。  
### **分析**：
就是直接模拟，要注意细节处理。
## 037. Sudoku Solver (Hard)
### **链接**：
题目：https://leetcode.com/problems/sudoku-solver/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求解一个数独。
### **分析**：
DFS 暴力就行了。  
用二进制表示，位运算处理的话，会快很多的。  
其实在一个 `(n^2) * (n^2)` 的格中放 `n * n` 数，这是个 NP 难问题，就 9x9 的方格，就有 `9^81` 种组合，用 DFS 遍历一遍是不可想象的，所以在解一个空一点的 9x9 时就要跑好久。  
有个比较常用的优化方法就是用 `Dancing Links`，不过这也只是个剪枝，它仍是个 NP 难问题。  
Link:  
- [Sudoku - Wikipedia](http://en.wikipedia.org/wiki/Sudoku)
- - [Dancing Links](http://en.wikipedia.org/wiki/Dancing_Links)
## 195. Tenth Line (Easy)
### **链接**：
题目：https://leetcode.com/problems/tenth-line/  
## 036. Valid Sudoku (Easy)
### **链接**：
题目：https://leetcode.com/problems/valid-sudoku/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
判断一个数独是否有效。  
有效的数独不强求有解。
### **分析**：
只要同一行、列、块里没有相同数字就行了。  
开个数组记录就行了，没什么难度，可以用二进制来表示，表位运算加速。  
（注意是判断有效，不是有解，我刚开始给求解了，TLE 了好多次。。。）
---
**English**
## 035.Valid_Sudoku  
Because it just checks whether the sudoku is valid, so we can just check the numbers in it only.  
But if we check if the sudoku has a solution, then we should use other algorithms. Because a sudoku is VALID doesn't mean that it has a solution.  
To check if it has a solution, we can use **DFS** to check it. But it may take a long time. Because the complexity is O((n*n)!) !  
The better algorithm is **Dancing Link**.  
## 035. Search Insert Position (Medium)
### **链接**：
题目：https://leetcode.com/problems/search-insert-position/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
要把一个数有序插入到一个有序数组里，问插入的位置。
### **分析**：
还是二分变形题。  
1. 用 STL 的 `lower_bound` 偷懒。
2. 二分，最后注意判断一下是否找到，要输出什么。
## 034. Search for a range (Medium)
### **链接**：
题目：https://leetcode.com/problems/search-for-a-range/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在有序数组中找到一个数的范围。（因为数有重复）
### **分析**：
还是二分搜索变形。  
1. **(C++)**直接用 C++ STL 的 `lower_bound` 和 `upper_bound` 偷懒。
2. **(Java)**直接从普通的二分改一下就行了。
## 032. Longest Valid Parentheses (Hard)
### **链接**：
题目：https://leetcode.com/problems/longest-valid-parentheses/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
问一个字符串里最长的合法括号串的长度。
### **分析**：
1. **(C++)**用栈来做，如果匹配就出栈，然后长度就是 `cur - stack_top_pos` 也就是 - 匹配的前一个位置。 O(n) time, O(n) space。
2. **(C++)**栈消耗空间太多了，其实可以维护 () 匹配的长度，不过可能出现 `()))` 和 `((()` 的情况，所以要前后各扫一遍。O(n) time, O(1) space。
3. 用较复杂的 DP 来做，不过空间可没解法 2 那么优了。刚看到[我很久前的一个解法](http://blog.csdn.net/hcbbt/article/details/15494035)，用太多空间了Orz。现在来看还是 1、2 的做法好。
## 033. Search in Rotated Sorted Array (Hard)
### **链接**：
题目：https://leetcode.com/problems/search-in-rotated-sorted-array/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在一个旋转过的有序数组中找一个数。  
比如 `4 5 6 7 0 1 2` 就是一个“旋转过的有序数组”。
### **分析**：
这是单纯二分搜索的变形。  
因为旋转过不好定位，所以在找的时候可以先判断一下一个区间是完全有序的还是已经旋转过的，然后分类讨论。
## 031. Next Permutation (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/next-permutation/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求一个序列的下一个排列。  
  
### **分析**：  
  
可以用 STL 里的 'next_permutation' 偷懒。  
  
具体算法是：  
  
> 首先，从最尾端开始往前寻找两个相邻的元素，令第一个元素是 i，第二个元素是 ii，且满足 `i<ii` ；  
> 然后，再从最尾端开始往前搜索，找出第一个大于 i 的元素，设其为 j；  
> 然后，将 i 和 j 对调，再将 ii 及其后面的所有元素反转。  
  
## 030. Substring with Concatenation of All Words (Hard)  
  
### **链接**：  
题目：https://leetcode.com/problems/substring-with-concatenation-of-all-words/    
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
给一个字符串 S 和一个单词列表，单词长度都一样，找出所有 S 的子串，子串由所有单词组成，返回子串的起始位置。  
  
### **分析**：  
  
很明显每个子串都是由所有单词组成的，长度是一定的，所以直接枚举子串，切分后再用 map 进行判断就行了。  
  
这样的算法复杂度是 O(n*m)，其实还有几种很酷的 O(n) 的算法：  
  
1. 跟[「076. Minimum Window Substring (Hard)」](https://github.com/illuz/leetcode/blob/master/solutions/079.Word_Search) 一样的思路，就是维护两个指针，分别为前后区间，和一个 map，跑前面的指针看看当前区间能不能恰好匹配，行的话就得到答案了。  
2. 还有个用神奇的 `map<string, queue>` 来做，其实原理是跟 1 是一样的，具体见：[code with HashTable with Queue for O(n) runtime](https://leetcode.com/discuss/21598/my-c-code-with-hashtable-with-queue-for-runtime-71ms-runtime)  
3. 这其实只是一个优化，在匹配时使用 Trie 匹配，具体见：[Accepted recursive solution using Trie Tree](https://leetcode.com/discuss/20055/accepted-recursive-solution-using-trie-tree)  
  
这里用 C++ 实现了 O(n*m) 算法，用 Java 实现了 1 算法。  
## 029. Divide Two Integers (Medium)
### **链接**：
题目：https://leetcode.com/problems/divide-two-integers/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
实现除法，不能用乘、除和取模。
### **分析**：
不能用乘、除和取模，那剩下的，还有加、减和位运算。  
1. 会想到的就是一次次去减，不过这样会超时。
2. 在 1 的基础上优化下，跟快速幂一样，每次把除数翻倍（用位运算即可）。  
这里有坑，就是结果可能超 int 范围，所以最好用 long long 处理，之后再转 int。
## 028. Implement strStr() (Easy)
### **链接**：
题目：https://leetcode.com/problems/implement-strstr/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在一个字符串里找另一个字符串在其中的位置。  
### **分析**：
这题归在 Easy 类是因为它 O(n*n) 的暴力能过。  
如果数据强点就得 Midium 以上了。  
1. **(C++)** 这题的暴力 O(n^2) 就是两遍 for 去找  
2. **(C++)** 还有各种高大上的算法，比如 [KMP 算法](http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm)，这是经典的了  
3. **(Python)** 另外可以用 hash 去做，叫 rolling hash 算法（见 [Wiki](http://en.wikipedia.org/wiki/Rolling_hash) 和 [StackOverflow](http://stackoverflow.com/questions/711770/fast-implementation-of-rolling-hash)），就是把字符串 hash 出来，按匹配串长度窗口去滚动，再去匹配。hash 字符串有很多种方法，这边的字母好像都是小写，有 26 个，所以就用 29 做基数（本来想像 djb2 算法用 33 做基数，可以直接 `((hash << 5) + hash)` 很快，不过 int 范围只能 hash 6 个字母而且 rolling 的时候还是要 `/33`，还是用 29 算了），超 int 范围的话用 Python 就不用考虑这个问题了。  
其他还有 Boyer–Moore，Rabin–Karp 算法，具体自己去搜。  
## 026. Remove Duplicates from Sorted Array (Easy)
### **链接**：
题目：https://leetcode.com/problems/remove-duplicates-from-sorted-array/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个有序数列，删重复的元素。
### **分析**：
如果可以开一个数组来存就非常容易。但是这题不让你用多余的空间。  
不过也不难，只要维护一个新的坐标就行了。  
用 C++ 的 STL 可以只要一句话：用 `unique` 实现功能，用 `distance` 计算大小。  
（之前看错题以为是无序的，写了几个无序的版本）  
Java 和 Python 的写法都和 C++ 的一样，这里就不写出来了。  
## 194. Transpose File (Medium)
### **链接**：
题目：https://leetcode.com/problems/transpose-file/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
用 awk 做就像用 C 一样。
## 027. Remove Element (Easy)
### **链接**：
题目：https://leetcode.com/problems/remove-element/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
删除一个数组里值为 elem 的所有数。
### **分析**：
用两个指针，一个为可放位置的指针，一个为扫描指针。  
因为不难，Java 和 Python 的做法都和 C++ 一样，这里就不给出了。
## 025. Reverse Nodes in k-Group (Hard)
### **链接**：
题目：https://leetcode.com/problems/reverse-nodes-in-k-group/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一个链表每 k 个分为一组，每组内进行翻转。  
只能用常数级的空间。
### **分析**：
这题比较考验链表的操作，用递归做会比较方便，先找到下一组的节点，把本组反转后再递归处理后面的节点。
## 024. Swap Nodes in Pairs (Medium)
### **链接**：
题目：https://leetcode.com/problems/swap-nodes-in-pairs/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把一个链表中的每一对节点对换（不能只换值）。  
### **分析**：
直接模拟即可。  
开个前节点来做会比较方便。  
用 Python 的异常处理和赋值会很方便。
## 023. Merge k Sorted Lists (Hard)
### **链接**：
题目：https://leetcode.com/problems/merge-k-sorted-lists/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
和  [021. Merge Two Sorted Lists (Easy)](http://blog.csdn.net/hcbbt/article/details/44064639) 类似，这次要 Merge K 个。
### **分析**：
很明显可以想到利用已经完成的 Merge Two Sorted Lists 的函数来用。  
这时有两种方法：  
1. (C++) 用二分的思想，把每个 List 和它相邻的 List 进行 Merge，这样规模就缩小了一半了，再重复这样，就可以 O(nklogk) 完成。比如： [1, 2, ..., n] 的第一轮 Merge 是 [1, n/2], [2, n/2+1], ...  
2. (Python) 也是用二分的思想，就是把 Lists 分为两部分，分别递归 Merge k Sorted Lists 后变成两个 List ，然后再对这两 List 进行 Merge Two Sorted Lists 。  
这两种方法都是递归调用，都可以进行记忆化，用空间换时间，不过我不清楚会不会超空间（Memory Limit Exceed），所以就没试了~  
除了用二分的思路，还有更好写的方法，就是用堆(heap)，具体就是用优先队列(Priority Queue)。  
(Java) 先把每个 List 的第一个节点放进优先队列，每次取出队列中的最大值节点，再把那个节点的 next 放进去。  
## 022.Generate_Parentheses (Medium)
### **链接**：
题目：https://leetcode.com/problems/generate-parentheses/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
产生有 n 对括号的所有有效字符串。
### **分析**：
1. 用 DFS 可以很快做出来，能加'('就加'('，能加')'就加')'。（下面的 C++ 实现）  
2. 还有很机智方法写出很短的 DFS 。 (Java 实现)  
3. 对于 DFS 都可以进行记忆化，用空间换时间。 (Python 实现)  
## 021.Merge_Two_Sorted_Lists (Easy)
### **链接**：
题目：https://leetcode.com/problems/merge-two-sorted-lists/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
合并两个有序链表。
### **分析**：
很经典的题目，不过知道怎么做后很容易，模拟即可。  
有两种做法：  
1. 开一个节点做 head 的前节点 （下面的 Python 代码实现）  
2. 不开直接做（C++ 代码实现）
## 020.Valid_Parentheses (Easy)
### **链接**：
题目：https://leetcode.com/problems/valid-parentheses/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
判断一个括号字符串是否是有效的。
### **分析**：
直接用栈模拟，很简单的。  
Java 的括号匹配可以用 if 写，也可以用 `HashMap<Character, Character>` 存，还可以用 `"(){}[]".indexOf(s.substring(i, i + 1)`。 （这个讨论也可以用于 C++ 和 Python）  
这里的 C++ 是用 if 匹配， Java 用 indexOf， Python 用 dict。
## 019.Remove_Nth_Node_From_End_of_List (Easy)
### **链接**：
题目：https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
删除一个单向链表的倒数第 N 个节点。  
### **分析**：
1. 直接模拟，先算出节点数，再找到节点删除  
2. 用两个指针，一个先走 N 步，然后再一起走。  
这里用 C++ 实现第一种， 用 Python 实现第二种。  
Java 的话和 C++/Python 差不多，不写出来了。  
## 018.4Sum (Medium)
### **链接**：
题目：https://leetcode.com/problems/4sum/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个数列 S ,找出四个数 a,b,c,d 使得`a + b + c + d = target`。
### **分析**：
1. 跟之前的 2Sum, 3Sum 和 3Sum Closest 一样的做法，先排序，再左右夹逼，复杂度 O(n^3)。不过用 Python 可能会被卡超时。  
2. 先求出每两个数的和，放到 `HashSet` 里，再利用之前的 2Sum 去求。这种算法比较快，复杂度 `O(n*n*log(n))`，不过细节要处理的不少。  
 
这里 C++ 用的是算法1， Java, Python 用的是 2。  
这题 Java 可以好好地学学 `HashMap` 的使用， Python 可以学习 `set`, `collection` 和 `itertools` 的一些用法。  
**(2015-04-02 UPDATE)**  
这题解法 2 的复杂度是 `O(n*n*log(n))`，是在 `HashMap` 操作复杂度是 `O(log(n))` 的情况下算出的。  
不过是正常都把 `HashMap` 当成 `O(1)` 操作的，所以也会把总的复杂度算成 `O(n*n)`。
## 017.Letter_Combinations_of_a_Phone_Number
### **链接**：
题目：https://leetcode.com/problems/letter-combinations-of-a-phone-number/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在手机上按字母，给出按的数字键，问所有的按的字母的情况。
### **分析**：
DFS 过去是比较轻松的写法。 
## 193. Valid Phone Numbers (Easy)
### **链接**：
题目：https://leetcode.com/problems/valid-phone-numbers/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
用 Shell Script 输出 `(xxx) xxx-xxxx` or `xxx-xxx-xxxx` 格式的号码。
### **分析**：
这题考察的是正则表达式。  
可惜我写的正则是很挫的。  
1. 用 sed 做：`sed -n '/expression/p'`
2. 用 grep 做：`grep 'expression'`
3. 用 egrep 做：`egrep 'expression'`，egrep 的正则和 grep 的不太一样。
4. 用 awk 做：`awk '/expression/ {print}`，awk 的匹配式不太支持正则表达式，比较难用。
## 016.3Sum_Closest (Medium)
### **链接**：
题目：https://leetcode.com/problems/3sum-closest/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在给定数列中找出三个数，使和最接近 target。
### **分析**：
与 [015. 3Sum (Medium)](../015.3Sum) 类似，甚至更简单。  
还是先排序，再左右夹逼。
## 015.3Sum (Medium)
### **链接**：
题目：https://leetcode.com/problems/3sum/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
在给定数列中找出三个数，使和为 0。
### **分析**：
先排序，再左右夹逼，复杂度 O(n*n)。  
N-sum 的题目都可以用夹逼做，复杂度可以降一维。  
这题数据更新后卡得很紧， C++ 不能全部加完再用 STL 的 erase 和 unique 去重，要一边判断一边加。
## 014.Longest_Common_Prefix (Easy)
### **链接**：
题目：https://leetcode.com/problems/longest-common-prefix/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求多个字符串的最长公共前缀。
### **分析**：
一位一位判断即可，没什么坑点。
## 013.Roman_to_Integer (Easy)
### **链接**：
题目：https://leetcode.com/problems/roman-to-integer/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把罗马数转为十进制。
### **分析**：
跟 [012. Integer to Roman (Medium)](http://blog.csdn.net/hcbbt/article/details/44026099) 一样，只要知道转化规则就行了。
## 012.Integer_to_Roman (Medium)
### **链接**：
题目：https://leetcode.com/problems/integer-to-roman/
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把十进制转为罗马数。
### **分析**：
模拟即可。
“罗马数字的基本符号有Ｉ（表示十进制数1），Ｖ（表示5），Ｘ（表示10），Ｌ（表示50），Ｃ（表示100），Ｄ（表示500），Ｍ（表示1000）。” -- [罗马数制(百度百科)](http://baike.baidu.com/view/1246899.htm)
## 011.Container_With_Most_Water
### **链接**：
题目：https://leetcode.com/problems/container-with-most-water/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一些挡板，选两个挡板，求最大蓄水容量。
### **分析**：
可以看看[这个大神的详细算法](http://www.cnblogs.com/TenosDoIt/p/3812880.html)，给跪...  
1. 暴力 O(n*n) 会超时
2. 双指针，O(n) 时间和 O(1) 空间，应该是最优的算法了，上述的文章有这个算法的正确性证明。
3. 预处理每个挡板的左边最高和右边最高，这样蓄水区间就可以知道了  
这里只用了第二种算法。
## 010.Regular_Expression_Matching
### **链接**：
题目：https://leetcode.com/problems/regular-expression-matching/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个原串和一个正则表达式，问能不能匹配。
### **分析**：
1. 偷懒的方法是直接用语言自带的正则实现。(Python 又是一句话 =w=)
2. 用 DFS 的方法
3. 可以用 DP 的方法
    - 用数组 DP :`dp[i][j]` 表示 s[0..i] 和 p[0..j] 是否 match，当 `p[j] != '*'`，`b[i + 1][j + 1] = b[i][j] && s[i] == p[j]` ，当 `p[j] == '*'` 要再分类讨论，具体可以参考 [DP C++](https://leetcode.com/discuss/18970/concise-recursive-and-dp-solutions-with-full-explanation-in)，还可以压缩下把 dp 降成一维：参考[这里](https://leetcode.com/discuss/19902/share-a-scarce-dp-solution-in-java-time-o-mn-spaceo-n)
    - 用记忆化，就是把算过的结果保存下来，下次就不用再算了
## 009.Palindrome_Number
### **链接**：
题目：https://leetcode.com/problems/palindrome-number/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
判断一个数是否是回文数。  
### **分析**：
按自己想的去写就行了。  
1. 可以先转为字符串，再判断。（这种解法用 Python 可以一句话完成 =w=）  
2. 更好的方法是直接算出回文的数再直接比较。
## 008.String_to_Integer (Easy)
### **链接**：
题目：https://leetcode.com/problems/string-to-integer-atoi/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
将一个字符串转化为 int 型。  
### **分析**：
注意如果超出范围就返回最接近的 int 数。  
如：2147483648 大于 INT_MAX(2147483647) ，就返回 2147483647 。  
之前可以用 sscanf 偷懒，最近更新了 case 就被卡了。  
要注意几点：  
1. 跳过前面的空格,\t,\n  
2. 范围界定  
使用 Python 的正则表达式可以很容易处理。  
## 007.Reverse_Integer (Easy)
### **链接**：
题目：https://leetcode.com/problems/Reverse-Integer/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
反转一个数。  
### **分析**：
注意读入和返回的数都是 int 型的，这时就要考虑反转后这个数会不会超 int，超的话就返回 0 。这时处理数时最好用比 int 大的类型，不然恐怕会超范围。  
当然也可以用 int ：`if (result > (INT_MAX/10))`
还有一点就是还要考虑前导零。  
## 192. Word Frequency (Medium)
### **链接**：
题目：https://leetcode.com/problems/word-frequency/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
统计 word.txt 里的单词和频数，然后按频数从小到大排序输出。
### **分析**：
1. 用 `awk` 统计单词个数。
    - 用 `awk` 里的字典，循环统计每一行的第个单词。
    - 处理完全部行后，再用`for (item in Dict) { #do someting# }` 把单词和频数输出来。
2. 不过现在只是做好了统计，还要排序下。用管道 `|` 把输出交给 `sort` 来排序
    - `sort -n` 把字符串转成数来比较。
    - `sort -r` 从小到大。
    - `sort -k 2` 把第二个字串当做 key。
---
English version:
1. I should count the words. So I chose the `awk` command.
  - I use a dictionary in `awk`. For every line I count every word in the dictionary.
  - After deal with all lines. At the `END`, use `for (item in Dict) { #do someting# } ` to print every words and its frequency.
2. Now the printed words are unsorted. Then I use a `|` pipes and sort it by `sort`
  - `sort -n` means "compare according to string numerical value".
  - `sort -r` means "reverse the result of comparisons".
  - `sort -k 2` means "sort by the second word"
## 006.ZigZag_Conversion (Easy)
### **链接**：
题目：https://leetcode.com/problems/zigzag-conversion/  
代码(github)：https://github.com/illuz/leetcode  
### **题意**：
把一个字符串按横写的折线排列。  
### **分析**：
直接模拟就行了。
## 005.Longest_Palindromic_Substring (Medium)
### **链接**：
题目：https://leetcode.com/problems/Longest-Palindromic-Substring/  
代码(github)：https://github.com/illuz/leetcode  
### **题意**：
求一个字符串中的最长回文子串。  
### **分析**：
回文的解法有不少：  
1. 暴力搜索 O(n^3)   
2. 动态规划 O(n^2)， `dp[i][j] = dp[i + 1][j - 1] (if s[i] == s[j])`  
3. 用[Manacher's ALGORITHM](http://blog.csdn.net/hcbbt/article/details/18952129)可达到 O(n) 时间。  
本题要用第三种算法。  
需要注意的是， Python 和 Java 的字符串和 C++ 的不一样，没有 `\0` 结尾，用'Manacher's ALGORITHM'的时候是不一样的。
## 004.Median_of_Two_Sorted_Arrays
### **链接**：
题目：https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
求两个有序数组的中位数。要求复杂度是 O(log(n + m))。
### **分析**：
两种思路：  
1. 直接 merge 两个数组，然后求中位数，能过，不过复杂度是 O(n + m)。  
2. 用二分的思路去做，这不好想，还要考虑到奇偶。可以转化思维，去求两个有序数组中的第 K 大数，这样就比较好想了。  
---
**(English version)**
## 004.Median_of_Two_Sorted_Arrays
**Link**:
Problem: https://leetcode.com/problems/Median-of-Two-Sorted-Arrays/  
Newest solutions in my Github: https://github.com/illuz/leetcode
**Analysis**：
Two ways to get it.  
1. Merge the two arrays first and solve it. But the time complexity is O(n + m).  
2. Use the method of binary search. This will be hard to think. Just consider to find the k-th biggest number in two sorted arrays and it will help you.  
  
## 003.Longest_Substring_Without_Repeating_Characters  
  
### **链接**：  
题目：https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
从标题就可以知道题意了，是求一个字符串中最长的不含重复字符的子串。  
  
### **分析**：  
开一个数组记录当前字符最近出现的位置，一遍算过去，更新左边界，用它计算最大值就行了。  
需要花费常数的空间。  
  
  
---  
  
**(English version)**  
  
  
## 003.Longest_Substring_Without_Repeating_Characters  
  
  
**Link**:  
Problem: https://leetcode.com/problems/Longest-Substring-Without-Repeating-Characters/  
Newest solutions in my Github: https://github.com/illuz/leetcode  
  
**Analysis**：  
Generate an array to record the last position of current character.  
Count and update the left bound, and calculate the maximum.  
It will just cost constant space.  
## 002.Add_Two_Numbers (Medium)  
  
  
### **链接**：  
题目：https://leetcode.com/problems/add-two-numbers/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
求两个 List 相加产生的新的一个 List。  
  
### **分析**：  
直接模拟就可以了。  
  
---  
  
**(English version)**  
  
## 002.Add_Two_Numbers (Medium)  
  
  
**Link**:  
Problem: https://leetcode.com/problems/add-two-numbers/  
Newest solutions in my Github: https://github.com/illuz/leetcode  
  
**Analysis**：  
Just simulation is enough.  
## 001.Two_Sum (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/two-sum/  
代码(github)：https://github.com/illuz/leetcode  
  
### **题意**：  
一个数组中两个位置上的数的和恰为 target，求这两个位置。  
  
### **分析**：  
暴力找过去复杂度是 O(n^2)，会 TLE。  
  
1. 可以先排序再用双指针向中间夹逼，复杂度 O(nlogn)。  
2. 可以用 Map 记录出现的数，只要判断有没有和当前的数凑成 target 的数，再找出来就行，复杂度 O(nlogn) 而不是 O(n) ，因为 Map 也要复杂度的。  
3. 在 2 中的 Map 复杂度可以用数组来弥补，时间复杂度是 O(n) ，不过空间复杂度是 O(MAXN)。  
  
---  
  
**(English Version)**  
  
## 001.Two_Sum (Medium)  
  
### **Link**:  
Problem: https://leetcode.com/problems/two-sum/  
Newest solutions in my Github: https://github.com/illuz/leetcode  
  
### **Analysis**：  
Brute-force finding will get TLE, because the time complexity is high O(n^2).  
  
1. Sort and use two pointers  
2. Use a hashmap (map in C++, HashMap in Java, dict in Python) to store the numbers. Then we can only find out the number which is (target - current_number) in the hashmap. The time complexity is O(nlogn). (NOT O(n), because the hashmap operator will cost time)  
3. We can use array to implement the hashmap in 2. Then the hashmap operator cost O(1) and the total time is O(n). But the array will cost O(MAXNUM) space.  
  
## 205. Isomorphoic Strings (Easy)
### **链接**：
题目：https://leetcode.com/problems/isomorphic-strings/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
判断两个字符串能否相互映射.
### **分析**：
1. 直接模拟，记录下映射关系
2. 用 Python 的 dict 和 zip 能够很方便处理映射关系
## 203. Remove Linked List Elements (Easy)
### **链接**：
题目：https://leetcode.com/problems/remove-linked-list-elements/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把链表里的等于 val 的节点都删掉。
### **分析**：
1. 直接模拟
2. 递归处理
## 202. Happy Number (Easy)
### **链接**：
题目：https://leetcode.com/submissions/detail/26084443/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
给一个操作，每次对一个数的每一位平方求和。  
现在给一个数，对这个数循环操作，如果这个数可以变成 1，那这个数就是 Happy Number。  
问这个数是不是 Happy Number。
### **分析**：
1. 可以直接模拟，用 HashMap 可以很方便地做。
2. 参考 [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) 的 [Two Point 解法](https://github.com/illuz/leetcode/tree/master/solutions/141.Linked_List_Cycle) 来做，很方便的。
## 201. Bitwise AND of Numbers Range (Medium)
### **链接**：
题目：https://leetcode.com/problems/bitwise-and-of-numbers-range/  
代码(github)：https://github.com/illuz/leetcode
### **题意**：
把 `[m, n]` 每个数进行与操作，问最后的数。
### **分析**：
问的是与操作，很容易发现结果都是 m 和 n 前面相同的部分 + 后面 0 填充，所以直接处理就行了。
1. 用 `while` 和位运算算出相同部分长度。
2. 不用循环，直接可以对 `n - m` 取 log 加 1 就是相同部分的长度了。
