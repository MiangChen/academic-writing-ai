# IEEE Transactions on Robotics (T-RO) Style Guide

> This file is designed to be used as a steering file for AI coding assistants (Kiro, Claude Code, Cursor, etc.)

## About IEEE T-RO

IEEE Transactions on Robotics (T-RO) is a premier journal covering robotics research including manipulation, locomotion, multi-robot systems, human-robot interaction, and robot learning. It emphasizes both theoretical rigor and experimental validation.

## Voice & Tone

1. **Technical Precision**: Use domain-specific robotics terminology accurately (e.g., "end-effector" not "robot hand", "degrees of freedom" not "joints").
2. **First Person Plural Accepted**: T-RO commonly accepts "We propose..." style, though third person is also acceptable.
3. **Balance Theory and Practice**: T-RO values both theoretical contributions (proofs, analysis) and real-world experiments on physical robots.
4. **Quantitative Rigor**: Include specific metrics — success rate, completion time, position error (in mm), orientation error (in degrees), etc.

## Structure Templates

### Abstract (150-200 words)
```
[1-2 sentences: Problem motivation in robotics context]
[1 sentence: Limitation of existing approaches]
[1-2 sentences: Your proposed method and key innovation]
[2-3 sentences: Experimental validation — simulation AND real robot results preferred]
[1 sentence: Significance or broader impact]
```

### Introduction (5-6 paragraphs)
```
P1: Real-world robotics application and motivation
P2: Technical challenges specific to the problem
P3: Brief review of existing approaches and their limitations
P4: Your key insight and proposed solution
P5: Summary of contributions (itemized list, 3-4 items)
P6: Paper organization
```

### Contribution Statement Format
```latex
The main contributions of this work are summarized as follows:
\begin{itemize}
    \item We propose [method/algorithm name], a [brief description] for [problem].
    \item We provide [theoretical analysis, e.g., stability proof, convergence guarantee, complexity analysis].
    \item We validate the proposed method through [simulation environment] and real-world experiments on [robot platform].
    \item We release our [code/dataset/benchmark] to facilitate future research.
\end{itemize}
```

### Experiments Section Structure
```
A. Experimental Setup
   - Robot platform specifications
   - Sensor configurations
   - Computing hardware
   - Software framework (ROS version, etc.)

B. Simulation Experiments
   - Simulator used (Gazebo, Isaac Sim, MuJoCo, etc.)
   - Benchmark scenarios
   - Comparison with baselines

C. Real-World Experiments
   - Physical setup description
   - Safety considerations
   - Quantitative results with error bars/statistics

D. Ablation Studies
   - Component-wise analysis
   - Parameter sensitivity
```

## Common Phrases

### Introducing the Problem
- "Autonomous [task] remains a fundamental challenge in robotics due to..."
- "Enabling robots to [capability] is essential for applications in [domain]..."
- "Multi-robot coordination for [task] has gained increasing attention..."

### Describing Technical Challenges
- "The key challenge lies in [specific difficulty]..."
- "This problem is particularly challenging because..."
- "Existing methods struggle with [limitation] in real-world scenarios..."

### Describing Your Method
- "To address these challenges, we propose..."
- "The core idea of our approach is to..."
- "Our method differs from prior work in that..."
- "We formulate the problem as..."

### Presenting Experimental Results
- "We validate our approach through extensive experiments in both simulation and real-world settings."
- "The proposed method achieves [metric] of X.XX (±Y.YY), outperforming [baseline] by Z%."
- "Real-robot experiments demonstrate that..."
- "The results confirm the effectiveness and generalizability of..."

### Discussing Limitations
- "While our method achieves [strength], it has limitations in [aspect]..."
- "Future work will address [limitation] by..."

## T-RO Specific Requirements

### Experimental Validation
- **Simulation alone is insufficient**: T-RO strongly prefers papers with real-robot experiments
- **Statistical significance**: Report mean ± std over multiple trials (typically 10+)
- **Failure analysis**: Discuss failure cases and their causes
- **Video attachment**: Supplementary video demonstrating real-robot experiments is highly recommended

### Mathematical Rigor
- **Formal problem statement**: Clearly define state space, action space, objective function
- **Theoretical guarantees**: Stability analysis, convergence proofs, or complexity bounds when applicable
- **Notation consistency**: Use standard robotics notation (SE(3), SO(3), etc.)

## Common Pitfalls to Avoid

1. **Simulation-Only Results**: T-RO reviewers often reject papers without real-robot validation.
2. **Missing Error Analysis**: Always report uncertainty/variance, not just mean performance.
3. **Unfair Comparisons**: Ensure baselines use the same sensor inputs and computational budget.
4. **Ignoring Practical Constraints**: Address real-world issues like sensor noise, latency, and calibration.
5. **Overclaiming Generality**: Be specific about the scope and assumptions of your method.

## Example Transformations

### Before (Too Vague)
> Our multi-robot system works well in various scenarios and outperforms existing methods.

### After (T-RO Style)
> We validate the proposed coordination framework on a team of six quadrotors in both simulated (Gazebo) and real-world indoor environments. Our method achieves a task success rate of 94.2% (±3.1%) across 50 trials, compared to 78.5% (±5.2%) for the decentralized baseline, while reducing average completion time from 45.3s to 32.1s.

### Before (Missing Details)
> We use deep learning to solve the manipulation problem.

### After (T-RO Style)
> We formulate the manipulation task as a Markov Decision Process and train a policy network using Proximal Policy Optimization (PPO). The policy takes as input the RGB-D observation (640×480) and proprioceptive state (7-DoF joint positions and velocities), and outputs end-effector velocity commands at 10 Hz. Training is conducted in Isaac Sim with domain randomization, followed by zero-shot transfer to a Franka Emika Panda robot.

## Reference Style

T-RO uses IEEE citation format:
```
[1] S. Zhao and D. Zelazo, "Bearing rigidity theory and its applications for control and estimation of network systems," IEEE Control Syst. Mag., vol. 39, no. 2, pp. 66–83, 2019.
```

Key formatting rules:
- Author initials before surname
- Article titles in sentence case with quotes
- Journal names abbreviated and italicized
- Include volume, number, pages, and year
