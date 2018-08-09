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
    # unbuffered

    c = await boring('boring!')

    for i in range(5):
        print('You say: %s' % (await c.get()))

    print("You're boring: I'm leaving.")


if __name__ == '__main__':
    go_thread(main())
