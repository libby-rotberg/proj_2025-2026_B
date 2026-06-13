# id1: 215537218
# name1: Nehora Shabtay
# username1: nehora
# id2: 216191627
# name2: Libby Rotberg
# username2: Libbyrotberg


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.height!=-1


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    @type is_avl: boolean
    @param is_avl: If True then tree is AVL, otherwise it is just a "regular" binary search tree, without rotations.
    """

    def __init__(self, is_avl):
        self.root = None
        self.is_avl = is_avl
        self.size = 0
        self.virtual_node = AVLNode(None, None) 
        self.virtual_node.height = -1

    def get_height(self, node):
        if node is None or not node.is_real_node():
            return -1
        return node.height

    def left_rotate(self, B):
        A = B.right
        B.right = A.left
        if A.left.is_real_node():
            A.left.parent = B
        A.parent = B.parent
        if B.parent is None or not B.parent.is_real_node():
            self.root = A
        elif B == B.parent.left:
            B.parent.left = A
        else:
            B.parent.right = A
        A.left = B
        B.parent = A        
        B.height = max(self.get_height(B.left), self.get_height(B.right)) + 1
        A.height = max(self.get_height(A.left), self.get_height(A.right)) + 1
        return A

    def right_rotate(self, B):
        A = B.left
        B.left = A.right
        if A.right.is_real_node():
            A.right.parent = B
        A.parent = B.parent
        if B.parent is None or not B.parent.is_real_node():
            self.root = A
        elif B == B.parent.left:
            B.parent.left = A
        else:
            B.parent.right = A
        A.right = B
        B.parent = A
        B.height = max(self.get_height(B.left), self.get_height(B.right)) + 1
        A.height = max(self.get_height(A.left), self.get_height(A.right)) + 1
        return A

    """searches for a node in the dictionary corresponding to the key (starting at the root)

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x, search_time) where x is the node corresponding to key (or None if not found)
    and search_time is the search time, as defined and explained in the assignment.
    """

    def search(self, key):
        return None, -1

    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int,int)
    @returns: a 4-tuple (x, search_time, rotations, height_changes), where x is the new node
    and the other 3 return values are as defined and explained in the assignment.
    """

    def insert(self, key, val):
        new_node = AVLNode(key, val)
        new_node.left = self.virtual_node
        new_node.right = self.virtual_node
        if self.is_avl:
            new_node.height = 0

        search_time = 0
        parent = None
        curr = self.root
        while curr is not None and curr.is_real_node():
            search_time += 1
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        search_time += 1

        new_node.parent = parent
        if parent is None or not parent.is_real_node():
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self.size += 1
        
        rotations = 0
        height_changes = 0
        
        if self.is_avl:
            y = parent
            while y is not None and y.is_real_node():
                left_h = self.get_height(y.left)
                right_h = self.get_height(y.right)
                bf = left_h - right_h
                new_height = max(left_h, right_h) + 1
                height_changed = (new_height != y.height)
                if abs(bf) < 2:
                    if not height_changed:
                        break
                    else:
                        y.height = new_height
                        height_changes += 1  
                        y = y.parent
                else:
                    if bf == 2:
                        left_bf = self.get_height(y.left.left) - self.get_height(y.left.right)
                        if left_bf >= 0: 
                            self.right_rotate(y)
                            rotations += 1
                        else:
                            self.left_rotate(y.left)
                            self.right_rotate(y)
                            rotations += 2
                    else: 
                        right_bf = self.get_height(y.right.left) - self.get_height(y.right.right)
                        if right_bf <= 0: 
                            self.left_rotate(y)
                            rotations += 1
                        else:  
                            self.right_rotate(y.right)
                            self.left_rotate(y)
                            rotations += 2
                    break
                    
        return new_node, search_time, rotations, height_changes

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        return

    """returns a list representing dictionary 

    @rtype: list
    @returns: a list of (key, value) tuples sorted by key, representing the data structure
    """

    def avl_to_list(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return None

    """returns the height of the tree

        @rtype: int
        @returns: the height of the tree 
        """

    def get_height(self):
        return -1
