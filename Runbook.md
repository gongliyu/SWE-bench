# Run inference
https://github.com/gongliyu/SWE-agent/blob/main/Runbook.md

# Prepare Python Env
## Create conda env
```shell
conda create -n SWE-bench python=3.10 -y
conda activate SWE-bench
pip install --upgrade pip setuptools wheel
```
## Install
```shell
git clone https://github.com/gongliyu/SWE-bench.git
cd SWE-bench
pip install -e .
```

## Run evaluation
### Go back to the direactory of SWE-agent
```shell
cd path/to/swe-agent
```
### GPT-5.3-codex
```shell
python -m swebench.harness.run_evaluation \                        [11:55:11]
    --dataset_name princeton-nlp/SWE-bench_Lite \
    --predictions_path trajectories/eval_gpt_53/preds.json \
    --max_workers 2 \
    --run_id gpt_53_codex_run
```

### Claude-sonnet-4.6
```shell
python -m swebench.harness.run_evaluation \                        [11:55:11]
    --dataset_name princeton-nlp/SWE-bench_Lite \
    --predictions_path trajectories/eval_claude_sonnet_4_6/preds.json \
    --max_workers 2 \
    --run_id claude_sonnet_4_6_run
```

### Claude-opus-4.6
```shell
python -m swebench.harness.run_evaluation \                        [11:55:11]
    --dataset_name princeton-nlp/SWE-bench_Lite \
    --predictions_path trajectories/eval_claude_opus_4_6/preds.json \
    --max_workers 2 \
    --run_id claude_opus_4_6_run
```