#!/bin/bash
# Academic Writing AI 环境安装脚本
# 用法: bash setup.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config_llm.json"
CONFIG_EXAMPLE="$SCRIPT_DIR/config_llm_example.json"
SETUP_MARKER="$SCRIPT_DIR/.setup_done"
ENV_NAME="academic_writing_311"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}=== Academic Writing AI 环境安装 ===${NC}"

# 检查 conda 是否安装
if ! command -v conda &> /dev/null; then
    echo -e "${RED}[错误] 未找到 conda，请先安装 Anaconda 或 Miniconda${NC}"
    exit 1
fi

# 创建 conda 环境
echo -e "${YELLOW}[1/3] 创建 conda 环境 ${ENV_NAME}...${NC}"
if conda env list | grep -q "^${ENV_NAME} "; then
    echo -e "${GREEN}[Setup] 环境 ${ENV_NAME} 已存在，跳过创建${NC}"
else
    if ! conda create -n "$ENV_NAME" python=3.11 -y; then
        echo -e "${RED}[错误] conda 环境创建失败${NC}"
        exit 1
    fi
fi

# 激活环境并安装依赖
echo -e "${YELLOW}[2/3] 安装 LangGraph 依赖...${NC}"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

if ! pip install -r "$SCRIPT_DIR/requirements.txt"; then
    echo -e "${RED}[错误] pip install 失败${NC}"
    exit 1
fi

# 检查配置文件
echo -e "${YELLOW}[3/3] 检查配置文件...${NC}"
if [ ! -f "$CONFIG_FILE" ]; then
    if [ -f "$CONFIG_EXAMPLE" ]; then
        cp "$CONFIG_EXAMPLE" "$CONFIG_FILE"
        echo -e "${GREEN}[Setup] 已从示例创建配置文件: $CONFIG_FILE${NC}"
    fi
    echo -e "${YELLOW}[Setup] 请编辑 $CONFIG_FILE 填入你的 API Key 和 Base URL${NC}"
else
    echo -e "${GREEN}[Setup] 配置文件已存在: $CONFIG_FILE${NC}"
fi

# 创建安装标记
touch "$SETUP_MARKER"

echo ""
echo -e "${GREEN}=== 安装完成 ===${NC}"
echo -e "${YELLOW}下一步:${NC}"
echo -e "${YELLOW}  1. 编辑 config_llm.json 填入 API Key${NC}"
echo -e "${YELLOW}  2. 运行 bash start.sh 启动工作流${NC}"
