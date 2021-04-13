# stupid-compiler-benchmark

This is the world's stupidest compiler benchmark. It compiles 50 1kloc files that prints "hello world" a bunch of times to the console.

It is stupid, but it is also an apples-to-apples comparison, and indicates the order of magnitude of iteration speed we can expect.

When I run it on my 2020 13" MBP I get the following output:

```
Cold compile: java

real	0m1.663s
user	0m6.373s
sys	0m0.207s

Cold compile: esbuild (no typechecking)

real	0m0.054s
user	0m0.196s
sys	0m0.071s

Cold compile: tsc (typechecking)

real	0m3.529s
user	0m4.825s
sys	0m0.170s
```

tsc with typechecking is about 2x slower than javac. esbuild is about 30x faster than javac.
