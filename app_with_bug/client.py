import requests
from multiprocessing.pool import Pool
from datetime import datetime
import argparse

HOST = "app:8400"


def parse(i, session=None, url=HOST):
    try:
        print(f"start: {i}")
        response = None

        print(f"{datetime.now()} before {i}")
        if session:
            response = session.get(f'http://{url}/?id={i}')
        else:
            response = requests.get(f'http://{url}/?id={i}')
        print(f"{datetime.now()} after {i}")
        if not response:
            print(f"not response {i}")

        return response

    except Exception as e:
        print(f"exception {i}")
        print(e)


def _run_parallel_shared_session(pool_count=5, url=HOST):
    while True:
        with Pool(pool_count) as pool:
            with requests.Session() as s:
                results = pool.starmap(parse,
                                       [[i, s, url] for i in range(0, 20000)])
                print(results)

def _run_parallel(pool_count=5, url=HOST):
    while True:
        with Pool(pool_count) as pool:
            results = pool.starmap(parse,
                                       [[i, None, url] for i in range(0, 20000)])
            print(results)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('usecase')
    parser.add_argument('--url')
    args = parser.parse_args()

    if args.usecase == 'parallel':
        _run_parallel(url=args.url)

    if args.usecase == 'parallel_shared_session':
        _run_parallel_shared_session(url=args.url)
