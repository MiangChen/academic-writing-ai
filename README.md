# Academic Writing AI

**[English](README_EN.md)** | 中文

> 🎓 开源的学术写作 Prompt 模板库，专为本地 AI 编程助手设计。

## 为什么做这个项目？

市面上的 AI 写作工具都绑定自家模型，还要收订阅费。我们认为学术写作辅助应该是：

- **免费开源** — 没有付费墙，没有厂商锁定
- **自带模型（BYOM）** — 兼容 Claude Code、Codex CLI、Kiro、Cursor 等任何 AI 助手
- **社区驱动** — 所有人都可以贡献不同期刊和写作风格的 Prompt

## 工作原理

这些 Prompt 被设计为本地 AI 编程助手的 **steering files** 或 **system prompts**：

```
your-paper-project/
├── .kiro/steering/          # Kiro 用户
│   └── nature-style.md      # 从本仓库复制
├── .claude/                 # Claude Code 用户
│   └── CLAUDE.md
├── main.tex
└── ...
```

只需将对应的风格指南复制到你的项目中，AI 助手就会按照该期刊的风格来写作。

## 支持的风格

### 按期刊分类
| 期刊 | 风格特点 | 状态 |
|------|----------|------|
| Nature | 叙事性、易读、故事驱动 | ✅ 可用 |
| Science | 钩子开头、强调广泛影响 | 🚧 开发中 |
| IEEE Transactions | 技术性、正式、结构化 | ✅ 可用 |
| ACM | 计算机领域、强调可复现性 | � 开发中 |
| Cell | 视觉优先、机制导向 | 📋 计划中 |
| 中文核心期刊 | 八股文结构、规范表达 | 📋 计划中 |

### 按写作任务分类
| 任务 | 描述 | 状态 |
|------|------|------|
| 摘要 | 结构化 vs 叙事性摘要 | ✅ 可用 |
| 引言 | 问题-空白-贡献 流程 | ✅ 可用 |
| 相关工作 | 定位与差异化 | � 开发中 |
| 方法 | 可复现性导向 | 📋 计划中 |
| Rebuttal | 审稿人回复策略 | 📋 计划中 |

## 快速开始

### Kiro 用户
```bash
# 在你的论文项目中
mkdir -p .kiro/steering
cp academic-writing-ai/styles/ieee-transactions.md .kiro/steering/
```

### Claude Code 用户
```bash
cp academic-writing-ai/styles/nature-style.md .claude/CLAUDE.md
```

### Cursor 用户
```bash
cp academic-writing-ai/styles/nature-style.md .cursorrules
```

## 参与贡献

欢迎贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 如何贡献新风格
1. Fork 本仓库
2. 创建 `styles/your-journal-style.md`
3. 包含：语气风格指南、结构模板、常用短语、常见错误
4. 提交 PR，附带修改前后的示例

## 项目理念

> "作为曾经在'有好想法'和'用正确的风格表达出来'之间挣扎过的研究者，我们希望把那些以前只有通过昂贵工具或资深导师才能获得的写作指导，开放给所有人。"

## 相关项目

- [academic-graph-ai](https://github.com/MiangChen/academic-graph-ai) — AI 辅助论文绘图

## 许可证

MIT — 自由使用，欢迎回馈。
