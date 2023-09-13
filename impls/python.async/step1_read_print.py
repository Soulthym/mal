from async_readline import read_lines
from async_reader import read_str
from async_printer import pr_str
import traceback
import asyncio
import sys

async def READ(code):
    return await read_str(code)

async def EVAL(ast):
    return ast

async def PRINT(expr):
    return pr_str(expr)

async def rep(code):
    return await PRINT(await EVAL(await READ(code)))

async def main():
    async for code in read_lines():
        try:
            print(await rep(code))
        except Exception as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
    print("Bye!")
if __name__ == "__main__":
    asyncio.run(main())
