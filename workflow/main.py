"""
Academic Writing AI - LangGraph Workflow
一个最简单的学术写作工作流示例
"""

import json
import os
from pathlib import Path
from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# ============ 配置加载 ============

def load_config():
    """加载 LLM 配置"""
    config_path = Path(__file__).parent.parent / "config_llm.json"
    if not config_path.exists():
        console.print("[red]错误: 未找到 config_llm.json[/red]")
        raise FileNotFoundError("请先配置 config_llm.json")
    
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_style(style_name: str) -> str:
    """加载期刊风格 prompt"""
    style_path = Path(__file__).parent.parent / "styles" / f"{style_name}.md"
    if not style_path.exists():
        console.print(f"[yellow]警告: 未找到风格文件 {style_name}.md，使用默认风格[/yellow]")
        return "You are an academic writing assistant."
    
    with open(style_path, "r", encoding="utf-8") as f:
        return f.read()

# ============ 状态定义 ============

class WritingState(TypedDict):
    """工作流状态"""
    style: str              # 期刊风格
    section: str            # 要写的章节 (abstract/intro/related)
    user_input: str         # 用户输入的内容/要求
    draft: str              # 生成的草稿
    feedback: str           # 用户反馈
    final_output: str       # 最终输出
    iteration: int          # 迭代次数

# ============ 节点函数 ============

def write_draft(state: WritingState) -> WritingState:
    """生成初稿"""
    config = load_config()
    style_prompt = load_style(state["style"])
    
    llm = ChatOpenAI(
        api_key=config["api_key"],
        base_url=config["api_base"],
        model=config["model"],
    )
    
    section_prompts = {
        "abstract": "Write an abstract for the following research. Keep it concise (150-250 words).",
        "intro": "Write an introduction section for the following research.",
        "related": "Write a related work section positioning this research.",
    }
    
    section_instruction = section_prompts.get(state["section"], "Help improve this academic writing.")
    
    messages = [
        SystemMessage(content=style_prompt),
        HumanMessage(content=f"{section_instruction}\n\nUser input:\n{state['user_input']}")
    ]
    
    if state.get("feedback") and state["iteration"] > 0:
        messages.append(HumanMessage(content=f"Previous draft:\n{state['draft']}\n\nUser feedback:\n{state['feedback']}\n\nPlease revise based on the feedback."))
    
    console.print("[cyan]正在生成...[/cyan]")
    response = llm.invoke(messages)
    
    return {
        **state,
        "draft": response.content,
        "iteration": state.get("iteration", 0) + 1
    }

def human_review(state: WritingState) -> WritingState:
    """人工审核节点"""
    console.print(Panel(state["draft"], title="[green]生成的草稿[/green]", expand=False))
    
    feedback = Prompt.ask(
        "\n[yellow]请输入反馈[/yellow] (直接回车表示满意，输入 'q' 退出)",
        default=""
    )
    
    if feedback.lower() == 'q':
        return {**state, "feedback": "__QUIT__"}
    
    return {**state, "feedback": feedback}

def finalize(state: WritingState) -> WritingState:
    """最终输出"""
    return {**state, "final_output": state["draft"]}

# ============ 路由函数 ============

def should_continue(state: WritingState) -> str:
    """决定是否继续迭代"""
    if state.get("feedback") == "__QUIT__":
        return "end"
    if not state.get("feedback") or state["feedback"].strip() == "":
        return "finalize"
    if state.get("iteration", 0) >= 5:
        console.print("[yellow]已达到最大迭代次数[/yellow]")
        return "finalize"
    return "revise"

# ============ 构建工作流 ============

def build_workflow():
    """构建 LangGraph 工作流"""
    workflow = StateGraph(WritingState)
    
    # 添加节点
    workflow.add_node("write", write_draft)
    workflow.add_node("review", human_review)
    workflow.add_node("finalize", finalize)
    
    # 设置入口
    workflow.set_entry_point("write")
    
    # 添加边
    workflow.add_edge("write", "review")
    workflow.add_conditional_edges(
        "review",
        should_continue,
        {
            "revise": "write",
            "finalize": "finalize",
            "end": END
        }
    )
    workflow.add_edge("finalize", END)
    
    return workflow.compile()

# ============ 主函数 ============

def main():
    console.print(Panel.fit(
        "[bold green]Academic Writing AI[/bold green]\n"
        "基于 LangGraph 的学术写作工作流",
        border_style="green"
    ))
    
    # 选择风格
    console.print("\n[cyan]可用的期刊风格:[/cyan]")
    styles_dir = Path(__file__).parent.parent / "styles"
    available_styles = [f.stem for f in styles_dir.glob("*.md")]
    for i, style in enumerate(available_styles, 1):
        console.print(f"  {i}. {style}")
    
    style_choice = Prompt.ask(
        "选择风格 (输入名称或序号)",
        default=available_styles[0] if available_styles else "ieee-transactions"
    )
    
    # 处理序号输入
    if style_choice.isdigit():
        idx = int(style_choice) - 1
        if 0 <= idx < len(available_styles):
            style_choice = available_styles[idx]
    
    # 选择章节
    console.print("\n[cyan]要写什么章节?[/cyan]")
    console.print("  1. abstract - 摘要")
    console.print("  2. intro - 引言")
    console.print("  3. related - 相关工作")
    
    section_map = {"1": "abstract", "2": "intro", "3": "related"}
    section_choice = Prompt.ask("选择章节", default="1")
    section = section_map.get(section_choice, section_choice)
    
    # 获取用户输入
    console.print("\n[cyan]请输入你的研究内容/要点 (输入 END 结束):[/cyan]")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    user_input = "\n".join(lines)
    
    if not user_input.strip():
        console.print("[red]错误: 请输入内容[/red]")
        return
    
    # 初始化状态
    initial_state: WritingState = {
        "style": style_choice,
        "section": section,
        "user_input": user_input,
        "draft": "",
        "feedback": "",
        "final_output": "",
        "iteration": 0
    }
    
    # 运行工作流
    app = build_workflow()
    final_state = app.invoke(initial_state)
    
    # 输出结果
    if final_state.get("final_output"):
        console.print("\n")
        console.print(Panel(
            final_state["final_output"],
            title="[bold green]最终输出[/bold green]",
            expand=False
        ))
        
        # 保存到文件
        output_dir = Path(__file__).parent.parent / "output"
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"{section}_{style_choice}.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_state["final_output"])
        console.print(f"\n[green]已保存到: {output_file}[/green]")

if __name__ == "__main__":
    main()
