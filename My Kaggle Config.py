# examples/my-kaggle-config.py
#
# This is not a notebook, and it's not meant to run as-is anywhere but my own
# account. It's the actual Cell 0 I run, unedited, kept here as proof this
# was a real working setup and not just a hypothetical template. If you want
# to run Trinity yourself, use trinity_notebook.ipynb and fill in your own
# Cell 0 instead of copying this one.

import os

WORKDIR = "/kaggle/working"
DATASET_DIR = "/kaggle/input/datasets/swayamohapatra/trinity-40b-core"
LLAMA_CPP_SRC = f"{DATASET_DIR}/llama.cpp-b9775-cuda-12.8-amd64/cuda-12.8"
MODEL_DIR = DATASET_DIR

RUNNING_ON_KAGGLE = True
FIX_SYMLINKS = True
CUDA_LIB_PATHS = ["/usr/local/nvidia/lib64", "/usr/local/cuda/lib64"]

LLAMA_LIB_VERSION = "0.0.1"
GGML_LIB_VERSION = "0.15.2"

MODEL_TALK = "L3.2-Rogue-Creative-Instruct-Uncensored-7B-D_AU-q5_k_m.gguf"
MODEL_VISION = "Qwen3.5-9B-Claude-4.6-OS-AV-H-UNCENSORED-THINK-D_AU-Q5_K_M-imat.gguf"
MMPROJ_VISION = "mmproj-F16(9B).gguf"
MODEL_DEEP = "Qwen3.6-40B-Deck-Opus-NEO-CODE-HERE-2T-OT-Q4_K_M.gguf"
MMPROJ_DEEP = "mmproj-F16.gguf"
MODEL_CYBERREALISTIC = "CyberRealistic_V4.1_FP16.safetensors"
MODEL_REALVISXL = "RealVisXL_V5.0_Lightning_fp16.safetensors"

PORT_TALK = 8081
PORT_VISION = 8082
PORT_DEEP = 8083
PORT_WEBUI = 3000
PORT_IMAGE = 7860

WEBUI_REQUIRE_LOGIN = True
