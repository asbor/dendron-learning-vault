# Environmental Variables

Before we can run our scripts and functions as shell commands, we need to understand **environmental variables**. These are variables where Bash stores data about your current computing environment. The names are **uppercase** by convention.

Common variables:
- `$HOME`: your home directory path
- `$PWD`: current directory path
- `$PATH`: list of directories Bash checks for executable commands

## Checking Environment Variables

```bash
echo $HOME   # e.g., /Users/sean
echo $PWD    # e.g., /Users/sean/Code
```

## Making Your Scripts Globally Available

To run a script from anywhere, add its location to the `$PATH` variable.

### Check the Current PATH

```bash
echo $PATH
# e.g., /usr/local/bin:/usr/bin:/bin:/usr/local/git/bin
```

The `$PATH` variable contains a colon-separated list of directories Bash uses to find executable files.

## Adding a Directory to PATH

1. Create a new directory for your scripts:

```bash
mkdir Commands
```

2. Edit your Bash profile:

```bash
nano ~/.bash_profile
```

3. Add the following lines:

```bash
alias docs='cd ~/Documents'
alias edbp='nano ~/.bash_profile'
export PATH=~/Code/Commands:$PATH
```

4. Save and close the file.

5. Apply changes:

```bash
source ~/.bash_profile
```

## Example Script

Let's say you've created a script called `short` in the `Commands` directory. After the steps above, you can now use it like a normal command:

```bash
short
# A small program
```

## Sourcing Bash Functions

Instead of making each script executable, you can define functions in a `.sh` file and source it from `.bash_profile`.

1. Edit `.bash_profile`:

```bash
nano ~/.bash_profile
```

2. Add the source line:

```bash
source ~/Code/addseq2.sh
```

3. Save and apply:

```bash
source ~/.bash_profile
```

4. You can now run the function directly:

```bash
addseq2 9 8 7
# 24
```

## Summary

- Keep your programs **short, simple, and quiet**
- Use `chmod` to make scripts executable
- Use `~/.bash_profile` to modify environment variables and aliases
- Use `export` to set environment variables
- Use `source` to include reusable functions

## Related Topics

- [[data-engineering.course.unix-workbench.bash-fundamentals.commands]]
- [[data-engineering.course.unix-workbench.functions.basics]]
- [[data-engineering.course.bash-integration.workflows]]