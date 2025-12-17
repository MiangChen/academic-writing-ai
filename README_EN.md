# Academic Writing AI

English | **[中文](README.md)**

> 🎓 Open-source prompt templates for academic writing, designed to work with your local AI coding assistants.

## Why This Project?

Commercial AI writing tools lock you into their models and charge subscription fees. We believe academic writing assistance should be:

- **Free & Open Source** — No paywalls, no vendor lock-in
- **Bring Your Own Model (BYOM)** — Works with Claude Code, Codex CLI, Kiro, Cursor, or any AI assistant
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
| Nature | Narrative, accessible, story-driven | ✅ Ready |
| Science | Hook opening, broad impact | 🚧 WIP |
| IEEE Transactions | Technical, formal, structured | ✅ Ready |
| ACM | CS-focused, reproducibility emphasis | 🚧 WIP |
| Cell | Visual-first, mechanistic | 📋 Planned |
| PNAS | Significance statement style | 📋 Planned |

### By Writing Task
| Task | Description | Status |
|------|-------------|--------|
| Abstract | Structured vs. narrative abstracts | ✅ Ready |
| Introduction | Problem-gap-contribution flow | ✅ Ready |
| Related Work | Positioning & differentiation | 🚧 WIP |
| Methods | Reproducibility-focused | 📋 Planned |
| Rebuttal | Reviewer response strategies | 📋 Planned |

## Quick Start

### For Kiro Users
```bash
# In your paper project
mkdir -p .kiro/steering
cp academic-writing-ai/styles/ieee-transactions.md .kiro/steering/
```

### For Claude Code Users
```bash
cp academic-writing-ai/styles/nature-style.md .claude/CLAUDE.md
```

### For Cursor Users
```bash
cp academic-writing-ai/styles/nature-style.md .cursorrules
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute a New Style
1. Fork this repo
2. Create `styles/your-journal-style.md`
3. Include: voice/tone guidelines, structure templates, example phrases, common pitfalls
4. Submit a PR with a sample before/after

## Philosophy

> "As researchers who have struggled with the gap between having good ideas and expressing them in the 'right' style for each venue, we built this to democratize access to writing guidance that was previously only available through expensive tools or experienced mentors."

## Related Projects

- [academic-graph-ai](https://github.com/MiangChen/academic-graph-ai) — AI-assisted figure generation for papers

## License

MIT — Use freely, contribute back if you can.
