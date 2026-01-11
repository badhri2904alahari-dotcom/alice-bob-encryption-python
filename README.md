# Alice & Bob Encryption – Python

This project solves the **Alice & Bob encrypted message decoding problem** using Python.

## Problem Statement
Alice encrypts a message using a dot (`.`) and underscore (`_`) based scheme.
Given an encrypted string, the program finds **all possible valid decoded messages**
and prints them in **alphabetical order**.

## Approach
- Defined the mapping of letters (A–Z) to encrypted codes
- Reversed the mapping for decoding
- Used **backtracking (DFS)** to explore all valid decodings
- Sorted and printed all results

## How to Run

```bash
python decoder.py
