#!/usr/bin/env python3
"""
Migrate IU Data Science and IAU Intelligent Analysis courses to Dendron format.
Converts markdown files with proper image path corrections.
"""

import os
import re
import shutil
from pathlib import Path

# Source and target directories
IU_SOURCE = "/mnt/c/repos/iu-data-science-DLMBDSA01/data-science"
IAU_SOURCE = "/mnt/c/repos/stu-iau_b-intelligent-data-analysis/DataAnalasys"
DENDRON_ROOT = "/home/lbrl0259/Dendron/notes"


def slugify(text):
    """Convert text to Dendron-friendly slug"""
    # Remove special characters and convert to lowercase
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text


def convert_iu_image_path(match):
    """Convert IU image paths to Dendron format"""
    full_match = match.group(0)
    alt_text = match.group(1) if match.group(1) else "Image"
    filename = match.group(2)

    # Extract just the filename without path
    img_name = os.path.basename(filename)

    # New Dendron path
    new_path = f"assets/images/data-science/iu-dlmbdsa01/{img_name}"

    return f"![{alt_text}]({new_path})"


def convert_iau_image_path(match, module_name):
    """Convert IAU image paths to Dendron format"""
    full_match = match.group(0)
    alt_text = match.group(1) if match.group(1) else "Slide"
    filename = match.group(2)

    # Extract just the filename
    img_name = os.path.basename(filename)

    # New Dendron path with module subdirectory
    new_path = f"assets/images/data-science/iau-intelligent-analysis/{module_name}/{img_name}"

    return f"![{alt_text}]({new_path})"


def migrate_iu_course():
    """Migrate IU Data Science course content"""
    print("\\n=== Migrating IU Data Science Course ===\\n")

    # Module mapping: directory name -> Dendron hierarchy
    module_map = {
        "1.-introduction-to-data-science": "introduction",
        "2.-use-cases-and-performance-evaluation": "use-cases-evaluation",
        "3.-data-pre-processing": "data-preprocessing",
        "4.-processing-of-data": "data-processing",
        "5.-selected-mathematical-techniques": "mathematical-techniques",
        "6.-selected-artificial-intelligence-techniques": "ai-techniques",
        "7.-exam-examples": "exam-prep"
    }

    files_migrated = 0

    for module_dir, dendron_name in module_map.items():
        source_dir = os.path.join(IU_SOURCE, module_dir)
        if not os.path.exists(source_dir):
            print(f"  ⚠  Skipping {module_dir} (not found)")
            continue

        print(f"  📁 Processing {module_dir}...")

        # Process markdown files in this module
        for md_file in Path(source_dir).glob("*.md"):
            content = md_file.read_text(encoding='utf-8', errors='ignore')

            # Fix image paths
            content = re.sub(
                r'!\[(.*?)\]\((.*?\.png)\)',
                convert_iu_image_path,
                content
            )

            # Create Dendron filename
            file_slug = slugify(md_file.stem)
            dendron_filename = f"data-science.iu-dlmbdsa01.{dendron_name}.{file_slug}.md"
            target_path = os.path.join(DENDRON_ROOT, dendron_filename)

            # Add navigation footer
            content += f"\\n\\n---\\n\\n## Navigation\\n\\n"
            content += f"- **Parent**: [[data-science.iu-dlmbdsa01.{dendron_name}]]\\n"
            content += f"- **Course**: [[data-science.iu-dlmbdsa01]]\\n"

            # Write to Dendron
            Path(target_path).write_text(content, encoding='utf-8')
            files_migrated += 1
            print(f"    ✓ {dendron_filename}")

    print(f"\\n  ✅ Migrated {files_migrated} IU files\\n")
    return files_migrated


def migrate_iau_course():
    """Migrate IAU Intelligent Analysis course content"""
    print("\\n=== Migrating IAU Intelligent Analysis Course ===\\n")

    files_migrated = 0

    # Get all IAU lecture markdown files
    for md_file in Path(IAU_SOURCE).glob("IAU-*.md"):
        if md_file.stat().st_size < 100:  # Skip tiny placeholder files
            continue

        print(f"  📄 Processing {md_file.name}...")

        content = md_file.read_text(encoding='utf-8', errors='ignore')

        # Determine module name for image paths
        module_name = md_file.stem

        # Fix image paths with module-specific directory
        content = re.sub(
            r'!\[(.*?)\]\((.*?\.png)\)',
            lambda m: convert_iau_image_path(m, module_name),
            content
        )

        # Create Dendron filename
        file_slug = slugify(md_file.stem.replace('IAU-', ''))
        dendron_filename = f"data-science.iau-intelligent-analysis.lectures.{file_slug}.md"
        target_path = os.path.join(DENDRON_ROOT, dendron_filename)

        # Enhance content with header and navigation
        header = f"# {md_file.stem.replace('IAU-', 'Lecture ').replace('-', ' ')}\\n\\n"

        content = header + content
        content += f"\\n\\n---\\n\\n## Navigation\\n\\n"
        content += f"- **Parent**: [[data-science.iau-intelligent-analysis.lectures]]\\n"
        content += f"- **Course**: [[data-science.iau-intelligent-analysis]]\\n"

        # Write to Dendron
        Path(target_path).write_text(content, encoding='utf-8')
        files_migrated += 1
        print(f"    ✓ {dendron_filename}")

    print(f"\\n  ✅ Migrated {files_migrated} IAU lecture files\\n")
    return files_migrated


def main():
    """Main migration function"""
    print("\\n" + "="*60)
    print(" Data Science Courses Migration to Dendron")
    print("="*60)

    iu_count = migrate_iu_course()
    iau_count = migrate_iau_course()

    print("\\n" + "="*60)
    print(f" Migration Complete!")
    print(f" - IU files: {iu_count}")
    print(f" - IAU files: {iau_count}")
    print(f" - Total: {iu_count + iau_count}")
    print("="*60 + "\\n")


if __name__ == "__main__":
    main()
