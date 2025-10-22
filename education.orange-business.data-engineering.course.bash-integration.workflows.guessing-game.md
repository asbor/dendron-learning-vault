# Guessing Game Project

A practical example demonstrating the integration of Bash scripting, Make automation, Git version control, and GitHub deployment.

## Project Overview

This project implements a simple number guessing game that asks users to guess how many files are in the current directory. It serves as a complete example of Unix tool integration.

## Script Implementation

### Core Functionality

```bash
#!/usr/bin/env bash
# File: guessinggame.sh

echo "Guess how many files are in the current directory?"

# Function to count the number of files in the current directory
function count_files {
    local file_count=$(ls -1 | wc -l)
    echo $file_count
}

# Function to prompt the user for a guess
function prompt_guess {
    local guess
    read -p "Enter your guess: " guess
    echo $guess
}

# Function to check the user's guess against the actual file count
function check_guess {
    local guess=$1
    local file_count=$2

    if [[ $guess -lt $file_count ]]; then
        echo "Too low!"
    elif [[ $guess -gt $file_count ]]; then
        echo "Too high!"
    else
        echo "Congratulations! You guessed it right!"
        return 0
    fi
    return 1
}

# Main game loop
file_count=$(count_files)
while true; do
    guess=$(prompt_guess)
    check_guess $guess $file_count
    if [[ $? -eq 0 ]]; then
        break
    fi
done
echo "Thanks for playing!"
```

## Key Programming Concepts

### Functions and Modularity

The script demonstrates good programming practices:

- **Modular functions**: Each function has a single responsibility
- **Local variables**: Using `local` to avoid variable conflicts
- **Return codes**: Using return values to communicate success/failure

### Game Logic

- **Input validation**: Handling user input safely
- **Loop control**: Using `while true` with `break` for game loop
- **Conditional logic**: Comparing user guess with actual count

### Shell Features

- **Command substitution**: Using `$(ls -1 | wc -l)` to count files
- **Parameter expansion**: Passing arguments between functions
- **Exit codes**: Using `$?` to check function return values

## Integration Points

This project demonstrates integration with:

- **Make**: Automated documentation generation
- **Git**: Version control for project evolution
- **GitHub**: Repository hosting and deployment
- **GitHub Pages**: Automated website deployment

## Learning Outcomes

Students learn to:

1. Structure Bash scripts with functions
2. Handle user input and feedback
3. Use shell commands for data gathering
4. Implement game logic with loops and conditionals
5. Apply Unix principles of modularity and simplicity

## Related Topics

- [[education.orange-business.data-engineering.course.bash-integration.workflows.makefile-automation]]
- [[education.orange-business.data-engineering.course.bash-integration.workflows.git-integration]]
- [[education.orange-business.data-engineering.course.unix-workbench.functions.basics]]