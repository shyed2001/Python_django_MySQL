# Repository Registry Index

## Purpose

Track all local and remote repositories, their AI instruction files, package managers, MCP links, server links, Obsidian links, and risk levels.

## Registry Sources

- `registries/repos.local.json`
- `registries/repos.remote.json`
- `registries/repos.matrix.csv`

## Required Fields Per Repo

- repo_id
- repo_name
- local_path
- remote_url
- primary_branch
- repo_type
- protection_level
- package_manager
- instruction_files
- related_mcp_servers
- related_local_servers
- related_remote_servers
- related_obsidian_docs
- related_mempalace_palace
- related_mempalace_wing
- status
- last_indexed_at
- last_verified_at
