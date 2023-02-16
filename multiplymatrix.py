#!/usr/bin/env python3
import time
import numpy as np

N = 4096

# X = randn(n) returns an n-by-n matrix of normally distributed random numbers.
if __name__ == '__main__':
    A = np.random.randn(N, N).astype(np.float32)  # astype : for converting dtype
    B = np.random.randn(N, N).astype(np.float32)

    # complexity : N^2 output cells with 2N compute each
    # flop : floating point operation & flops : floating point operations per second
    flop = (N * N * 2 * N)
    print(f"{flop / 1e9:.2f} GFLOP")

    st = time.monotonic()
    C = A @ B  # multiply matrix
    et = time.monotonic()
    s = et - st

    print(f"{flop/s} FLOP/S")
    print(flop/s)
    # GFLOP : giga flop : system capable of performing 10^9 floating point operations per second
    print(f"{flop / s * 1e-12:.2f} TLOP/S")

    with open("/tmp/matmul", "wb") as f:
        f.write(A.data)
        f.write(B.data)
        f.write(C.data)