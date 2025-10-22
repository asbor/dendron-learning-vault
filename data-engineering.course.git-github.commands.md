# Git Commands Reference

A quick, clear guide to the most useful Git CLI actions. Use the examples exactly as shown or adapt the placeholders (`<…>`, `branch-name`, etc.) to your project.

## Basic Commands

### `git add`

Stages edits so they can be committed.

```bash
git add <file>   # stage one file
git add .        # stage everything in the current dir
git add -A       # stage all changes in the repo
```

### `git reset`

Undo local changes.

```bash
git reset                # unstage files, keep edits
git reset --hard HEAD    # discard all uncommitted edits
```

### `git branch`

List, create, or delete branches.

```bash
git branch                # list branches
git branch <new-branch>   # create
git branch -d <branch>    # delete (safe)
```

### `git checkout`

Switch branches (example shows `main`).

```bash
git checkout main
```

## Remote Operations

### `git clone`

Copy a remote repo locally.

```bash
git clone <repo-url>
```

### `git pull`

Fetch **and** merge remote changes into the current branch.

```bash
git pull origin main
```

### `git push`

Send local commits to a remote repo.

```bash
git push origin <branch>
```

## Information Commands

### `git version`

Show the Git release installed.

```bash
git version
```

### `git diff`

Compare snapshots or branches.

```bash
git diff                    # working dir ↔ last commit
git diff HEAD~1 HEAD        # last ↔ previous commit
git diff <branch1> <branch2>
```

## Advanced Operations

### `git revert`

Create a new commit that undoes a previous one.

```bash
git revert HEAD            # revert most recent commit
```

### Global identity (one-time setup)

```bash
git config --global user.name  "<Your Name>"
git config --global user.email "<email@example.com>"
```

### Remote management

```bash
git remote           # list remotes
git remote -v        # list with URLs
git remote add origin <url>        # add
git remote rename origin upstream  # rename
git remote rm <name>               # remove
```

## Advanced Workflows

### Email-style patch workflow

```bash
git format-patch HEAD~3                 # make 3 patches
git request-pull origin/main <branch>   # summary for email
git send-email *.patch                  # email the patches
git am <patchfile.patch>                # apply a patch
```

### Miscellaneous power tools

| Command | Purpose | Example |
|---------|---------|---------|
| `git daemon`   | Serve repos over the lightweight `git://` protocol | `git daemon --base-path=/path/to/repos` |
| `git instaweb` | One-click local web viewer | `git instaweb --httpd=webrick` |
| `git rerere`   | Auto-reuse recorded conflict resolutions | `git rerere` |

## Conclusion

Master these commands and you'll handle the vast majority of day-to-day version-control tasks with confidence.

## Related Topics

- [[data-engineering.course.git-github.getting-started]]
- [[data-engineering.course.git-github.branching]]
- [[data-engineering.course.git-github.cheat-sheet]]