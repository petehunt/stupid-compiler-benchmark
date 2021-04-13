# stupid-compiler-benchmark

This is the world's stupidest compiler benchmark. It compiles 50 1kloc files that print "hello world" a bunch of times to the console.

It is stupid, but it is also an apples-to-apples comparison, and indicates the order of magnitude of iteration speed we can expect.

When I run it on my 2020 13" MBP I get the following output:

```
Wrote 50 files per language, 1000 statements each

java

real	0m1.907s
user	0m6.657s
sys	0m0.239s

golang

real	0m0.247s
user	0m0.226s
sys	0m0.233s

TypeScript, no type checking (esbuild)

real	0m0.058s
user	0m0.204s
sys	0m0.075s

TypeScript, with type checking (tsc)

real	0m3.789s
user	0m5.201s
sys	0m0.199s
```

tsc with typechecking is about 2x slower than javac. esbuild is about 30x faster than javac.
