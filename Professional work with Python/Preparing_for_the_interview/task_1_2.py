# class Stack:

#     def __init__(self, item) -> None:
#         self.item = item
#         self.max_elem = len(item)

#     def is_empty(self) -> bool:
#        return bool(len(self.item) == 0)

#     def push(self, element) -> None:
#         self.item = self.item + element

#     def pop(self) -> str:
#         come_back = self.item[-1:]
#         # self.max_elem = self.max_elem - 1 
#         self.item = self.item[:-1]
#         return come_back

#     def peek(self) -> str:
#         return self.item[-1:]

#     def size(self) -> str:
#         return len(self.item)
        

# if __name__ == "__main__":
#     # stack = Stack('(((([{}]))))')
#     # print(stack.size())
#     # print(stack.peek())
#     string = input()
#     stack = Stack(string)
#     if stack.size() % 2 != 0:
#         print("Несбалансированно")
#     else:
#         opening = str()
#         ending = str()
#         for index in range(len(string)):
#             if stack.size == 0:
#                 break
#             elif stack.peek() in [")", "]", "}"]:
#                 opening = stack.pop() + opening
#             else:
#                 for item in opening:
#                     elem = stack.peek()
#                     if item == ")" and elem == "(":
#                         stack.pop()
#                         continue
#                     elif item == "]" and elem == "[":
#                         stack.pop()
#                         continue
#                     elif item == "}" and elem == "{":
#                         stack.pop()
#                         continue
#                     elif stack.peek() in [")", "]", "}"] and (stack.size() % 2 != 0) :
#                         opening = opening[-1:]
#                         break
#                     else:
#                         print("Несбалансированно")
#                         exit()
#                 if len(opening) != 1:
#                     opening = str()
#         print("Сбалансировано")
def l():
    s = "()"
    if len(s) % 2 != 0:
        return False
    else:
        opening = str()
        for index in range(len(s)):
            if len(s) == 0:
                break
            elif s[-1]  not in [")", "]", "}"]:
                return False
            elif s[-1] in [")", "]", "}"]:
                opening = s[-1] + opening
                s = s[:-1]
                for item in opening:
                    elem = s[-1]
                    if item == ")" and elem == "(":
                        s = s[:-1]
                        continue
                    elif item == "]" and elem == "[":
                        s = s[:-1]
                        continue
                    elif item == "}" and elem == "{":
                        s = s[:-1]
                        continue
                    elif s[-1] in [")", "]", "}"] and (len(s) % 2 != 0) :
                        opening = opening[-1:]
                        break
                    else:
                        return False
                opening = str()
        return True
    
print(l())