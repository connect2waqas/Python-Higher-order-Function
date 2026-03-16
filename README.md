# Python Higher-Order Functions (with practical Python examples)

Welcome! This repo is a **small, course-style mini track** for learning **higher-order functions in Python**. It’s organized into “lectures” with code you can run, read, and tweak.

If you’ve ever wondered things like:
- “How does `map()` really work?”
- “What does it mean to *pass a function* into another function?”
- “Why do people use `lambda` so much?”

…you’re in the right place.

---

## Course goals (what you’ll learn)

By the end of these examples, you should be able to:

- Explain what a **higher-order function** is
- Pass functions as arguments (callbacks)
- Return functions from other functions (function factories)
- Recognize common Python patterns that depend on higher-order functions

---

## Quick definition: What are Higher-Order Functions?

A **higher-order function** is a function that does at least one of the following:

1. **Takes another function as an argument**, or
2. **Returns a function as a result**

In Python, functions are **first-class objects**. That means you can store them in variables, pass them around, and return them—just like integers or strings.

Common built-in examples you may already know:
- `map(...)`
- `filter(...)`
- `sorted(..., key=...)`
- `lambda` functions
- decorators (very common in real projects)

---

## Repo structure (your “course modules”)

Most of the learning content is inside:

- `Higher Order Functions/`

Inside that folder you’ll find lecture-style directories. Some lectures include a runnable `code.py` file:

- `Higher Order Functions/lecture1/code.py`
- `Higher Order Functions/lecture2/code.py`
- `Higher Order Functions/lecture3/code.py`
- `Higher Order Functions/lecture4/code.py`

There are also additional folders that look like extended practice / projects:

- `Higher Order Functions/Project/`
- `Higher Order Functions/lecture 5/`
- `Higher Order Functions/lecture 6/`
- `Higher Order Functions/lecture7/`
- `Higher Order Functions/project2/`

And one small output file:

- `Higher Order Functions/output.csv`

> Recommended starting point: **lecture1 → lecture4** (they definitely contain `code.py`).

---

## How to run the lessons

### Requirements
- Python 3.x (Python 3.8+ recommended)

### Run a lecture
From the repository root, run:

```bash
python "Higher Order Functions/lecture1/code.py"
```

Swap `lecture1` for other lectures:

```bash
python "Higher Order Functions/lecture2/code.py"
python "Higher Order Functions/lecture3/code.py"
python "Higher Order Functions/lecture4/code.py"
```

---

## Suggested learning path (like a real mini-course)

### Step 1: Read like a student
Open the lecture’s `code.py` and try to answer:
- What function is being passed in?
- What function is being returned?
- What changes if I swap the callback?

### Step 2: Run and observe
Run the file and look closely at the output.

### Step 3: Practice (small edits that teach a lot)
Try these quick exercises:
- Replace a normal `def` callback with a `lambda`
- Add a new test case / new list of values
- Write a *second* callback function and swap it in
- Print intermediate values to see the flow

### Step 4: Rebuild
Try rewriting the same idea in your own words/code.

---

## Why higher-order functions matter (real-world value)

You’ll see these patterns in:
- data processing and cleaning
- reusable utilities
- configuration-driven logic (functions as “plugins”)
- decorators and wrappers

When used well, higher-order functions make code:
- more modular
- easier to reuse
- easier to test
- easier to extend

---

## Contributing / ideas to improve the course

If you’d like to level this repo up even more, great next steps are:
- Add short explanations at the top of each `code.py`
- Add “Expected output” sections per lecture
- Add mini-exercises at the bottom of each lecture
- Add a LICENSE file (MIT is a simple popular option)

---

## License

No license is currently included. If you want others to reuse this repository freely, consider adding an open-source license (MIT is a common simple option).