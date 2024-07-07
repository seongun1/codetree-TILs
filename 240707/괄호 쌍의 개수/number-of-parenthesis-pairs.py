def count_valid_transformations(s):
    n = len(s)
    
    # 전체 균형 확인
    total_open = s.count('(')
    total_close = n - total_open

    # 균형이 맞지 않으면 절대 올바른 괄호 문자열이 될 수 없음
    if total_open != total_close:
        return 0

    # 접두사 균형 확인
    prefix_balance = [0] * (n + 1)
    balance = 0
    for i in range(n):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        prefix_balance[i + 1] = balance

    cnt = 0
    for i in range(n):
        if s[i] == '(':
            # 변경: '(' -> ')'
            new_balance = balance - 2
        else:
            # 변경: ')' -> '('
            new_balance = balance + 2

        # 새로운 전체 균형이 맞는지 확인
        if new_balance != 0:
            continue
        
        # 변경 후 올바른 접두사 균형 확인
        valid = True
        for j in range(i + 1):
            if s[j] == '(':
                new_prefix_balance = prefix_balance[j] - 1
            else:
                new_prefix_balance = prefix_balance[j] + 1
            if new_prefix_balance < 0:
                valid = False
                break

        if valid:
            for j in range(i + 1, n):
                if s[j] == '(':
                    new_prefix_balance += 1
                else:
                    new_prefix_balance -= 1
                if new_prefix_balance < 0:
                    valid = False
                    break

        if valid:
            cnt += 1

    return cnt

# 테스트 케이스 입력
s = input()
print(count_valid_transformations(s))