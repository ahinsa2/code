import java.util.*;

public class TreasureIsland {
    public static int minStepsToTreasure(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> q = new LinkedList<>();

        // find start 'S'
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 'S') {
                    q.add(new int[]{r, c, 0});
                    visited[r][c] = true;
                }
            }
        }

        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], steps = cur[2];

            if (grid[r][c] == 'T') return steps;

            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && grid[nr][nc] != 'X') {
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc, steps + 1});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        char[][] grid = {
            {'S','O','O','S','S'},
            {'X','O','X','O','X'},
            {'O','O','O','O','X'},
            {'X','X','X','O','O'},
            {'X','X','X','X','T'}
        };
        System.out.println(minStepsToTreasure(grid));
    }
}
