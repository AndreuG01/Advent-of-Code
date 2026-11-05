# Advent of Code

This repository contains the solutions to the [Advent of Code](https://adventofcode.com) problems.

## 2021

This is the first year that I attempt to solve the Advent of Code problems. I have recently learned Java, so I have chosen to use it to solve the problems.

To obtain the solutions to your problem of day `x`, replace the data inside `dayx_data.txt` by your own data. Recompile and run the program

## 2022

This year's solutions have been developed using CPP. To obtain the solutions to your problem of day `x`, go into the folder `2022/Dayx` and change the `data.txt` for your puzzle input and the `example.txt` by the example that Advent of Code provides to us.

## 2023

The chosen language for 2023 has been Python. To obtain the solutions to your problem of day `x`, go into the folder `2023/Dayx` and change the `data.txt` for your puzzle input and the `example.txt` by the example that Advent of Code provides to us.

## 2015 in other languages

The 2015 solutions exist in Python, C++, Rust, Swift and Java, next to each other in `2015/Dayx` and sharing `data.txt` and `example.txt`.

Nothing is installed globally. C++ and Swift use the compilers from the Apple Command Line Tools. Rust and Java are installed inside the repository, in the git-ignored `.tools/` folder:

```bash
./setup_tools.sh                     # install the local Rust and JDK (Apple Silicon Macs)
./run.sh 2015 3 rust                 # compile if needed and run on data.txt
./run.sh 2015 3 cpp example.txt      # run on another input (py, cpp, rust, swift, java)
./verify.sh 2015                     # compare every language against the Python results
```

To remove the toolchains and compiled files: `rm -rf .tools .build`.
