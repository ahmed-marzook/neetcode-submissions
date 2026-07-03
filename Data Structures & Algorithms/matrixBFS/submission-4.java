class Solution {
    public int shortestPath(int[][] grid) {
        // intialise the number of rows and columns in the matrix grid
        int ROWS = grid.length;
        int COLS = grid[0].length;

        // If the starting cell or the ending cell is a rock, no path exists
        if (grid[0][0] == 1 || grid[ROWS - 1][COLS - 1] == 1) {
            return -1;
        }

        // initlaise the visit matrix grid this will track what areas of the grid we already have visited and mark it 1 for visited 0 for not
        int[][] visit = new int[ROWS][COLS];
        // adding all valid paths to the queue to explore
        Deque<int[]> queue = new ArrayDeque<>();
        // Starting from the top left off the matrix grid and adding it to the queue
        queue.add(new int[2]);
        visit[0][0] = 1;

        // length intialised this is what will be returned
        int length = 0;
        // While loop tp go through the queue of all the valid items added
        while(!queue.isEmpty()) {
            // going through each layer of the matrix this is what it means by breadth first search
            int queueLength = queue.size();

            for(int i = 0; i < queueLength; i++) {
                // get the first item of the array and intialise the row and column
                int pair[] = queue.poll();
                int r = pair[0], c = pair[1];
                // this is the base case if we have traversed the matrix to the bottom right we have achived the goal and to return the length
                if(r == ROWS - 1 && c == COLS - 1) {
                    return length;
                }
                // intialised the neigbours right, left, above and below
                int[][] neighbors = {{r, c + 1}, {r, c - 1}, {r + 1, c}, {r - 1, c}};
                //going through the neighbours for the current item we popped off the queue
                for(int j = 0; j < 4; j++) {
                    // Get the neighbours
                    int newR = neighbors[j][0], newC = neighbors[j][1];
                    // if the new cordiantes meet any of these criteria they fail so skip
                    // if either columsn or rows is out of bounds
                    // if exists in the visited matrix
                    // if the path has a 1 which represents a rock so we cant raverse
                    if(Math.min(newR, newC) < 0 || 
                    newR == ROWS || newC == COLS || 
                    visit[newR][newC] == 1 || 
                    grid[newR][newC] == 1) {
                        continue;
                    }
                    // else add to the queue for the next layer and make sure to add it to already visited
                    queue.add(new int[]{newR, newC});
                    visit[newR][newC] = 1;
                }
            }
            length++;
        }
        return -1;
    }
}