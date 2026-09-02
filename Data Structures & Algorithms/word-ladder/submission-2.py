class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:



        if endWord == "" or endWord not in wordList:
            return 0 

        l = len(beginWord)
        patterns = collections.defaultdict(list)

        for word in wordList:
            for index in range(l):
                patterns[word[:index] + "*" + word[index + 1:]].append(word)
        

        q = collections.deque()
        q.append([beginWord, 1])
        visited = set()
        visited.add(beginWord)

        while q:

            word, distance = q.popleft()

            if word == endWord:
                return distance
            
            for index in range(l):

                pat = word[:index] + "*" + word[index + 1:]

                for child in patterns[pat]:
                    if child not in visited:
                        visited.add(child)
                        q.append([child, distance + 1])

        
        return 0 