import readline as pyreadline
from pathlib import Path
import aiofiles
import asyncio
import sys

history_file = Path.home() / ".mal_history"
history_loaded = False

async def ainput(string: str) -> str:
    return (await asyncio.to_thread(input, string)).rstrip("\r\n")

async def read_lines(prompt="user> "):
    global history_loaded
    if not history_loaded:
        try:
            async with aiofiles.open(history_file, "r") as f:
                async for line in f:
                    pyreadline.add_history(line.rstrip("\r\n"))
        except FileNotFoundError:
            pass
        history_loaded = True
    while True:
        try:
            line = await ainput(prompt)
            async with aiofiles.open(history_file, "a") as f:
                pyreadline.add_history(line)
                await f.write(line + "\n")
            yield line
        except IOError:
            pass
        except EOFError:
            break
