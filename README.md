# 🧮 Coding Solutions/Representations for Various Mathematical Problems

Welcome to the Mathematical Problem Solving repository! This project provides algorithmic solutions or visualitzations to a variety of mathematical problems. Whether you're a student, developer, or mathematics enthusiast, this repository serves as a practical reference to explore how to tackle complex mathematical tasks. In this repository, you'll find implementations of the following popular mathematical problems:

## ♟️ The Trapped Knight

The Trapped Knight is a mathematical problem centred arround chess. 
For an explanation of the problem, here is a complete article about it: https://scipython.com/blog/the-trapped-knight/

The problem defines a board of n by n (n determined by user) and makes L (2x1) shaped moves until the knight cannot move.

## 🔄🔢 The 3n + 1 Problem (Collatz Conjecture) 

This repository implements a solution to the famous **3n + 1 Problem**, also known as the **Collatz Conjecture**. The conjecture states that, starting with any positive integer `n`, the following process will eventually reach the number 1:
- If `n` is even, divide it by 2.
- If `n` is odd, multiply it by 3 and add 1.

This cycle is repeated until the number reaches 1.

## 🔢🚀 Mersenne Prime Finder

A simple and efficient tool to find **Mersenne Prime Numbers** within a given range of exponents `x` to `y`. A Mersenne prime is a prime number of the form `M_n = 2^n - 1`, where `n` is an integer. This project helps you find all Mersenne primes within any user-defined range by testing exponents between `x` and `y`.

## 🔄🌀 Fibonacci Sequence

This section deals with generating the Fibonacci sequence, where each number is the sum of the two preceding ones, usually starting with 0 and 1. Mathematically, it is defined as:

Fib(0) = 0
Fib(1) = 1
For n >= 2: Fib(n) = Fib(n-1) + Fib(n-2)

You can visualize and compute Fibonacci sequences of arbitrarily large lengths using this provided implementation.

## 🔢🤝 Greatest Common Divisor Algorithm

This implementation computes the Greatest Common Divisor (GCD) between two integers, which represents the largest positive integer that divides both numbers without leaving a remainder. The algorithm utilizes the Euclidean Algorithm, which efficiently finds the GCD through recursive division, starting with:

( \text{GCD}(a, b) = \text{GCD}(b, a % b) )
Until ( b = 0 ), at which point ( a ) is the GCD.

## 🔢🔺 Pascal’s Triangle

The repository includes an algorithm to generate Pascal’s Triangle, a triangular array where each number is the sum of the two numbers directly above it. This structure is used in combinatorics and binomial expansions, providing:

Row 0: [1]
Row 1: [1, 1]
Row 2: [1, 2, 1], and so on.

Pascal’s Triangle contains numerous interesting properties and applications in mathematics.

## 🔍 Prime Number Checker

With this algorithm, you can check for prime numbers. A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself. The algorithm efficiently checks primality by testing whether a number is divisible by any integer up to its square root.

## 📐🔢 Pythagoras Calculator

Using the Pythagorean Theorem, this calculator computes the length of the hypotenuse ( c ) in a right triangle given the lengths of the other two sides a and b, following the equation:

( c^2 = a^2 + b^2 )
Thus, ( c = \sqrt{a^2 + b^2} ), where ( a ) and ( b ) are the two perpendicular sides.

This classic theorem is foundational in geometry and widely used to solve distance-related problems.