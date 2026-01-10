#!/bin/bash
set -e

# Colors
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}🚀 Setting up StreamLive Development Environment...${NC}\n"

# 1. UV Installation
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
else
    echo "✅ uv is already installed"
fi

# 2. Tuist Installation
if ! command -v tuist &> /dev/null; then
    echo "📦 Installing Tuist..."
    if command -v mise &> /dev/null; then
        echo "   Using mise to install tuist..."
        mise install tuist@4.40.0
        mise use tuist@4.40.0
    else
        echo "   Mise not found. Installing via curl script..."
        echo "   NOTE: Mise is recommended for version management."
        curl -Ls https://install.tuist.io | bash
    fi
else
    echo "✅ Tuist is already installed"
fi

# 3. Python Dependencies
echo -e "\n📦 Installing Backend Dependencies..."
cd backend
uv sync
cd ..

# 4. Success
echo -e "\n${GREEN}✨ Setup Complete!${NC}"
echo "Run 'make help' to see available commands."
