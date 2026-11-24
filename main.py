#!/usr/bin/env python3
"""Butterfly Protocol — make.fun entry (u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)"""
import os

ENTRY_LINE = "Warning: do not pet the butterfly. Your Wi-Fi will be worse, and everyone will still check their phones."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
