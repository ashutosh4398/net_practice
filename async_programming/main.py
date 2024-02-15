import asyncio

# create a co-routine
# returns a co-routine, and need to handle via await
async def foo():
    print("async code")

async def main(text):
    task = asyncio.create_task(foo())
    print(text)
    slp = await asyncio.sleep(1)
    await foo()
    print(slp)
    print("Done with sleeping...")

# creates an event loop
asyncio.run(main("ashutosh"))