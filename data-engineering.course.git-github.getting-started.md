# Getting Started with Git

Git is a distributed version control system that tracks changes in files and coordinates work between multiple people.

## Initial Setup

Check your Git version:

```bash
git --version
```

Configure your identity:

```bash
git config --global user.name "myUserName"
git config --global user.email myName@email.com
```

## Step 1: Create Your First Git Repository

First, create a directory where your Git repository will live:

```bash
mkdir my_repo
cd my_repo
```

"Repo" is short for "repository." To start tracking files with Git in a directory, run:

```bash
git init
```

You've now initialized your first Git repository!

## Step 2: Create and Track a File

Create a file in the Git repository:

```bash
touch readme.txt
```

Check the status of your repository:

```bash
git status
```

Git will show `readme.txt` as an **untracked file**. To start tracking it:

```bash
git add readme.txt
```

Check the status again:

```bash
git status
```

Git is now tracking `readme.txt` — it's **staged**. To unstage it:

```bash
git rm --cached readme.txt
```

The file is now back to being **untracked**. Let's track it again:

```bash
git add readme.txt
```

## Step 3: Commit Your Changes

Now that `readme.txt` is staged, create a **commit** to save the current state:

```bash
git commit -m "Add readme.txt"
```

This creates a milestone that records the creation of `readme.txt`.

Check the status again:

```bash
git status
```

All changes have been committed.

## Step 4: Add More Files and Make Changes

Add two new files:

```bash
touch file1.txt fil2.txt
```

Add a new line to `readme.txt`:

```bash
echo "New line of text" >> readme.txt
```

Check the status:

```bash
git status
```

Git shows:
- `readme.txt` is **modified**
- `file1.txt` and `fil2.txt` are **untracked**

You can stage changes in multiple ways:

- Individually:

  ```bash
  git add readme.txt
  git add file1.txt
  git add fil2.txt
  ```

- All `.txt` files:

  ```bash
  git add *.txt
  ```

- Everything (recommended):

  ```bash
  git add -A
  ```

## Step 5: Commit the Changes

```bash
git commit -m "Add two files and update readme"
```

Oops! There's a typo: `fil2.txt` should be `file2.txt`.

Undo the last commit (but keep changes staged):

```bash
git reset --soft HEAD~
```

Rename the file:

```bash
mv fil2.txt file2.txt
```

Check the status again:

```bash
git status
```

Git recognizes `fil2.txt` as deleted. Bring everything back up to date:

```bash
git add -A
```

## Step 6: Final Commit

```bash
git commit -m "Fix filename typo and commit all changes"
```

Success! Everything is clean and correct.

## Summary

- Git tracks changes to plain text files (code, documentation, etc.)
- A directory with Git tracking is called a **repository**
- Use `git init` to initialize a Git repo
- Use `git add [file]` to stage changes
- Use `git commit -m "message"` to save changes
- Use `git status` frequently to inspect the state of your repository

## Related Topics

- [[data-engineering.course.git-github.help-logs-diffs]]
- [[data-engineering.course.git-github.branching]]
- [[data-engineering.course.git-github.commands]]