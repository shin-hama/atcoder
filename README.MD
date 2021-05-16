# AtCoder answer

This repository is record of my challenge of atcoder

## Result

| date        | title                                                              | score |
| ----------- | ------------------------------------------------------------------ | ----- |
| 2021/05/15  | [AtCoder Beginner Contest 201](https://atcoder.jp/contests/abc201) | 300   |
| 2021/05/16~ | [競プロ典型 90 問](https://atcoder.jp/contests/typical90)          | None  |

## Tips for python

### PyPy を使う

`Python` は処理が遅いため、普通にコードを書くと N が増えるにつれて `TLE` しやすくなってしまう。
そのため、提出の際は `Python3` で提出するのではなく `PyPy3` を使う

例：[./standard90/004.py](./standard90/004.py)

- Python3 : 2214 ms => TLE
- PyPy3 : 850 ms 　=> AC
  - 提出方法を変えただけで、処理時間が半分程度まで減少

注意点として、PyPy は Python 3.6 までしかサポートしてないっぽい
