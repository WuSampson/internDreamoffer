def match(s):
    countleft=[]; #未匹配的左括号栈
    list=[]; #输出字符串，代替java中的StringBuffer？
    for index in range(len(s)):
        char=s[index]
        if char =='(':
            list.append(' ')
            countleft.append(index)
        elif char ==')':
            if(bool(countleft)):
                list.append(' ')
                countleft.pop()
            else:
                list.append('?')#未匹配的右括号
        else:
            list.append(' ')
    for i in countleft:#未匹配的左括号
        list[i]='x'
    s="".join(list)
    # print(s)
    return s

if __name__ == "__main__":
    ss=['bge)))))))))','((IIII))))))','()()()()(uuu','))))UUUU((()']
    for s in ss:
        print(s)
        print(match(s))
        print("")
