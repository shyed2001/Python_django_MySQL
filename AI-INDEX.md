# AI Index

## Purpose

This repo follows centralized AI governance.

- Universal and global AI instruction assets are managed in:
  - `F:\GitHubDesktop\GitHubCloneFiles\AI_Tools_Plan_Master_Index_Lib`
- This repo keeps only repo-specific AI context and pointer/cross-reference metadata.
- Fleet relationship data is generated from the git-root under `F:\GitHubDesktop\GitHubCloneFiles`.

## Source Of Truth

- Central repo: `F:\GitHubDesktop\GitHubCloneFiles\AI_Tools_Plan_Master_Index_Lib`
- Central branch: `main`
- Fleet root: `F:\GitHubDesktop\GitHubCloneFiles`

## Common AI Files (Fleet Baseline)

These files are the baseline common AI files seen across almost all repos.

1. `AGENTS.md`
2. `CLAUDE.md`
3. `GEMINI.md`
4. `.cursorrules`
5. `.windsurfrules`
6. `.clinerules`
7. `ANTIGRAVITY.md`

## This Repo Status

- Baseline common AI files are represented through central governance references.
- Cross-repo relationship data is defined in `AI-RELATIONS.json`.
- Related repo coverage below is full-fleet scope, not a manually curated subset.
- This file is generated for `Python_django_MySQL` from the configured fleet scan.

## Rollout Model

- Recommended default for cross-repo governance: pointer-file model.
- Optional local Windows optimization: junction or symlink for convenience only.
- Canonical update flow remains central-repo-first.
- Fleet rollout metadata should be regenerated from the fleet root scan when repos are added or removed.

## How To Regenerate

Run one of the following commands from the project root:

```powershell
uv run gitautofleet sync-ai-governance
uv run gitautofleet sync-ai-governance --all
uv run python scripts/generate_ai_governance_docs.py
uv run python scripts/generate_ai_governance_docs.py --all
```

Supporting manual and architecture references:

- Generator repo: `F:\GitHubDesktop\GitHubCloneFiles\GitAutoRepoFleet`
- `F:\GitHubDesktop\GitHubCloneFiles\GitAutoRepoFleet\docs\AI_GOVERNANCE_MANUAL.md`
- `F:\GitHubDesktop\GitHubCloneFiles\GitAutoRepoFleet\docs\AI_GOVERNANCE_SYSTEM_DESIGN.md`

## Related Repos

The following repos were discovered by scanning direct child git repos under `F:\GitHubDesktop\GitHubCloneFiles`.

1. `F:\GitHubDesktop\GitHubCloneFiles\.NET-Backend-Developer-Roadmap`
2. `F:\GitHubDesktop\GitHubCloneFiles\AbsolutePath__RelativePath`
3. `F:\GitHubDesktop\GitHubCloneFiles\adorshogeenbangla_dotNET_web_app`
4. `F:\GitHubDesktop\GitHubCloneFiles\AI_Tools_Plan_Master_Index_Lib` (hub)
5. `F:\GitHubDesktop\GitHubCloneFiles\Al-Bidaya-wan-Nihaya`
6. `F:\GitHubDesktop\GitHubCloneFiles\Algorithoms_and_Data_Structures`
7. `F:\GitHubDesktop\GitHubCloneFiles\Android`
8. `F:\GitHubDesktop\GitHubCloneFiles\androidHome`
9. `F:\GitHubDesktop\GitHubCloneFiles\ArchLinux`
10. `F:\GitHubDesktop\GitHubCloneFiles\AspNetCore-Developer-Roadmap`
11. `F:\GitHubDesktop\GitHubCloneFiles\AssemblyCode_asm_Programs`
12. `F:\GitHubDesktop\GitHubCloneFiles\Asset-Management-ERP-MBA`
13. `F:\GitHubDesktop\GitHubCloneFiles\books-Python-C-CPP-HTML-CSS-Js-PHP-Rust-AssemblyLanguage-`
14. `F:\GitHubDesktop\GitHubCloneFiles\Browser_Add_ons_Extensions_PlugIns`
15. `F:\GitHubDesktop\GitHubCloneFiles\C-Learning_ignored_and_discontinued`
16. `F:\GitHubDesktop\GitHubCloneFiles\C_Programming`
17. `F:\GitHubDesktop\GitHubCloneFiles\caveman`
18. `F:\GitHubDesktop\GitHubCloneFiles\cavemem`
19. `F:\GitHubDesktop\GitHubCloneFiles\CPlusPlusCPP_Programming`
20. `F:\GitHubDesktop\GitHubCloneFiles\CPP-Programming_AbdulBari`
21. `F:\GitHubDesktop\GitHubCloneFiles\CPP_AbdulBari`
22. `F:\GitHubDesktop\GitHubCloneFiles\CppBooks`
23. `F:\GitHubDesktop\GitHubCloneFiles\CppCoreGuidelines`
24. `F:\GitHubDesktop\GitHubCloneFiles\CS50GitPractice`
25. `F:\GitHubDesktop\GitHubCloneFiles\CS50W-Project0-Google-Search`
26. `F:\GitHubDesktop\GitHubCloneFiles\CyberSecurity_PenTesting_BugBounty`
27. `F:\GitHubDesktop\GitHubCloneFiles\Dart-Flutter`
28. `F:\GitHubDesktop\GitHubCloneFiles\Data_Mining_MCSE_642`
29. `F:\GitHubDesktop\GitHubCloneFiles\DBMS_Database_Management_System_CSI_223_MCSE`
30. `F:\GitHubDesktop\GitHubCloneFiles\digitalbd_org`
31. `F:\GitHubDesktop\GitHubCloneFiles\Docker---Kubernetes`
32. `F:\GitHubDesktop\GitHubCloneFiles\DomainsAndWebSiteHosting`
33. `F:\GitHubDesktop\GitHubCloneFiles\DSA_C_and_CPP_Data_Structures_and_Algorithms`
34. `F:\GitHubDesktop\GitHubCloneFiles\Electronic-Cheat-Sheet-and-Schematics-MegaCollection`
35. `F:\GitHubDesktop\GitHubCloneFiles\Evolutionary_Algorithm_MCSE662`
36. `F:\GitHubDesktop\GitHubCloneFiles\General-Study-Skills`
37. `F:\GitHubDesktop\GitHubCloneFiles\GitAutoRepoFleet` (spoke)
38. `F:\GitHubDesktop\GitHubCloneFiles\Hands-On-WebAssembly-for-C-Programmers`
39. `F:\GitHubDesktop\GitHubCloneFiles\Hard__Junction__Soft_Symbolic_SymLinks`
40. `F:\GitHubDesktop\GitHubCloneFiles\Help-Files`
41. `F:\GitHubDesktop\GitHubCloneFiles\HTML-and-html.txt-files`
42. `F:\GitHubDesktop\GitHubCloneFiles\JavaScript`
43. `F:\GitHubDesktop\GitHubCloneFiles\KLEHPT`
44. `F:\GitHubDesktop\GitHubCloneFiles\Library_Management_Dot_Net`
45. `F:\GitHubDesktop\GitHubCloneFiles\Markup_Languages`
46. `F:\GitHubDesktop\GitHubCloneFiles\mempalace`
47. `F:\GitHubDesktop\GitHubCloneFiles\MemPalace-dev`
48. `F:\GitHubDesktop\GitHubCloneFiles\modern-js-cheatsheet`
49. `F:\GitHubDesktop\GitHubCloneFiles\MongoDB`
50. `F:\GitHubDesktop\GitHubCloneFiles\MSc_CSE`
51. `F:\GitHubDesktop\GitHubCloneFiles\mSc_CSEOLD_FIlesOf`
52. `F:\GitHubDesktop\GitHubCloneFiles\My-md-website-cv`
53. `F:\GitHubDesktop\GitHubCloneFiles\MySQL_RDBMS`
54. `F:\GitHubDesktop\GitHubCloneFiles\Networking_IT_Comm_IE_IP`
55. `F:\GitHubDesktop\GitHubCloneFiles\Obsidian_Vault`
56. `F:\GitHubDesktop\GitHubCloneFiles\Office-Works`
57. `F:\GitHubDesktop\GitHubCloneFiles\Open_Source_Projects_Contributions`
58. `F:\GitHubDesktop\GitHubCloneFiles\Operating_System_CSI_313`
59. `F:\GitHubDesktop\GitHubCloneFiles\palaces-mempalace-mydev`
60. `F:\GitHubDesktop\GitHubCloneFiles\Palaces-mempalace-official`
61. `F:\GitHubDesktop\GitHubCloneFiles\PLC-VFD-SCADA`
62. `F:\GitHubDesktop\GitHubCloneFiles\Project-Material`
63. `F:\GitHubDesktop\GitHubCloneFiles\Python_django_MySQL`
64. `F:\GitHubDesktop\GitHubCloneFiles\Python_Programming`
65. `F:\GitHubDesktop\GitHubCloneFiles\Sadik-Education-Materials`
66. `F:\GitHubDesktop\GitHubCloneFiles\Scratch-online-programming-and-game-making`
67. `F:\GitHubDesktop\GitHubCloneFiles\Shared_businet`
68. `F:\GitHubDesktop\GitHubCloneFiles\Shared_public_html`
69. `F:\GitHubDesktop\GitHubCloneFiles\Shared_repo`
70. `F:\GitHubDesktop\GitHubCloneFiles\Shehrine_Education_Material`
71. `F:\GitHubDesktop\GitHubCloneFiles\shyed2001`
72. `F:\GitHubDesktop\GitHubCloneFiles\shyed2001.github.io`
73. `F:\GitHubDesktop\GitHubCloneFiles\Sirat_un_Nabi_by_Ibn_Hisham`
74. `F:\GitHubDesktop\GitHubCloneFiles\SQLite`
75. `F:\GitHubDesktop\GitHubCloneFiles\StructuredProgrammingCSI_121`
76. `F:\GitHubDesktop\GitHubCloneFiles\system-design-primer`
77. `F:\GitHubDesktop\GitHubCloneFiles\System_Security_Management_MCSE586`
78. `F:\GitHubDesktop\GitHubCloneFiles\Tafsir-Ibn-Kathir`
79. `F:\GitHubDesktop\GitHubCloneFiles\test`
80. `F:\GitHubDesktop\GitHubCloneFiles\Testing_SoftwareQualityAssuranceMCSE652`
81. `F:\GitHubDesktop\GitHubCloneFiles\UbuLinDexConMan`
82. `F:\GitHubDesktop\GitHubCloneFiles\Utsho`
83. `F:\GitHubDesktop\GitHubCloneFiles\VLOG-BLOG`
84. `F:\GitHubDesktop\GitHubCloneFiles\Web-Data-Text-Link-Extractor-Scripts-Broad-And-Searchable`
85. `F:\GitHubDesktop\GitHubCloneFiles\Webassembly`
86. `F:\GitHubDesktop\GitHubCloneFiles\WebComputingAndMining`
87. `F:\GitHubDesktop\GitHubCloneFiles\Windows-File-Explorer-Manager-Startup-Windows-Automation`

## Change Policy

- Global AI policy changes: make them in the central repo, then propagate references.
- Repo-specific AI behavior: keep it in each local repo.
- When the fleet membership changes, regenerate this file and `AI-RELATIONS.json` from the fleet root scan.
- Manual edits to the generated repo list are deprecated because they are prone to drift.
