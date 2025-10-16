import time, random

MEAN = 2.5  # 평균 간격(초)

def sleep_poisson(mean=MEAN, low=0.3, high=10):
    # 지수분포에서 샘플링
    t = random.expovariate(1.0 / mean)
    # 극단값 컷
    t = max(low, min(high, t))
    return t