import asyncio
import re

class Reader:
    def __init__(self, tokens, index=0):
        self.tokens = tokens
        self.index = index

    def next(self):
        self.index += 1
        return self.tokens[self.index-1]

    def peek(self):
        if self.index < len(self.tokens):
            return self.tokens[self.index]
        return None

MALTOKENS = re.compile(r'''[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)''')
async def tokenize(code):
    print("Tokenizing", code)
    tokens = [t for t in MALTOKENS.findall(code)
              if t and t[0] != ';']
    print("Tokens", tokens)
    return tokens

INT = re.compile(r'^-?\d+$')
async def read_atom(reader):
    token = reader.next()
    if INT.match(token): return int(token)
    return token

async def read_list(reader):#(
    sentinel = ')'
    ast = []
    reader.next() # consume left delimeter
    while (t:=reader.peek()) != sentinel:
        if not t: raise Exception(f"expected {sentinel!r}, got EOF")
        ast.append(await read_form(reader))
    reader.next() # consume right delimeter
    return ast

async def read_form(reader):
    token = reader.peek()
    if token[0] == ';':
        reader.next()
        return None
    elif token == '(':
        return await read_list(reader)
    else:
        return await read_atom(reader)

async def read_str(code):
    tokens = await tokenize(code)
    return await read_form(Reader(tokens))

async def main():
    code = input("user> ")
    tokens = await tokenize(code)
    reader = Reader(tokens)

if __name__ == "__main__":
    asyncio.run(main())
