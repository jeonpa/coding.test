def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    i = 2
    while i <= min(numer, denom):
        if numer % i == 0 and denom % i == 0:
            numer = numer // i  # 분자 약분
            denom = denom // i  # 분모 약분
        else:
            i += 1
    return [numer, denom]