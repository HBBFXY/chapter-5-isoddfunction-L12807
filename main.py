def isOdd(num):
    # 判断是否为整数
    if isinstance(num, int):
        # 判断是否为奇数
        return num % 2 != 0
    # 非整数情况
    return False
