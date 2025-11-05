# CMPS 6610 Problem Set 04
## Answers

**Name:** Qi An Ong

Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |1340                     |826                |826/1340 = 0.616

alice29.txt    |1039367                     |676374                |676374/1039367 = 0.651

asyoulik.txt    |876253                     |606448                |606448/876253=0.692

grammar.lsp    |26047                     |17356                |17356/26047=0.666

fields.c    |78050                     |56206                |56206/78050=0.720


There is a consistent trend. Huffman coding reduces the cost compared to fixed length coding. the huffman cost is roughly 62-72% of the fixed length cost. This is based on how skewed the character frequency distribution is. Files with more uniform frequency distribution will see less benefit

- **1d.**
If every character in alphabet Σ had the same frequency, the huffman tree will be balanced so code lengths will be log(Σ) bits per symbol. The huffman cost should be approximately equal to the fixed length cost, expected cost of log(Σ) and consistent, same across all documents in which characters are also uniformly distrubuted. Huffman coding advantage over fixed length coding only appears when frequencies are non uniform.




- **2a.**
For array A, root at index 0, for node at index i, left child at 2i + 1, right at 2i + 2, parent at (i - 1)/2.
To consstruct the binary minheap, we can use a heapify down approach, start from the last non leaf node (n/2) - 1 down to 0. For each A[i], compare it with its children A[2i + 1] and A[2i + 2] and find the smallest element among them. If the smallest element is not A[i], swap A[i] with it. Recursively implement this approach on the smallest element/child that was swapped.
The work would be O(n) as this heapify approach is proportional to the height of the subtree it operates on so total work would be $\sum_{h=0}^{log n}$ $(n/2^{h+1})$ * h = O(n)



- **2b.**
The span of the approach would be max height of the tree which is O(log(n)).



- **3a.**
Start by finding the largest coin of ${2^i}$ such that ${2^i} < N$ 
Add 1 coin of ${2^i}$ into the solution. 
Subtract ${2^i}$ from N so the new amount is N - ${2^i}$
if the new amount is > 0, repeat the algorithm with the new amount. If it is 0, stop, the solution has been found.


- **3b.**
We picked the largest denomination coin ${2^i}$ at each iteration, so any other coin ${2^j}$ would be smaller and any combination of smaller coins cannot sum up to ${2^i}$. We need 2 of $2^{i-1}$ to sum up to ${2^i}$. Hence by picking ${2^i}$ always, it is always included in the optimal solution since it is the most efficient way to reduce the amount and any other set of coins that does not include ${2^i}$ but also sums to N would have to use a larger number of smaller coins to make up for ${2^i}$, making it non-optimal.




- **3c.**
We repeatedly find the largest power of 2 less than or equal to N and subtract it from N. This process continues until N becomes 0. This is equivalent to splitting the tree into half each time, binary representation of N. Each step takes O(1) time to find the next coin. Hence the work is O(logN) and the  span is also O(logN).


- **4a.**
Suppose D={1,3,4}, N = 6. Using Greedy algorithm, we would pick 4 since its the largest coin < 6 and then for the remainder 2, we would pick 1 twice, (4 + 1 + 1) total 3 coins. However, the optimal solution would be to pick (3+3), total only 2 coins required. Hence the greedy algorithm does not produce the fewest number of coins.


- **4b.**
Finding the minimum number of coins to make change for an amount N with denominations D exhibits the optimal substructure property. Suppose an optimal solution S of n contains coin d and the remainder set of coins R sums to n - d. If R were not an optimal solution for n - d, there exists a better solution R' with fewer coins summing to n - d. Replace R with R' and add coin d → we get a solution for n with fewer coins than S, contradicting optimality of S. Hence R must be optimal for n - d. This shows optimal substructure holds.




- **4c.**
Let M[0..N] where M[n] = minimum number of coins to make n
Initialize M[0] = 0 and the rest of the array to infinity.
For each element x from 1 to N, for each denomination d of coin with d <= x, M[x] = min(M[x], 1 + M[x - d]).
The result would be that M[N] is the minimum coin count or infinity if impossible. 
The work would be O(k * N) where k is the number of coin denominations and N is the target value. This is because for each of the N steps, we iterate over up to k denominations. 
The span would be O(Nlog(k)) since the algorithm is sequential and M[x] depends on previously computed M[x - d] for smaller values. However for a fixed x, the inner min over k denominations can be done in parallel with span O(log k) (parallel reduction). Thus span ≈ sum over x of O(log k) = O(N · log k).
- **5a.**
Yes. First, sort tasks from 1...n by fnish times. Let p(i) be the index of the last task that finishes ≤ ${s_i}$. Let OPT(i) = maximum total value achievable using tasks 1..i.
The optimal solution would then be:
${OPT(i)=max(v_i​+OPT(p(i)),OPT(i−1))}$
This is because for the optimal solution, either it contains task i or it does not. If it does, then the other tasks in the optimal solution must lie in 1..p(i) or else they would overlap. If it does not, the optimal subproblem would just be ${OPT(i−1)}$

- **5b.**
No.
CounterExample 1: 
Tasks: A: {s=0, f=4, v=100} B: {s=0, f=1, v=60} C: {s=1, f=2, v=60} D: {s=2, f=3, v=60}
If we pick based on the largest value first,
We will pick task A and then not be able to pick tasks B-D because they overlap with task A. But the optimal solution would be to pick task B, C and D, summing up to 180 instead of 100 for just task A.
CounterExample 2:
Tasks: A: {s=0, f=2, v=1} B: {s=2, f=4, v=1} C: {s=4, f=6, v=1} D: {s=0, f=6, v=10}
If we pick based on earliest finish time first, it would be task A, B, C adding up to 3. But the optimal solution would be to pick Task D which has value 10 > 3.
Hence greedy algorithm by largest value first and earliest finish time fails to achieve an optimal solution.
- **5c.**
Dynamic programming algorithm: Sort the task by finish time, for each task i, compute p(i) such that ${p(i) = }$ largest ${j < i}$ such that ${f_j <= s_i}$. In other words, the index of the latest non-overlapping task before job i. Job j can be found in O(logn) by binary search.
${DP[0]= 0}$ For i = 1...n:
${DP[i]=max(v_i​+DP(p(i)),DP(i−1))}$
The answer to the problem, would be ${OPT[n]}$
Sorting the tasks takes O(nlogn), Finding all p(i) takes O(nlogn), total n iterations of DP loop, so total work is O(nlogn).
The DP algorithm is sequential, each DP[i] depends on DP[i-1] and DP[p(i)]. Although the array can be sorted in parallel and binary search can be done in parallel giving O(logn) the DP recurrence has to be done sequentially with a dependency chain of length n hence Span is O(n).
