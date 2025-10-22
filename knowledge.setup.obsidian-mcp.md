---
id: knowledge.setup.obsidian-mcp
title: Obsidian MCP Server Setup
desc: "Setup and configuration guide"
updated: 1761144402000
created: 1761144402000
---


*Created: 2025-09-25*
*Tags: #setup #mcp #obsidian #vscode #github-copilot*

## Overview

Successfully configured the Obsidian MCP (Model Context Protocol) Server to work with VS Code and GitHub Copilot, enabling AI interaction with my Obsidian vault.

## Problem & Solution

### The Challenge
- Obsidian vault is located on Windows filesystem: `C:\repos\Obsidian\Orange Business Services\`
- VS Code runs in WSL (Windows Subsystem for Linux)
- MCP server has security restrictions:
  - ❌ No network mounts (`/mnt/c/...`)
  - ❌ No symbolic links pointing outside directories
  - ✅ Requires local filesystem paths only

### The Solution
Created a **sync-based approach** with rsync to keep Windows and WSL vaults synchronized.

## Technical Setup

### 1. VS Code Configuration
**File**: `~/.vscode-server/data/Machine/settings.json`

```json
{
    "plantuml.render": "Local",
    "plantuml.jar": "/home/lbrl0259/plantuml-1.2025.1.jar",
    "plantuml.exportOutDir": "",
    "github.copilot.chat.experimental.mcp.enabled": true,
    "github.copilot.chat.experimental.mcp.servers": {
        "obsidian": {
            "command": "obsidian-mcp",
            "args": ["/home/lbrl0259/obsidian-vault"]
        }
    }
}
```

### 2. MCP Server Installation
```bash
# Install globally
npm install -g obsidian-mcp

# Verify installation
obsidian-mcp --help
```

### 3. Vault Locations
- **Windows (Primary)**: `C:\repos\Obsidian\Orange Business Services\`
- **WSL (MCP Copy)**: `/home/lbrl0259/obsidian-vault/`

### 4. Sync Script
**File**: `~/sync-obsidian.sh`

**Usage**:
```bash
# Pull FROM Windows TO WSL (before using MCP)
~/sync-obsidian.sh pull

# Push FROM WSL TO Windows (after MCP changes)
~/sync-obsidian.sh push

# Check vault status
~/sync-obsidian.sh status
```

## Available MCP Tools

The Obsidian MCP server provides these tools for GitHub Copilot:

- `create-note` - Create new notes
- `read-note` - Read existing notes  
- `edit-note` - Edit notes
- `delete-note` - Delete notes
- `move-note` - Move notes to different locations
- `create-directory` - Create new directories
- `search-vault` - Search notes in the vault
- `add-tags` / `remove-tags` / `rename-tag` - Tag management
- `list-available-vaults` - List all available vaults

## Workflow

### Daily Usage
1. **Before using MCP**: `~/sync-obsidian.sh pull`
2. **Use GitHub Copilot Chat** to interact with vault
3. **After MCP session**: `~/sync-obsidian.sh push`
4. **Continue editing** in Windows Obsidian normally

### Example Copilot Queries
- *"List my available Obsidian vaults"*
- *"What notes do I have in my FLEXI folder?"*
- *"Search my vault for 'SQL'"*
- *"Create a new note called 'meeting-notes.md'"*
- *"Read the content of my SQL Crash Course notes"*

## Troubleshooting

### Common Issues
1. **MCP server not showing in Copilot**
   - Restart VS Code after configuration changes
   - Check settings.json syntax

2. **Permission errors**
   - Ensure vault path is readable/writable
   - Run sync script to refresh permissions

3. **Sync conflicts**
   - Always pull before using MCP
   - Push changes back to Windows after MCP modifications

### Verification Commands
```bash
# Test MCP server
timeout 5 obsidian-mcp "/home/lbrl0259/obsidian-vault"

# Check vault sync status
~/sync-obsidian.sh status

# Verify VS Code settings
cat ~/.vscode-server/data/Machine/settings.json | grep -A5 "mcp"
```

## System Requirements

- ✅ Node.js 20+ (have v22.15.0)
- ✅ VS Code with GitHub Copilot
- ✅ WSL environment
- ✅ rsync for synchronization

## Security Notes

- MCP server has read/write access to vault
- Always backup vault before major changes
- Sync script maintains data integrity between Windows/WSL
- Use `~/sync-obsidian.sh status` to monitor file counts

## Next Steps

- [ ] Consider automating sync with file watchers
- [ ] Add conflict resolution to sync script
- [ ] Test all MCP tools with GitHub Copilot
- [ ] Document specific use cases and workflows

---

*This setup enables seamless AI interaction with my Obsidian knowledge base while maintaining the familiar Windows Obsidian editing experience.*