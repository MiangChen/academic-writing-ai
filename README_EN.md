# Academic Writing AI

English | **[中文](README.md)**

> 🎓 Open-source prompt templates for academic writing, designed to work with your local AI coding assistants.

## Why This Project?

Commercial AI writing tools lock you into their models and charge subscription fees. We believe academic writing assistance should be:

- **Free & Open Source** — No paywalls, no vendor lock-in
- **Use Any Model** — Works with Claude Code, Codex CLI, Kiro, Cursor, or any AI assistant
- **Community-Driven** — Everyone can contribute prompts for different journals and writing styles

## How It Works

These prompts are designed as **steering files** or **system prompts** for local AI coding assistants:

```
your-paper-project/
├── .kiro/steering/          # For Kiro users
│   └── nature-style.md      # Copy from this repo
├── .claude/                 # For Claude Code users  
│   └── CLAUDE.md
├── main.tex
└── ...
```

Simply copy the relevant style guide into your project, and your AI assistant will write in that journal's style.

## Supported Styles

### By Journal Family
| Journal | Style | Status |
|---------|-------|--------|
| IEEE Transactions | Technical, formal, structured | ✅ Ready |

### By Writing Task
| Task | Description | Status |
|------|-------------|--------|
| Abstract | Structured vs. narrative abstracts | ✅ Ready |
| Introduction | Problem-gap-contribution flow | ✅ Ready |
| Related Work | Positioning & differentiation | 🚧 WIP |
| Methods | Reproducibility-focused | 📋 Planned |
| Rebuttal | Reviewer response strategies | 📋 Planned |

## Quick Start

### Option 1: Copy Prompts to Your AI Assistant

#### For Kiro Users
```bash
mkdir -p .kiro/steering
cp academic-writing-ai/styles/ieee-transactions.md .kiro/steering/
```

#### For Claude Code Users
```bash
cp academic-writing-ai/styles/ieee-transactions.md .claude/CLAUDE.md
```

#### For Cursor Users
```bash
cp academic-writing-ai/styles/ieee-transactions.md .cursorrules
```

### Option 2: Use LangGraph Workflow (Interactive)

We provide an interactive writing workflow based on LangGraph, supporting write-review-revise loops:

```bash
# 1. Setup environment
bash setup.sh

# 2. Configure API Key
cp config_llm_example.json config_llm.json
# Edit config_llm.json with your API Key

# 3. Start workflow
bash start.sh
```

Workflow features:
- 🎯 Select journal style and section type
- ✍️ Input research points, auto-generate draft
- 🔄 Human-in-the-loop review with iterative refinement
- 💾 Auto-save to `output/` directory

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Write     │ -> │   Review    │ -> │  Finalize   │
│  Generate   │    │  Human      │    │  Output     │
└─────────────┘    └──────┬──────┘    └─────────────┘
                         │ feedback
                         ↓
                   ┌─────────────┐
                   │   Revise    │
                   │  Refine     │
                   └─────────────┘
```

## Contributing

1. Fork this repo
2. Create `styles/your-journal-style.md`
3. Include: voice/tone guidelines, structure templates, example phrases, common pitfalls
4. Submit a PR with a sample before/after

## Related Projects

- [academic-diagram-ai](https://github.com/MiangChen/academic-diagram-ai) — AI-assisted figure generation for papers
