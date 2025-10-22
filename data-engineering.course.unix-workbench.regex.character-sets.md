# Character Sets

A character set is a group of characters enclosed in square brackets `[]`. It matches any one of the characters inside the brackets. For example, the regular expression `[abc]` matches any string that contains either the character `a`, the character `b`, or the character `c`.

```bash
touch small.txt
echo "abcdefghijklmnopqrstuvwxyz" >> small.txt
echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" >> small.txt
echo "0123456789" >> small.txt
echo "aa bb cc" >> small.txt
echo "rhythms" >> small.txt
echo "xyz" >> small.txt
echo "abc" >> small.txt
echo "tragedy + time = humor" >> small.txt
echo "http://www.jhsph.edu/" >> small.txt
echo "#%&-=***=-&%#" >> small.txt
```

## Examples

### General rules

- `.` matches any character except a newline.
- `\d` matches any digit character.
- `\D` matches any non-digit character.
- `\w` matches any word character.
- `\W` matches any non-word character.
- `\s` matches any whitespace character.
- `\S` matches any non-whitespace character.

Other characters can be matched by using their escape sequence. For example,

- New line character: `\n`
- Tab character: `\t`
- Carriage return: `\r` - *return the cursor to the beginning of the line*
- Form feed: `\f` - *advance the cursor to the next page*
- Backspace: `\b` - *move the cursor one character to the left*
- Null character: `\0` - *null character*
- Vertical tab: `\v` - *move the cursor to the next line*
- Escape: `\e` - *escape character*
- Alert: `\a` - *alert character*
- Control character: `\c` - *control character*

### Example 1: Basic Character Set

The regular expression `[abc]` matches any string that contains either the character `a`, the character `b`, or the character `c`.

```bash
grep -E '[abc]' small.txt
```

Output:

![Character set [abc] example](assets/images/unix-workbench/image.png)

### Example 2: Lowercase Range

The regular expression `[a-z]` matches any string that contains a lowercase letter.

```bash
grep -E '[a-z]' small.txt
```

Output:

![Lowercase range [a-z] example](assets/images/unix-workbench/image-1.png)

### Example 3: Uppercase Range

The regular expression `[A-Z]` matches any string that contains an uppercase letter.

```bash
grep -E '[A-Z]' small.txt
```

Output:

![Uppercase range [A-Z] example](assets/images/unix-workbench/image-2.png)

### Example 4: Alphanumeric

The regular expression `[a-zA-Z0-9]` matches any string that contains letters or digits.

```bash
grep -E '[a-zA-Z0-9]' small.txt
```

Output:

![Alphanumeric range [a-zA-Z0-9] example](assets/images/unix-workbench/image-3.png)

## Summary

Character sets are a powerful feature of regular expressions that allow you to match specific groups of characters. They provide flexibility in defining what characters you want to match in your patterns.

## Related Topics

- [[data-engineering.course.unix-workbench.regex.metacharacters]]
- [[data-engineering.course.unix-workbench.regex.escaping]]
- [[data-engineering.course.unix-workbench.bash-fundamentals.find]]