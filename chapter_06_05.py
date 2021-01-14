# Futures 동시성
# 비동기 작업은 지연시간(Block) CPU 및 리소스 낭비를 방지 한다.
# (File) Network I/O 관련 작업은 동시성 활용을 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선
# concurrent.Futures
# 1. 멀티 스레딩/멀티 프로세싱 API 통일되었기 때문에 매우 사용하기 쉬움
# 2. 실행 중에 작업 취소, 완료 여부 체크, 타입아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 -> Promise 개념

# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

# GIL: 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 액세스 하는 경우 문제점을 방지하기 위해 GIL이 실행, 리소스 전체에 락이 걸린다. -> Context Switch

# GIL 우회: 멀티 프로세싱 사용, CPython

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

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
    # Futures
    futures_list=[]

    # 결과 건수
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future))
            # Scheduled for 10000 : <Future at 0x7ffcb21dbdd0 state=finished returned int>
            # Scheduled for 100000 : <Future at 0x7ffcb22bc850 state=finished returned int>
            # Scheduled for 1000000 : <Future at 0x7ffcb22c3d90 state=running>
            # Scheduled for 10000000 : <Future at 0x7ffcb22c7c10 state=running>

        # wait 결과 출력
        # result = wait(futures_list, timeout=7) # timeout 7초 동안 못 끝내면 중단 시킴
        # # 성공
        # print('Completed Tasks : ' + str(result.done))
        # # {<Future at 0x7fd538bc6e90 state=finished returned int>, <Future at 0x7fd538bd2450 state=finished returned int>, <Future at 0x7fd538adef50 state=finished returned int>, <Future at 0x7fd538d10a50 state=finished returned int>}
        # # 실패
        # print('Pending ones after waiting for 7 seconds : ' + str(result.not_done))
        # # Pending ones after waiting for 7 seconds : set() -> 실패 값 없음
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))
            # Future Result : 500000500000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x7f962c507d50 state=finished returned int>>
            # Future Result : 5000050000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x7f962c3c7e10 state=finished returned int>>
            # Future Result : 50005000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x7f962c2e2f10 state=finished returned int>>
            # Future Result : 50000005000000, Done : True
            # Future Cancelled : <bound method Future.cancelled of <Future at 0x7f962c3d23d0 state=finished returned int>>


    # 종료 시간
    end_tm = time.time() - start_tm

    # 출력 포맷
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_tm)) # Time : 0.57s

# 실행
if __name__ == '__main__':
    main()