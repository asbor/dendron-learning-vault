# Pipes

Pipes allow you to connect the output of one command to the input of another command using the `|` operator. This is a fundamental concept in Unix/Linux systems that enables powerful command chaining.

## Basic Pipe Examples

### Combining cat and head

```bash
cat canada.txt | head -n 5
```

This command displays the first 5 lines of the `canada.txt` file.

### Pattern Matching with Counting

```bash
grep "[aeiou]$" states.txt | wc -l
```

This command finds all lines ending with vowels in `states.txt` and counts them.

### Listing with Filtering

```bash
ls -al | grep "Feb" | less
```

This command lists all files, filters for those created in February, and displays them in a pager. Remember you can use the Q key to quit `less` and return to the prompt.

## Pipes Exercises

### Exercise 1

Use pipes to figure out how many US states contain the word "New."

**Solution:**

```bash
grep "New" states.txt | wc -l
```

### Exercise 2

Examine your `~/.bash_history` to try to figure out how many unique commands you've ever used. (You may need to look up how to use the `uniq` and `sort` commands).

**Solution:**

```bash
cat ~/.bash_history | sort | uniq | wc -l
```

## Key Concepts

- Pipes (`|`) connect command outputs to inputs
- Commands can be chained together for complex operations
- Data flows from left to right through the pipe
- Each command in the pipeline processes the output of the previous command

## Related Topics

- [[data-engineering.course.unix-workbench.bash-fundamentals.commands]]
- [[data-engineering.course.unix-workbench.bash-fundamentals.find]]
- [[data-engineering.course.unix-workbench.regex.metacharacters]]