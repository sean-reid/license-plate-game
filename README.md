# License Plate Game

Algorithm benchmarking tools for a fun road trip game.

## Background

The rules of the license plate game are:
1. Take the first three letters from a license plate. For example, 5EVK495 -> EVK
2. Make a word out of those letters, in that order. The letters do not need to be next to each other in the word.
3. For the example above, EVK could make the word "revoke" or even "evoke".
4. The shortest word wins!

## Getting started

This repo includes a tool to benchmark the runtimes of different solutions to this game.

### Install dependencies

Install `uv` and `direnv` to run the benchmarking tool.

Install `uv` on Mac or Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install direnv on Mac or Linux:
```
curl -sfL https://direnv.net/install.sh | bash
```

Then enable direnv by adding this line to your bash profile:
```
eval "$(direnv hook bash)"
```

Then clone this repo and `cd` into it.

You might need to allow direnv in the directory:
```
direnv allow .
```

### Test runner

You can invoke the tool and make sure everything is configured with the following:
```
runner -h
```

### Run benchmarks

Currently, two algorithms are supported:
- Brute Force: searches through the entire dictionary upon each letter combo to find the shortest word
- Naive: with some preprocessing (in fixed time), generates a dict that allows fast searching for the answer

To run the tests for the brute force algorithm:
```
runner --name brute_force
```

To run the tests for the naive algorithm:
```
runner --name naive
```

### Testing

Add your own tests to the runner by adding a file to `test_data` that has a letter combo test case in each row.

For example, take a look at `test_data/combos1.txt`.

Point the runner at this file by passing the file's short name (excluding the .txt extenstion) as an argument:
```
runner --test combos1
```

### Custom dictionary

If you want to pass a custom dictionary as a reference, you can do add a dictionary file to `word_data` with a word in each row.

For example, take a look at `word_data/words_alpha.txt`.

Pass the dictionary short name as an argument:
```
runner --dictionary words_alpha
```

## Author
- Sean Reid
