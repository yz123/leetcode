#https://shenjie1993.gitbooks.io/leetcode-python/content/126%20Word%20Ladder%20II.html
"""
1. 在Word Ladder中，广度优先遍历是从上层到下层一层层遍历下去的，还是以下面的图为例，树结构可能是中间宽两头窄的情况。而一个节点转换为下层节点时，要依次将它字符串中的每个字符用其他字母替换后与给定字符串集合进行比较。如果树某一层的节点非常多，那么这个尝试转换的操作开销就很大。还需要明确的一点是，题目中的转换是可逆的，A可以转换为B，那么B也可以转换为A，且A和B都能转换为它们转换过程的某一个状态C。综上所述，我们可以从起始字符串和目标字符串同时进行转换，哪一端的节点数目少，我们就选这些节点继续进行转换，直到它们汇合到同一个节点或者转换终止（也就是下一层没有节点）。代码中由变量is_forward来表示从哪一端转换。
2. 现在是要求所有最少转换次数的转换方法，所以要将所有的转换可能都找出来。如图中bit和him转换为bim的转换关系我们都要找出来。
3. 我们还需要记录转换的路径，我们将从上一层到下一层的转换关系记录下来，等到确定能够转换成功了，再通过深度优先遍历的方法将转换路径组装起来。
"""
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        def bfs(front_level, end_level, is_forward, word_set, path_dic):
            if len(front_level) == 0:
                return False
            if len(front_level) > len(end_level):
                return bfs(end_level, front_level, not is_forward, word_set, path_dic)
            for word in (front_level | end_level):
                word_set.discard(word)
            next_level = set()
            done = False
            while front_level:
                word = front_level.pop()
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in end_level:
                            done = True
                            add_path(word, new_word, is_forward, path_dic)
                        else:
                            if new_word in word_set:
                                next_level.add(new_word)
                                add_path(word, new_word, is_forward, path_dic)
            return done or bfs(next_level, end_level, is_forward, word_set, path_dic)

        def add_path(word, new_word, is_forward, path_dic):
            if is_forward:
                path_dic[word] = path_dic.get(word, []) + [new_word]
            else:
                path_dic[new_word] = path_dic.get(new_word, []) + [word]

        def dfs(word, end_word, path_dic, path, paths):
            if word == end_word:
                paths.append(path)
                return
            if word in path_dic:
                for item in path_dic[word]:
                    dfs(item, end_word, path_dic, path + [item], paths)

        front_level, end_level = {beginWord}, {endWord}
        path_dic = {}
        bfs(front_level, end_level, True, wordlist, path_dic)
        path, paths = [beginWord], []
        dfs(beginWord, endWord, path_dic, path, paths)
        return paths
