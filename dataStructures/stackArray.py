class stackArray:
    """Create an array to utilize"""
    array = list()
    pointer = -1



    def push(self, item):
        self.pointer += 1
        self.array.append(item)

    def pop(self):
        temp = self.array[self.pointer]
        self.array[self.pointer] = None
        self.pointer -= 1
        return temp

    def peek(self):
        return self.array[self.pointer]

    def isEmpty(self):
        if self.pointer < 0:
            return True
        else:
            return False


"""Driver code below"""
stack = stackArray
stack.push(stack, "gottem")
stack.push(stack, "yeet")
print(stack.peek(stack))
print(stack.pop(stack))
print(stack.pop(stack))