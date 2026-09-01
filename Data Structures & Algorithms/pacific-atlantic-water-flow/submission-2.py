"""
BFS uses queues
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_seen = set() # seen
        p_que = deque() # visiting and its order

        a_seen = set()
        a_que = deque()

        ROW_COUNT = len(heights)
        COL_COUNT = len(heights[0])

        # add edge coords to seen/visited

        # top row for pacific
        for j in range(COL_COUNT):
            p_seen.add((0,j))
            p_que.append((0,j))

        # left col for pacific
        for i in range(ROW_COUNT):
            p_seen.add((i,0))
            p_que.append((i,0))

        # bottom row for atlantic
        for j in range(COL_COUNT):
            a_seen.add((ROW_COUNT-1,j))
            a_que.append((ROW_COUNT-1,j))

        # right col for atlantic
        for i in range(ROW_COUNT):
            a_seen.add((i,COL_COUNT-1))
            a_que.append((i,COL_COUNT-1))
        
        # given queue and seen set
        # pop a coord from queue
        # 
        def bfs(que,seen):
            while que:
                i,j = que.pop()
                for i_off,j_off in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_i = i+i_off
                    new_j = j+j_off

                    if (0 <= new_i < ROW_COUNT and
                        0 <= new_j < COL_COUNT and
                        heights[i][j] <= heights[new_i][new_j] and
                        (new_i,new_j) not in seen):
                        seen.add((new_i,new_j))
                        que.append((new_i,new_j))
            return seen
        
        a_coords = bfs(a_que,a_seen)
        p_coords = bfs(p_que,p_seen)

        return list(a_coords.intersection(p_coords))





