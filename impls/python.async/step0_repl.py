import asyncio
from async_readline import read_lines

async def READ(code):
    return code

async def EVAL(ast):
    return ast

async def PRINT(expr):
    return expr

async def rep(code):
    return await PRINT(await EVAL(await READ(code)))

async def main():
    async for code in read_lines():
        print(await rep(code))
    print("Bye!")
if __name__ == "__main__":
    asyncio.run(main())
