
                    
def isValid(s) -> bool:
    s
    open = []
    for i in s:
        if i == '{' or i == '(' or i == '[':
            open.append(i)
        elif i == ']':
            if open[-1] == '[':
                return True
            else:
                return False
        elif i == ')':
            if open[-1] == '(':
                return True
            else:
                return False
        elif i == '}':
            if open[-1] == '{':
                return True
            else:
                return False
            
def main():
    string = '()'
    isValid(string)

main()