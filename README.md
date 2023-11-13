# CS497-Assignment5

1. Remove all invalid Parenthesis:

-The function isValid(s) checks the validity of parentheses in the string s by using a stack to keep track of opening parentheses and their positions.
-isValid(s) function returns True if the parenthesis are valid and returns false if not by looking at if the stack is empty or not.
-The function dfs(s, left, right) uses depth-first search and explores all possible combinations of removing parenthesis.
-If both left and right are zero and the string is valid, add it to the result list.
-It iterates through each character in the string and ignores all non-parenthesis character until it encounters one
-If the character is '(', and there are remaining left parentheses (left > 0), or if the character is ')' and there are remaining right parentheses (right > 0), it recursively calls dfs with the string after removing the current character and updating the counts of remaining left and right parentheses.
-In the main function removeInvalidParentheses(s), get the initial stack of unmatched parentheses using isValid(s)[1] and calculate the counts of left and right parentheses in the stack.
-Then initialize an empty result list res and a set visited and call the DFS function with the original string s, remaining left count, and remaining right count.
-Return the result list.

Time Complexity: O(2^n), in the worst case, where n is the length of the input string because it explores all possible combinations of removing parenthesis
Space Complexity: O(2^n), due to the recursive calling of DFS and space required for the visited set for each recursive call.

2. Maximum absolute Difference in BST

-First, make the list of all the nodes in the BST with inOrder Traversal
-Then initialize the maximum difference variable to be negative infinity
-Now, iterate through all the elements, and check the absolute difference between that element, and the element right next to it, and compare it to the maximum difference variable, and update if it is greater than it.
-return the maximum difference variable.

Time complexity: O(n) because you are iterating through all the nodes once and then through the inorder traversal list
Space complexity: O(n) because it needs n spots to store the inorder traversal of n nodes

3. Shortest Path visiting all Nodes

-initialize the all_visited variable as bit mask to represent all nodes being visited
-create a dp matrix and setting each dp[musk][i]value to be infinity to represent the shortest path that visits all nodes in the mask and ends at node i
-set the length for the very first row of the matrix to be 0 because the minimum path to node to itself is 0
-Iterate over all possible masks representing different subsets of visited nodes.
-For each mask, iterate over all nodes u in the graph that are currently visited (mask & (1 << u) is true).
-For each neighbor v of node u, update the dp array for the next mask by considering the minimum path length.
-at the end, find the minimum path length for the final mask (all nodes visited), and return the result.
-If the result is still set to the initial infinity value, return -1 to indicate that there is no valid path that visits all nodes.

Time complexity - O(n \* 2^n), where n is the number of nodes in the graph. The outer loop iterates over all possible masks (2^n), and the inner loop iterates over all nodes.

Space complexity - O(2^n \* n) due to the 2D array dp of size (2^n) x n. Each entry in the array requires constant space.

4. Binary Tree Maximum Path Sum:

-Initialize a returnList to hold value of the root
-Now iterate through all the nodes and return 0 if it is None
-If it is not None, then call the function recursively on the left tree and store the maximum of 0 (to deal with negative values) and the maximum node sum
-Similarly, call the function recursively on the right tree and store the max path sum of the right tree.
-Now check if the first element in returnList is greater or the sum of left tree maximum node sum, right tree maximum node sum and the root, and update the returnList first element
-return the very first element in the returnList

Time complexity: O(n), where n is the number of nodes in the binary tree because each node is visited once.

Space complexity: O(1) because we are only storing 1 value in the returnList

5. Lexicographical Numbers

-Initialize a returnList to hold all the numbers in the lexicographical order and a counter variable to 1
-Now iterate through all the numbers from 1 to n
-In each iteration, append the counter to the returnList and keep on multiplyting the counter by 10 until it is smaller than or equal to n and appending it to the returnList.
-Once we get to a point where counter is greater than n, then start dividing the counter by 10 until it returns back to the value it was originally before we multiplied it by 10, and then add 1 to it, so that the same process can be followed again
-return the returnList

TimTime complexity: O(n), because the loop runs n times.

Space complexity: O(n) because we are storing n values in returnList
