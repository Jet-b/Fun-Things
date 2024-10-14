import networkx as nx
import matplotlib.pyplot as plt

class Stack():
    
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []


symbols = ['+', '-', '*', '/']

def evaluate_expression(expression):
    stack = Stack()
    expression = expression.split()
    for item in expression:
        if item in symbols:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                raise ValueError("Invalid expression")
            result = eval(f"{operand1} {item} {operand2}")
            stack.push(result)
        else:
            stack.push(item)

    return stack.pop()

def expression_to_reverse_polish(expression):
    stack = Stack()
    expression = expression.split()
    reverse_polish = []
    for item in expression:
        if item in symbols:
            stack.push(item)
        else:
            reverse_polish.append(item)
            while not stack.is_empty():
                reverse_polish.append(stack.pop())
    return " ".join(reverse_polish)

def reverse_polish_to_expression(expression):
    stack = Stack()
    expression = expression.split()
    for item in expression:
        if item in symbols:
            item1 = stack.pop()
            item2 = stack.pop()
            stack.push(f"{item1} {item} {item2}")
        else:
            stack.push(item)
    return stack.pop()

def tree_from_post_order_traversal(post_order):
    tree = [None] * (len(post_order) + 1)
    index = 1
    
    def recur(index, post_index):
        if post_index >= len(post_order):
            return post_index
        if 2 * index < len(tree):
            post_index = recur(2 * index, post_index)
        if 2 * index + 1 < len(tree):
            post_index = recur(2 * index + 1, post_index)
        tree[index] = post_order[post_index]
        post_index += 1
        return post_index
    
    recur(index, 0)
    return tree

def draw_tree(tree):
    G = nx.DiGraph()
    
    def add_edges(index):
        if index >= len(tree) or tree[index] is None:
            return
        if 2 * index < len(tree) and tree[2 * index] is not None:
            G.add_edge(tree[index], tree[2 * index])
            add_edges(2 * index)
        if 2 * index + 1 < len(tree) and tree[2 * index + 1] is not None:
            G.add_edge(tree[index], tree[2 * index + 1])
            add_edges(2 * index + 1)
    
    add_edges(1)
    
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=200, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.show()


if __name__ == "__main__":
    
    print(expression_to_reverse_polish("5 * 3 + 6"))
    
    draw_tree(tree_from_post_order_traversal(expression_to_reverse_polish("5 * 3 + 6"))) # something wrong here