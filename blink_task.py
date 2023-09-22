import pyfirmata
from pyfirmata import Arduino
import asyncio

board = pyfirmata.Arduino('COM4')

led1 = board.digital[9]
led2 = board.digital[7]
led3 = board.digital[6]

# Fungsi untuk mengendalikan LED 1 (dibagi 3)
async def blink_led1():
    count = 0
    while True:
        if count % 3 == 0:
            led1.write(1)
        else:
            led1.write(0)
        print(f'counter in led 1: {count}')
        count += 1
        await asyncio.sleep(1)

# Fungsi untuk mengendalikan LED 2 (dibagi 4)
async def blink_led2():
    count = 0
    while True:
        if count % 4 == 0:
            led2.write(1)
        else:
            led2.write(0)
        print(f'counter in led 2: {count}')
        count += 1
        await asyncio.sleep(1)

# Fungsi untuk mengendalikan LED 3 (dibagi 5)
async def blink_led3():
    count = 0
    while True:
        if count % 5 == 0:
            led3.write(1)
        else:
            led3.write(0)
        print(f'counter in led 3: {count}')
        count += 1
        await asyncio.sleep(1)

async def main():
    # Jalankan tiga fungsi untuk mengendalikan LED secara bersamaan
    await asyncio.gather(blink_led1(), blink_led2(), blink_led3())

if __name__ == '__main__':
    asyncio.run(main())
