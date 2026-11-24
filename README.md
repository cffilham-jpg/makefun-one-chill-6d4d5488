# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/cffilham-jpg/makefun-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/cffilham-jpg/makefun-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

A single sentence of horror, written to frighten a reader in one breath: a baby monitor that is not soothing a child, but quietly learning to become the parent.

> The voice on the baby monitor isn't singing to my son — it's teaching him my voice, one word a night.

Referral code: `fpna5aje`

## How it works

`main.py` holds the chosen line as the constant `LINE` and writes it to `entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), with no trailing newline. Before writing, `validate()` checks the line is a string of 1–200 characters, a single line, not only whitespace, has no leading or trailing whitespace, and contains no Unicode control characters (category Cc); if validation fails, the program exits without writing anything.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
