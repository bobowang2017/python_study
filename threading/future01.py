from concurrent.futures import ThreadPoolExecutor
import time


def say_hello(a):
    print("hello: " + a)
    time.sleep(2)


def main():
    seed = ["a", "b", "c"]
    start1 = time.time()
    for each in seed:
        say_hello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))
    start2 = time.time()
    with ThreadPoolExecutor(100) as executor:
        for each in seed:
            executor.submit(say_hello, each)
    end2 = time.time()
    print("time2: " + str(end2 - start2))
    start3 = time.time()
    with ThreadPoolExecutor(100) as executor1:
        executor1.map(say_hello, seed)
    end3 = time.time()
    print("time3: " + str(end3 - start3))


if __name__ == '__main__':
    main()
