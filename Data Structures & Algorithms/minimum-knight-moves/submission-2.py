class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:


        KNIGHT_OFFSETS = (
            (-2, -1), (-2, 1), 
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1),
        )

        x = abs(x)
        y = abs(y)


        q = collections.deque()
        q.append([0, 0])

        visited = set()
        visited.add((0, 0))
        moves = 0

        while q:

            for _ in range(len(q)):
                row, col = q.popleft()

                if (row, col) == (x, y):
                    return moves
                
                for rd, cd in KNIGHT_OFFSETS:
                    next_row = row + rd
                    next_col = col + cd
                    neighbor = (next_row, next_col)

                    if not(
                        -2 <= next_row <= x + 2 and -2 <= next_col <= y + 2
                    ):
                        continue
                    
                    if neighbor in visited:
                        continue
                    
                    visited.add(neighbor)
                    q.append(neighbor)

            moves += 1


        return -1
            

