# Roast the Gadget — Laptop Sleep Mode

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

An entry for make.fun's **One-Line Roast: The Gadget You Use Every Day** bounty:
one original, single-line roast of the laptop I use every day — funny, fresh,
and neatly worded, in at most 200 characters.

## The roast

> My laptop treats sleep mode as a suggestion: close the lid and it spends all night awake in my bag, warm, glowing, and quietly judging me for going to bed.

## How it works

`main.py` is a small deterministic program. It reads the `MAKEFUN_OUTPUT_DIR`
environment variable (default `/output`) and writes the single roast line to
`entry.txt` there. No network, no model calls, no file reads outside the repo.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
