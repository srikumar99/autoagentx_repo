# AutoAgent-X 🤖

**A Hierarchical Goal-Decomposition Model for Autonomous Multi-Step Task Execution**

[![Paper](https://img.shields.io/badge/paper-arXiv-red)](https://arxiv.org/abs/2502.XXXXX)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-green)](https://www.python.org/)
[![MegaTask-200](https://img.shields.io/badge/benchmark-MegaTask--200-orange)](https://github.com/autoagentx/megatask200)



---

## 🏗️ Architecture Overview

AutoAgent-X is organised into **four tightly integrated layers**:

```
User Task Input
      │
      ▼
┌─────────────────────────────────────────┐
│   Goal Decomposition Engine (GDE)       │  ← Layer 1
│   Parses NL goals → DAG of sub-goals    │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│   Hierarchical Task Planner (HTP)       │  ← Layer 2
│   DAG → Scheduled execution plan        │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│   Adaptive Execution Controller (AEC)  │  ← Layer 3
│   Executes, monitors, repairs failures  │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│   Persistent Episodic Memory (PEMM)     │  ← Layer 4
│   Cross-episode learning & reflection   │
└─────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/autoagentx/autoagentx.git
cd autoagentx
pip install -e ".[full]"
```

### Set API Keys

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."   # optional
```

### Run a Single Task

```python
from autoagentx import AutoAgentX

agent = AutoAgentX.from_config("configs/default.yaml")

result = agent.run(
    task="Find the top 5 AI papers published this week on arXiv, "
         "summarise each one, and save a markdown report to ./report.md"
)

print(f"Success: {result.success}")
print(f"Steps taken: {result.steps}")
print(f"Output: {result.output}")
```

### Run on MegaTask-200

```bash
python scripts/run_benchmark.py \
    --benchmark megatask200 \
    --config configs/default.yaml \
    --output results/megatask200_run1.json \
    --num_workers 4
```

---

## 📦 Installation Options

| Extra | Description |
|-------|-------------|
| `pip install -e ".[full]"` | All dependencies (recommended) |
| `pip install -e ".[minimal]"` | Core only (GPT-4 backend) |
| `pip install -e ".[dev]"` | + testing and linting tools |
| `pip install -e ".[memory]"` | + FAISS vector memory |

---

## 📁 Repository Structure

```
autoagentx/
├── autoagentx/              # Main package
│   ├── core/                # Agent orchestration
│   │   ├── agent.py         # AutoAgentX main class
│   │   ├── config.py        # Configuration dataclasses
│   │   └── result.py        # Result / trajectory types
│   ├── planning/            # Layers 1 & 2
│   │   ├── gde.py           # Goal Decomposition Engine
│   │   ├── dag.py           # DAG data structures & algorithms
│   │   ├── htp.py           # Hierarchical Task Planner
│   │   ├── scheduler.py     # Parallel execution scheduler
│   │   └── complexity.py    # Complexity classifier
│   ├── execution/           # Layer 3
│   │   ├── aec.py           # Adaptive Execution Controller
│   │   ├── repair.py        # Local repair strategies
│   │   └── subagent.py      # Sub-agent delegation
│   ├── memory/              # Layer 4
│   │   ├── pemm.py          # Persistent Episodic Memory Module
│   │   ├── episodic.py      # Episodic store (FAISS)
│   │   ├── semantic.py      # Semantic tool-pattern cache
│   │   └── reflection.py    # Self-reflection protocol
│   ├── tools/               # Built-in tool adapters
│   │   ├── web_search.py
│   │   ├── code_executor.py
│   │   ├── file_io.py
│   │   ├── api_caller.py
│   │   └── email_sender.py
│   └── utils/
│       ├── llm.py           # LLM backend abstraction
│       ├── tokenizer.py
│       └── logging.py
├── configs/                 # YAML experiment configs
├── experiments/             # Experiment scripts
├── scripts/                 # Benchmark runners
├── tests/                   # Unit + integration tests
├── weights/                 # Pre-trained model weights (see below)
├── docs/                    # Extended documentation
├── setup.py
└── pyproject.toml
```

---

## 🧠 Pre-trained Model Weights

We release two pre-trained components:

| Model | Size | Description | Download |
|-------|------|-------------|----------|
| `complexity_classifier_v1` | 220 MB | T5-large fine-tuned goal complexity scorer | [weights/](weights/) |
| `action_selector_v1` | 490 MB | 125M-param action-selection transformer | [weights/](weights/) |

Download and place in `weights/`:
```bash
python scripts/download_weights.py --all
```

Or download individually:
```bash
python scripts/download_weights.py --model complexity_classifier_v1
python scripts/download_weights.py --model action_selector_v1
```

---

## ⚙️ Configuration

Edit `configs/default.yaml`:

```yaml
llm:
  provider: openai              # openai | anthropic | local
  model: gpt-4-0125-preview
  temperature_plan: 0.0
  temperature_execute: 0.2
  max_tokens: 4096

gde:
  max_depth: 8
  complexity_threshold: 0.15
  validation: true

htp:
  max_parallel: 4
  token_budget_total: 32768
  token_budget_min_per_node: 512
  token_budget_max_per_node: 8192

aec:
  max_repair_attempts: 3
  delegation_threshold: 0.65

memory:
  enabled: true
  top_k_retrieval: 5
  embedding_model: text-embedding-ada-002
  index_path: .autoagentx_memory/faiss.index
```

---

## 📊 Reproducing Paper Results

### AgentBench

```bash
python experiments/run_agentbench.py \
    --config configs/agentbench.yaml \
    --output results/agentbench_results.json
```

### WebArena

```bash
# Requires a running WebArena server (see docs/webarena_setup.md)
python experiments/run_webarena.py \
    --server_url http://localhost:4999 \
    --config configs/webarena.yaml \
    --output results/webarena_results.json
```

### MegaTask-200

```bash
python experiments/run_megatask200.py \
    --config configs/megatask200.yaml \
    --output results/megatask200_results.json \
    --domains all \
    --difficulty all
```

### Ablation Study

```bash
bash experiments/run_ablations.sh
# Results saved to results/ablations/
```

### Scaling Analysis

```bash
python experiments/run_scaling.py \
    --max_subgoals 25 \
    --output results/scaling_results.json
```

---

## 📈 Results Summary

| Benchmark | AutoAgent-X | Best Baseline | Improvement |
|-----------|-------------|---------------|-------------|
| MegaTask-200 TSR | **89.1%** | 74.3% (TaskMatrix) | +14.8 pp |
| AgentBench Score | **0.71** | 0.56 (TaskMatrix) | +26.8% |
| WebArena TSR | **62.4%** | 53.1% (TaskMatrix) | +17.5% |
| Avg. Steps (MT-200) | **6.8** | 9.1 (TaskMatrix) | −25.3% |

---

## 🧪 Running Tests

```bash
pytest tests/ -v
pytest tests/unit/ -v          # Unit tests only
pytest tests/integration/ -v  # Integration tests (requires API keys)



