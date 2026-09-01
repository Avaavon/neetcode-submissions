"""
BFS so use queues
queue & seen set per atlantic and pacific

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        ROW = len(heights)
        COL = len(heights[0])

        # top row for p
        for i in range(COL):
            p_seen.add((0,i))
            p_que.append((0,i))

        # left col for p
        for j in range(ROW):
            p_seen.add((j,0))
            p_que.append((j,0))

        # bottom row for a
        for i in range(COL):
            a_seen.add((ROW-1,i))
            a_que.append((ROW-1,i))

        # right col for a
        for j in range(ROW):
            a_seen.add((j,COL-1))
            a_que.append((j,COL-1))
        
        def get_coords(que,seen):
            while que:
                i,j = que.popleft()
                for i_off, j_off in [(-1,0),(1,0),(0,-1),(0,1)]:
                    new_i, new_j = i+i_off, j+j_off
                    if (0 <= new_i < ROW and
                        0 <= new_j < COL and
                        heights[new_i][new_j] >= heights[i][j] and
                        (new_i,new_j) not in seen):
                        seen.add((new_i,new_j))
                        que.append((new_i,new_j))
        
        get_coords(p_que,p_seen)
        get_coords(a_que,a_seen)

        return list(p_seen.intersection(a_seen))



