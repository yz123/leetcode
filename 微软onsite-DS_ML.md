http://www.1point3acres.com/bbs/thread-210225-1-1.html

O(log log n)

http://stackoverflow.com/questions/16472012/what-would-cause-an-algorithm-to-have-olog-log-n-complexity

O(log log n) terms can show up in a variety of different places, but there are typically two main routes that will arrive at this runtime.

```
1. Shrinking by a Square Root
2. O(log n) Algorithms on Small Inputs
```


But, if we take the square root at each level, we get

√65,536 = 256
√256 = 16
√16 = 4
√4 = 2
Notice that it only takes four steps to get all the way down to 2. Why is this? Well, let's rewrite this sequence in terms of powers of two:

√65,536 = √216 = (216)1/2 = 28 = 256
√256 = √28 = (28)1/2 = 24 = 16
√16 = √24 = (24)1/2 = 22 = 4
√4 = √22 = (22)1/2 = 21 = 2
Notice that we followed the sequence 216 → 28 → 24 → 22 → 21. 

这应该算接续我前一篇“[面试经验] Microsoft 电面 (data/ML类)” 的on-site经验。

有人私讯我问了一下面试过程，无奈我权限不足无法私讯…我就全部一起在这回答吧…

1.一共面了几轮呢？也是标准的4轮吗？

不是，负责我的那个recruiter是说每个人不一定，总共会是3~5轮，我个人面了5轮，而且是当天早上就知道要面5轮了，所以也不是什么面4轮之后等一阵子再加面的。(他们面试的人似乎会有个系统，直接看的到你今天会跟哪些人面)

2.offer如何？

我想intern的package大概就大同小异吧，大概是固定的7xxx的salary，然后另外提供住房、交通的补助。住房的话可以每个月扣500住corporatehouse，不然就是自己搞定，他给你4000。交通的话也是每个月扣375的车钱，不要的话就给你1200自己搞定。

3.可以分享一下面试题目？

我想这应该是大部分的人最关心的吧….我总共面了五轮，五轮其实跟我的电面差没多少，问问我之前的work做了什么，能够做什么。大部分的时间都是在讲之前的work就是了。剩下的时间通常20分钟左右就问些ML的问题还有很简单的coding题。

第一轮：

ML相关：

─你跟deeplearning熟吗(回：不熟)那你讲讲你对ML的什么technique比较熟悉好了，解释给我听。 (我就在白板上从linearregression一路讲解到SVM，应该算是所有ML的基础了)

然后问了两题很简单的问题

─给你一个半径R的飞镖盘，问你射出去的飞镖距离圆心d的期望值？

─丢两颗骰子，看到一颗是6，问你两科都是6的机率？

第二轮：

ML相关：

─什么时候要用AUROC? 什么时候用PRROC? 什么时候用Accuracy?

─简述一下decisiontree跟randomforest，两个模型有什么样的问题?要怎么避免overfitting?

─那简述一下怎么做gradient-boostingdecision tree?

─那什么是bootstrapping？

这一轮感觉interviewer没特别准备，就是先问些问题，我在回答的时候提到了些名词或是些解决问题的方法后他在更深入追问，所以题目看起来才会关联性那么强。

Coding相关：

─给你一个二元树，然后给你两个节点a跟b，要你把他们所有的commonancestor印出来。

这个coding题目我一开始是用RMQ做LCA，然后他看了有点不满意，说如果我们DFS的过程中，纪录每个节点的child里面有几个a or b(就0/1/2三种可能)，我们只要发现我们节点==2的时候就印出来就好了。我干嘛这样做呢？

我也直接把他讲的作法在白板上写出来，反正也很好co。只是在写完之后我跟他argue说，如果你今天有multiplequery的话，他的做法每次都要DFS过一次，我的就preprocess过每次都可以很快找出来，但是他不太懂LCA，所以我就解释给她听，听完她好像挺满意的。

第三轮：

ML相关：

─在learning很常用到kernel，那你要怎么判断一个kernel是否valid？

─比较一下first-ordermethod跟second-ordermethod

Coding相关：

─给你一个n*m的matrix，他被存成一个1D-array (就第(i, j)的element放在Arr[i*n+j])，现在要你把他从row-wise的顺序变成column-wise的顺序，只能用O(1)的memory

Ex.

1 2 3

4 5 6

原本是[1,2,3,4,5,6] 要变成[1,4,2,5,3,6]

第四轮：

ML相关：

─讲一下regularization的意义。(面试官好像是想听noise，因为我一开始说避免overfitting的时候他一脸狐疑。后来想说不会这么OX遇到了一个bayesian吧，就说l1大概就是在做regression的时候加入laplacenoise然后l2就加入guassiannoise，解方程出来的时候就刚刚好会是那样。他看起来就心满意足问我下一题了)

─我今天有很多的广告，每个广告都会有些关键词。那我现在有针对每个关键词我所得到的revenue。那问你该怎么predict之后的revenue？(他中间有特别强调这个是个veryhigh-dimensional的问题，不能用太naïve的方法)

Coding相关：

─给你一个Array，问你第i个element到第j个element最大的是哪个？ (我这题直接写了一颗segmenttree给他，因为我忘记sparsetable了…)，他说有更快点的做法，问我有没有办法做到？他有说他不要sparsetable，他有一个O(loglogn)的做法，速度介在ST跟线段树中间，我有没有办法从复杂度想出这个算法？(这应该是我当天面试里面唯一一个没做出来的问题…)

第五轮：

ML相关：

─我们在做广告的时候，会有很多的bidding，那给你一些信息(ex. Userinformation, user location, keyword, …)，问你我们的bidding要多少才合理？

─那你认为在做这些learning问题的时候，有什么东西是很重要的吗？(回：我觉得domainknowledge超重要)

Coding相关：

─今天有些广告主愿意每个广告出x元，总共的预算是y元 (简单来说最多投放y/x次)。如果我们最多只能投放k个广告，我们要怎么样才能赚最多钱？(简单的greedy，对y排序)

─那承上题，如果我们最多只能投放k个广告，然后广告主要求，你要马就一次投完给你y元，没达成目标就不给你钱，那我们最多能赚多少钱？(简单的DP题，就经典背包)

─那回到第一题，你有没有更快的做法？(思考了10秒，才想到不用对y排序直接分治就可以做到线性了)
这关面试的Coding都太经典了，所以几乎都是反射回答，没有经过思考，如果有思考应该就不会被问第三题了…最后他只有要我写第三题的code，很快就结束了。
大概是这个样子吧！如果有问题可以在下面留言….或是赏点大米私讯我我再回吧！
