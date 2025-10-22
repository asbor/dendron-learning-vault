# Makefile Automation

Demonstrates how to use Make to automate documentation generation and project management tasks.

## Makefile Overview

The project uses a sophisticated Makefile that automatically generates documentation with dynamic content:

```makefile
all: clean generate

clean:
	rm -f README.md index.md

generate:
	echo "---" > README.md
	echo "title: Guessing Game Project" >> README.md
	echo "date: $$(date '+%Y-%m-%d %H:%M:%S')" >> README.md
	echo "version: 1.0.0" >> README.md
	echo "author: Your Name" >> README.md
	echo "license: MIT" >> README.md
	echo "---" >> README.md
	echo "" >> README.md
	echo "# Guessing Game Project" >> README.md
	echo "" >> README.md
	echo "This project is a simple guessing game written in Bash." >> README.md
	echo "" >> README.md
	echo "## Generated Info" >> README.md
	echo "" >> README.md
	echo "**Generated at:** $$(date '+%Y-%m-%d %H:%M:%S')" >> README.md
	echo "**Lines of code in guessinggame.sh:** $$(wc -l < guessinggame.sh)" >> README.md
	echo "" >> README.md
	echo "## GitHub URLs" >> README.md
	echo "" >> README.md
	echo "- [GitHub Repository](https://github.com/asbor/Guessing-Game-Project)" >> README.md
	echo "- [GitHub Pages](https://asbor.github.io/Guessing-Game-Project)" >> README.md
	echo "" >> README.md
	echo "## Clarification for GitHub Pages Deployment" >> README.md
	echo "" >> README.md
	echo "The assignment instructions require the GitHub Pages site to be generated from the README.md file, but GitHub Pages does not render README.md directly." >> README.md
	echo "To satisfy this, an additional file called \`index.md\` was created as a copy of the generated README.md. This allows GitHub Pages to render the content properly." >> README.md
	echo "" >> README.md
	echo "This clarification ensures that the Pages site functions correctly while remaining faithful to the assignment's intent." >> README.md
	cp README.md index.md
```

## Key Automation Features

### Dynamic Content Generation

The Makefile includes several dynamic elements:

1. **Timestamps**: `$$(date '+%Y-%m-%d %H:%M:%S')` generates current date/time
2. **Line counting**: `$$(wc -l < guessinggame.sh)` counts script lines
3. **YAML frontmatter**: Includes metadata for GitHub Pages

### Build Targets

- **`all`**: Default target that runs clean and generate
- **`clean`**: Removes generated files for a fresh start
- **`generate`**: Creates both README.md and index.md files

### GitHub Pages Integration

The Makefile addresses a common deployment challenge:

- GitHub Pages expects `index.md` for rendering
- Project requirements specify `README.md` generation
- Solution: Generate README.md and copy to index.md

## Advanced Make Concepts

### Variable Expansion

Using `$$` to escape shell variables in Make:

```makefile
echo "**Generated at:** $$(date '+%Y-%m-%d %H:%M:%S')" >> README.md
```

### Command Chaining

Multiple echo commands build the documentation incrementally:

- Enables complex document structure
- Allows for conditional content inclusion
- Maintains readability of the Makefile

### File Dependencies

While this example uses simple targets, it demonstrates:

- How Make can manage file generation
- Coordination between multiple output files
- Clean/rebuild workflows

## Practical Applications

This automation pattern is valuable for:

- **Documentation**: Keeping README files current with project stats
- **Reporting**: Generating reports with current data
- **Deployment**: Preparing files for different platforms
- **CI/CD**: Automating build processes in pipelines

## Learning Outcomes

Students learn to:

1. Create complex Makefiles with multiple targets
2. Generate documentation programmatically
3. Handle platform-specific requirements (GitHub Pages)
4. Use shell commands within Make recipes
5. Implement clean/build workflows

## Related Topics

- [[education.orange-business.data-engineering.course.unix-workbench.make.basics]]
- [[education.orange-business.data-engineering.course.bash-integration.workflows.guessing-game]]
- [[education.orange-business.data-engineering.course.bash-integration.workflows.git-integration]]