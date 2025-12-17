# IEEE Transactions Style Guide

> This file is designed to be used as a steering file for AI coding assistants (Kiro, Claude Code, Cursor, etc.)

## Voice & Tone

When writing for IEEE Transactions journals, adopt the following style:

1. **Formal and Technical**: Use precise technical language. Avoid colloquialisms and casual expressions.
2. **Third Person**: Write in third person ("This paper presents..." not "We present..."). Some IEEE journals now accept first person plural, but third person remains safer.
3. **Passive Voice Acceptable**: Unlike Nature/Science, passive voice is common and accepted ("The algorithm was implemented..." is fine).
4. **Quantitative Claims**: Every claim should be backed by numbers. Avoid vague statements like "significantly improves" — instead say "improves by 15.3%".

## Structure Templates

### Abstract (150-250 words)
```
[1-2 sentences: Problem context and importance]
[1 sentence: Gap in existing methods]
[1-2 sentences: Your approach/contribution]
[2-3 sentences: Key results with numbers]
[1 sentence: Broader implication]
```

### Introduction (4-5 paragraphs)
```
P1: Problem context and real-world motivation
P2: Existing approaches and their limitations (brief, details in Related Work)
P3: Your key insight or approach
P4: Summary of contributions (use itemized list)
P5: Paper organization (optional but common)
```

### Contribution Statement Format
```latex
The main contributions of this paper are as follows:
\begin{itemize}
    \item We propose [method name], which [key innovation].
    \item We provide [theoretical contribution, e.g., convergence proof, complexity analysis].
    \item We conduct extensive experiments on [benchmarks], demonstrating [quantitative improvement].
\end{itemize}
```

## Common Phrases

### Introducing the Problem
- "A fundamental challenge in [field] is..."
- "[Application] has attracted significant attention due to..."
- "Despite considerable progress, existing methods still suffer from..."

### Describing Your Method
- "To address this limitation, we propose..."
- "The key insight behind our approach is..."
- "Unlike prior work that [limitation], our method [advantage]..."

### Presenting Results
- "Experimental results demonstrate that the proposed method achieves..."
- "Compared with state-of-the-art methods, our approach improves [metric] by X%..."
- "The results validate the effectiveness of..."

## Common Pitfalls to Avoid

1. **Overclaiming**: Don't say "optimal" unless you prove optimality. Use "near-optimal" or "effective".
2. **Missing Baselines**: Always compare with recent (last 2-3 years) state-of-the-art methods.
3. **Vague Contributions**: "We propose a novel method" is not a contribution. Specify what makes it novel.
4. **Inconsistent Notation**: Define all symbols in a Notation section or upon first use.

## Example Transformation

### Before (Too Casual)
> We came up with a cool new way to do multi-robot coordination that works way better than the old methods.

### After (IEEE Style)
> This paper presents a novel coordination framework for multi-robot systems that achieves a 23.5% improvement in task completion rate compared to state-of-the-art methods, while reducing computational complexity from O(n²) to O(n log n).
