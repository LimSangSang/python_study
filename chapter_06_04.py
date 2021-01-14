# Futures 동시성
# 비동기 작업은 지연시간(Block) CPU 및 리소스 낭비를 방지 한다.
# (File) Network I/O 관련 작업은 동시성 활용을 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티 스레딩/멀티 프로세싱 API 통일되었기 때문에 매우 사용하기 쉬움
# 2. 실행 중에 작업 취소, 완료 여부 체크, 타입아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

# GIL: 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 액세스 하는 경우 문제점을 방지하기 위해 GIL이 실행, 리소스 전체에 락이 걸린다. -> Context Switch

# GIL 우회: 멀티 프로세싱 사용, CPython

import os
import time
from concurrent import futures

WORK_LIST=[10000, 100000, 1000000, 10000000] # 동시에 4개의 스레드를 이용해 일을 시켜볼 것.

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))
    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor
    with futures.ThreadPoolExecutor() as excutor:
        # map -> 작업 순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)

    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm)) 
    # Result -> [50005000, 5000050000, 500000500000, 50000005000000] Time : 0.56s

# 실행
if __name__ == '__main__':
    main()