# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary.
#  If no such itinerary exists, return null.
#  If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.


# Given the list of flights [['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'A']] and starting airport 'A',
# you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a
# valid itinerary. However, the first one is lexicographically smaller


from typing import List

class Solution:
    def findItinery(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        # tickets.sort()
        # Figure out sorting of data
        for src, dst in tickets:
            adj[src].append(dst)

        print('tickets', len(tickets))
        print('adj', adj)
        res = ['JKF']

        # def dfs(src):
        #     print()
        #     if len(res) == (len(tickets) + 1)
        #         return true
        #     if src not in adj:
        #         return False
        #
        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #
        #         if dfs(v): return true
        #
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return true
        #
        # dfs('JFK')
        return res


b = Solution()
print(b.findItinery([['A', 'B'], ['A', 'C'], ['B', 'C'], ['C', 'A']]))
