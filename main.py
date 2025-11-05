import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        x = p.get()  # smallest
        y = p.get()  # next smallest
        freq_sum = x.data[0] + y.data[0]
        z = TreeNode(left=x, right=y, data=(freq_sum, ""))  
        p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    
    if code is None:
        code = {}
    if node is None:
        return code
    
    if node.left is None and node.right is None:
        code[node.data[1]] = prefix
        return code

    # Recursive traversal
    get_code(node.left, prefix + "0", code)
    get_code(node.right, prefix + "1", code)
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    n = len(f)  # number of symbols
    bits_per_symbol = math.ceil(math.log2(n))
    total_cost = sum(freq * bits_per_symbol for freq in f.values())
    return total_cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    total_cost = 0
    for char in f.keys():
        total_cost += f[char] * len(C[char])
    return total_cost

if __name__ == "__main__":
    f = get_frequencies('fields.c')
    print("Fixed-length cost:  %d" % fixed_length_cost(f))
    T = make_huffman_tree(f)
    C = get_code(T)
    print("Huffman cost:  %d" % huffman_cost(C, f))


