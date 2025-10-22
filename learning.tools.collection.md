---
id: learning.tools.collection
title: Development Tools Collection
desc: "Development tool documentation"
updated: 1761144402000
created: 1761144402000
---


## Overview

Personal collection of development and documentation tools for markdown processing, format conversion, and document generation.

## Tools Inventory

### [[learning.tools.Markdown to Confluence Converter]] 
Java-based tool for converting Markdown documents to Confluence wiki markup

### [[learning.tools.Markdown to PDF Converter]]
Python-based tool using Pandoc for generating professional PDF documents from Markdown

### [[learning.tools.Mermaid Diagram Filter]]
Pandoc filter for rendering Mermaid diagrams in document conversions

## Quick Access

| Tool | Language | Primary Use | Input | Output |
|------|----------|-------------|-------|---------|
| Markdown to Confluence | Java | Wiki conversion | `.md` | `.confluence` |
| Markdown to PDF | Python | Document generation | `.md` | `.pdf` |
| Mermaid Filter | Python | Diagram rendering | Mermaid code | PNG images |

## Installation Requirements

### System Dependencies
- Java JDK (OpenJDK or Oracle)
- Python 3.x
- Pandoc
- XeLaTeX (for PDF generation)
- Mermaid CLI (`mmdc`)

### Python Dependencies
- `panflute` - Pandoc filter framework

## Usage Patterns

### Document Publishing Workflow
1. **Draft** - Write content in Markdown
2. **Convert** - Use appropriate converter for target format
3. **Review** - Check output formatting and quality
4. **Publish** - Deploy to target platform (Confluence/PDF distribution)

### Diagram Integration
1. **Create** - Embed Mermaid diagrams in Markdown
2. **Process** - Run through Mermaid filter during conversion
3. **Render** - Generate PNG images automatically
4. **Include** - Embed rendered diagrams in final output

## Maintenance Notes

- All tools are self-contained in `/tools/markdown-to-confluence/` directory
- Java class files require compilation before use
- Python scripts use system Python installation
- Pandoc filters use standard panflute framework

## Related Documentation

- [[learning.tools.Custom LaTeX Templates]] - PDF formatting customization
- [[learning.tools.Pandoc Filters Guide]] - Advanced document processing
- [[learning.tools.Confluence Publishing Workflow]] - Wiki deployment procedures

---
*Personal development tools for document processing and conversion*