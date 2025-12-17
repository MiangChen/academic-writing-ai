#!/bin/bash
# Academic Writing AI 启动脚本
# 用法: bash start.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SETUP_MARKER="$SCRIPT_DIR/.setup_done"
CONFIG_FILE="$SCRIPT_DIR/config_llm.json"
ENV_NAME="academic_writing_314"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 检查是否已安装
if [ ! -f "$SETUP_MARKER" ]; then
    echo -e "${RED}[错误] 请先运行 bash setup.sh 安装环境${NC}"
    exit 1
fi

# 检查配置文件
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}[错误] 未找到 config_llm.json，请从 config_llm_example.json 复制并填入 API Key${NC}"
    exit 1
fi

# 激活 conda 环境
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

echo -e "${GREEN}=== Academic Writing AI ===${NC}"
echo -e "${YELLOW}启动学术写作工作流...${NC}"
echo ""

# 运行工作流
python "$SCRIPT_DIR/workflow/main.py" "$@"
