# MCP Server Index

## Purpose

Index all Model Context Protocol servers used by local and remote AI workflows.

## MCP Server May Expose

- Tools
- Resources
- Prompts

## MCP Risk Levels

### Low

Read-only documentation and schema lookup.

### Medium

Repo-limited writes and controlled issue/draft generation.

### High

Shell execution, Git mutation, file delete/move, credential access, remote server mutation, deployment.

## Required MCP Card Fields

- MCP ID
- Display name
- Transport
- Command
- Arguments
- Allowed clients
- Allowed paths
- Blocked paths
- Tools exposed
- Resources exposed
- Prompts exposed
- Risk level
- Permission gates
- Related repos
- Related docs
- Status
