import random

from aiochan import *


async def boring(msg):
    c = Chan()

    async def work():
        i = 0
        while True:
            await c.put(f'{msg} {i}')
            await timeout(random.random()).get()
            i += 1

    go(work())
    return c


async def main():
    c = await boring('Joe')

    while True:
        s, ch = await select(c, timeout(0.8))
        if ch is c:
            print(s)
        else:
            print('You are too slow.')
            return


if __name__ == '__main__':
    go_thread(main())
