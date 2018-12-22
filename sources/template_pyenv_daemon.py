#!/usr/bin/env python3.7

import iterm2
# To install packages from PyPI, use this command, changing package_name to the package you
# wish to install:
#   "$$PYTHON_BIN$$/pip3" install package_name

async def main(connection):
    # This is an example of using an asyncio context manager to register a custom control
    # sequence. You can send a custom control sequence by issuing this command in a
    # terminal session in iTerm2 while this script is running:
    #
    # printf "\033]1337;Custom=id=%s:%s\a" "shared-secret" "create-window"
    async with iterm2.CustomControlSequenceMonitor(connection, "shared-secret", r'^create-window$') as mon:
        while True:
            match = await mon.async_get()
            await iterm2.Window.async_create(connection)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)
