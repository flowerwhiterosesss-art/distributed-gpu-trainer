# Distributed GPU Trainer

High-performance distributed training framework for large language models. Supports multi-node GPU training with automatic gradient synchronization, mixed precision, and dynamic batching.

## Features

- Multi-GPU distributed training with NCCL backend
- Mixed precision (FP16/BF16) with automatic loss scaling
- Dynamic batch sizing based on available VRAM
- Checkpoint management with automatic resume
- Weights & Biases integration for experiment tracking
- Support for LLaMA, Mistral, and custom architectures

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Configure training parameters
python scripts/config_manager.py

# Start training
bash start.sh

# Or run directly
python scripts/train.py --config configs/training.json --epochs 3
```

## Configuration

Edit `configs/training.json` or use the interactive config manager:

```bash
python scripts/config_manager.py
```

## Requirements

- Python 3.10+
- CUDA 12.0+
- PyTorch 2.0+
- 8GB+ VRAM (recommended: 24GB+)

## License

MIT
