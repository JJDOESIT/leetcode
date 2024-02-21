

def addBinary(a: str, b: str) -> str:
        newStr = ""
        carry = False

        a = list(a)
        b = list(b)

        if (len(a) > len(b)):
            for i in range(len(a)-len(b)): 
                  b.insert(0,'0')

        if (len(b) > len(a)):
            for i in range(len(b)-len(a)):
                  a.insert(0,'0')

        for ptr in range(len(a)):
            if int(a[len(a)-1-ptr]) + int(b[len(b)-1-ptr]) == 2:
                if carry:
                        newStr += '1'
                else:
                        newStr += '0'
                carry = True
            elif int(a[len(a)-1-ptr]) + int(b[len(b)-1-ptr]) == 1:
                if carry:
                    newStr += '0'
                else:
                     newStr += '1'
                     carry = False
            else:
                if carry:
                    newStr += "1"
                else:
                     newStr += "0"
                carry = False
    
        if carry:
             newStr += '1'
        li = list(reversed(newStr))
        li = "".join(li)
        return li



print(addBinary("1010","1011"))

#1 0 1 0
#1 0 1 1
#    0 1