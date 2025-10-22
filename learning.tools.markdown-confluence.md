---
id: learning.tools.markdown-confluence
title: Markdown to Confluence Converter
desc: "Development tool documentation"
updated: 1761144402000
created: 1761144402000
---


## Overview

Java-based tool that converts Markdown documents to Confluence wiki markup format for seamless integration with Atlassian Confluence.

## Features

### Supported Conversions

- **Headings**: `#` to `h1.`, `##` to `h2.`, etc.
- **Emphasis**: 
  - `*italic*` → `_italic_`
  - `**bold**` → `*bold*`
  - `***bold-italic***` → `_*bold-italic*_`
- **Code Blocks**: Fenced code blocks to Confluence code macros
- **Inline Code**: Backticks to `{{code}}`
- **Lists**: Bullet points with proper indentation
- **Horizontal Rules**: `---` to `----`

### Code Block Features

- **Language Detection**: Automatic language specification
- **Line Numbers**: Enabled by default
- **Syntax Highlighting**: Confluence theme applied
- **Collapsible**: Optional collapse functionality

## Installation

### Prerequisites

```bash
# Install Java JDK
sudo apt update
sudo apt install default-jdk
```

### Compilation

```bash
# Navigate to project directory
cd /home/lbrl0259/repo/MyWorkSpace_ASBO/tools/markdown-to-confluence

# Compile Java source
javac -d . MarkdownToConfluence.java
```

## Usage

### Basic Command

```bash
java MarkdownToConfluence <input.md> <output.confluence>
```

### Examples

```bash
# Convert single document
java MarkdownToConfluence input.md output.confluence

# Convert with specific paths
java MarkdownToConfluence /path/to/document.md /path/to/output.confluence
```

## Conversion Details

### Code Block Transformation

**Markdown Input:**
````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

**Confluence Output:**
```
{code:collapse=false|language=python|linenumbers=true|theme=Confluence}
def hello_world():
    print("Hello, World!")
{code}
```

### Emphasis Conversion Order

1. Single asterisks to underscores (italic)
2. Triple asterisks to bold-italic combination
3. Double asterisks to single asterisks (bold)

### List Processing

**Markdown:**
```markdown
- Item 1
  - Nested item
* Item 2
```

**Confluence:**
```
* Item 1
** Nested item
* Item 2
```

## Technical Implementation

### Core Components

- **Pattern Matching**: Regular expressions for Markdown syntax detection
- **Sequential Processing**: Order-dependent conversion to avoid conflicts
- **File I/O**: UTF-8 encoding support for international characters
- **Error Handling**: Command-line argument validation

### Processing Pipeline

1. **Input Validation**: Check command-line arguments
2. **File Reading**: Load Markdown source with UTF-8 encoding
3. **Code Block Protection**: Process fenced code blocks first
4. **Inline Code Protection**: Handle inline code elements
5. **Text Transformation**: Apply heading, emphasis, and list conversions
6. **Output Generation**: Write Confluence markup to file

## Limitations

### Not Supported
- Tables (requires manual conversion)
- Images (paths may need adjustment)
- Links (some formats may not convert)
- Complex nested structures
- Confluence-specific macros in input

### Known Issues
- Nested emphasis combinations may need manual review
- Code block languages not recognized by Confluence will default to 'text'
- Complex list indentation patterns may require adjustment

## Integration Patterns

### Wiki Publishing Workflow
1. **Author** content in Markdown for version control
2. **Convert** to Confluence format using this tool
3. **Review** converted markup for formatting accuracy  
4. **Paste** into Confluence editor
5. **Publish** with final formatting adjustments

### Batch Processing
```bash
# Process multiple files
for file in *.md; do
    java MarkdownToConfluence "$file" "${file%.md}.confluence"
done
```

## Troubleshooting

### Compilation Issues
- Ensure Java JDK is properly installed
- Verify classpath includes current directory
- Check file permissions for source and output directories

### Runtime Errors
- Validate input file exists and is readable
- Ensure output directory has write permissions
- Check file encoding if special characters appear corrupted

### Conversion Quality
- Review emphasis conversion for nested formatting
- Test code blocks with various programming languages
- Validate list indentation in Confluence preview

## File Locations

```
tools/markdown-to-confluence/
├── MarkdownToConfluence.java    # Main converter source
├── MarkdownToConfluence.class   # Compiled Java class
├── readme.md                    # Setup instructions
├── input.md                     # Sample input file
├── output.confluence            # Sample output file
└── test.confluence              # Test conversion results
```

## Related Tools

- [[learning.tools.Markdown to PDF Converter]] - PDF generation from same Markdown source
- [[learning.tools.Development Tools Collection]] - Complete tools overview
- [[learning.tools.Confluence Publishing Workflow]] - Wiki deployment procedures

---
*Java-based Markdown to Confluence conversion tool*