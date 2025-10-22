# Metacharacters

Metacharacters are characters that have a special meaning in regular expressions. They are used to define the search criteria. Here are some of the most common metacharacters:

```bash
. ^ $ * + ? { } [ ] \ | ( )
```

## The pipe (|) - Alternation Operator (OR)

The pipe metacharacter is used to match one of two or more expressions. For example, the regular expression `a|b` matches any string that contains either the character `a` or the character `b`.

## The dot (.) - Wildcard Character (Any Character)

The dot metacharacter matches any character except a newline character. For example, the regular expression `a.b` matches any three-character string that starts with `a`, ends with `b`, and has any character in between.

```bash
$ echo "abc" | grep 'a.b'
abc
```

## The caret (^) - Anchor (Start of Line)

The caret metacharacter matches the start of a line. For example, the regular expression `^a` matches any line that starts with the character `a`.

```bash
$ echo "abc" | grep '^a'
abc
```

## The dollar sign ($) - Anchor (End of Line)

The dollar sign metacharacter matches the end of a line. For example, the regular expression `b$` matches any line that ends with the character `b`.

```bash
$ echo "abc" | grep 'b$'
abc
```

## The asterisk (*) - Quantifier (Zero or More)

The asterisk metacharacter matches zero or more occurrences of the preceding character. For example, the regular expression `ab*c` matches any string that starts with `a`, ends with `c`, and has zero or more occurrences of the character `b` in between.

```bash
$ echo "ac" | grep 'ab*c'
ac
```

## The plus (+) - Quantifier (One or More)

The plus metacharacter matches one or more occurrences of the preceding character. For example, the regular expression `ab+c` matches any string that starts with `a`, ends with `c`, and has one or more occurrences of the character `b` in between.

```bash
$ echo "abc" | grep 'ab+c'
abc
```

## The question mark (?) - Quantifier (Zero or One)

The question mark metacharacter matches zero or one occurrence of the preceding character. For example, the regular expression `ab?c` matches any string that starts with `a`, ends with `c`, and has zero or one occurrence of the character `b` in between.

```bash
$ echo "ac" | grep 'ab?c'
ac
```

## The curly braces ({}) - Quantifier (Exact Number)

The curly braces metacharacters are used to specify the exact number of occurrences of the preceding character. For example, the regular expression `ab{2}c` matches any string that starts with `a`, ends with `c`, and has exactly two occurrences of the character `b` in between.

```bash
$ echo "abbc" | grep 'ab{2}c'
abbc
```

## The square brackets ([]) - Character Class

The square brackets metacharacters are used to define a character class. A character class matches any one of the characters inside the brackets. For example, the regular expression `[abc]` matches any string that contains either the character `a`, the character `b`, or the character `c`.

```bash
$ echo "abc" | grep '[abc]'
abc
```

## The backslash (\) - Escape Character

The backslash metacharacter is used to escape a metacharacter or a special character. For example, the regular expression `a\*b` matches the string `a*b` instead of any string that starts with `a` and ends with `b`.

```bash
$ echo "a*b" | grep 'a\*b'
a*b
```

## The parentheses (()) - Grouping

The parentheses metacharacters are used to group expressions. For example, the regular expression `(ab)+` matches any string that contains one or more occurrences of the string `ab`.

```bash
$ echo "abab" | grep '(ab)+'
abab
```

## Summary

In this section, we learned about the most common metacharacters used in regular expressions. We also saw how to use them to define the search criteria. In the next section, we will learn about character sets and escaping in regular expressions.

## Related Topics

- [[data-engineering.course.unix-workbench.regex.character-sets]]
- [[data-engineering.course.unix-workbench.regex.escaping]]
- [[data-engineering.course.unix-workbench.bash-fundamentals.find]]