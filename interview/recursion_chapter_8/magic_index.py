class BinaryNode(object):
    "Binary search tree."
    __slots__ = 'left', 'right', 'index','value'
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def add_children(data, parent, step):
    "Add both children for node."
    left_index = parent.index - step 
    if left_index >= 0 and left_index != parent.index:
        left = BinaryNode(index=left_index, value=data[left_index])
        parent.left = left
        add_children(data, left, step // 2)
    else:
        parent.left = None
    right_index = parent.index + step 
    if right_index != parent.index:
        right = BinaryNode(index=right_index, value=data[right_index])
        parent.right = right
        add_children(data, right, step // 2)
    else:
        parent.right = None

def create_bst(data):
    length = len(data)
    if length:
        index = length // 2
        step =  (length - index) // 2
        root = BinaryNode(index=index, value=data[index])
        add_children(data, root, step)
        return root
    return

def visit(node: BinaryNode):
    print(f'Visit node data[{node.index}] = {node.value}')
    if node.index == node.value:
        return node.index
    
def pre_order_traversal(node: BinaryNode):
    "Pre-order traversal visits the current node before its child nodes."
    if node:
        index = visit(node)
        if index:
            return index
        if node.left:
            index = pre_order_traversal(node.left)
            if index:
                return index
        if node.right:
            index = pre_order_traversal(node.right)
            if index:
                return index

def magic_index(data: tuple):
    """ Magic Index: A magic index in an array A [0, ..., n -1] is defined to
        be an index such that A[i] = i. Given a sorted array of distinct 
        integers, write a method to find a magic index, if one exists, in 
        array A.
        FOLLOW UP
        What if the values are not distinct?
        Hints: # 170, #204, #240, #286, #340
    """
    root = create_bst(data)
    magic_index = pre_order_traversal(root)
    if magic_index:
        print('Found magic index: {}'.format(magic_index))
    else:
        print('Magic index not found.')    

def magic_index_inplace(data: tuple):
    
    def step_generator(start):
        step = start
        while True:
            step = step // 2
            if step:
                yield step
            else:
                yield 1
                break

    def jump(data, index, step):
        "Jump to better index halving steps."
        print(f'Checking index: {index}', f'step: {step}')
        if index < 0 or index >= len(data):
            return None
        if data[index] == index:
            return index

        if not step:
            return None
        else:
            step = max(1, step // 2)
        if data[index] > index:
            return jump(data, index - step, step)
        elif data[index] < index:
            return jump(data, index + step, step)

    magic_index = jump(data, len(data) // 2, len(data) // 2)
    if magic_index is not None:
        print('Found magic index: {}'.format(magic_index))
    else:
        print('Magic index not found.')    


if __name__ == '__main__':
    data = (-1, 0, 1, 2, 4)
    # magic_index(data)
    magic_index_inplace(data)
    data = (0, 2, 4, 5, 8, 10, 20, 30, 31)
    # magic_index(data)
    magic_index_inplace(data)