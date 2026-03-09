import pandas as pd
from datasets import load_dataset
import json

# 1. Load the SWE-bench Lite dataset
print("Loading dataset...")
dataset = load_dataset("princeton-nlp/SWE-bench_Lite", split="test")
df = dataset.to_pandas()


# 2. Stratified sampling by repo (~33%), ensuring at least 1 sample per repo
def sample_repo(group, frac=0.33):
    n_sample = max(1, int(len(group) * frac))
    return group.sample(n=n_sample, random_state=42)  # random_state ensures reproducibility


sampled_df = df.groupby('repo', group_keys=False).apply(sample_repo)

# 3. Print sampling distribution
print(f"\nTotal sampled: {len(sampled_df)}")
print("Distribution by repo:")
print(sampled_df['repo'].value_counts())

# 4. Save sampled instance_ids to file
sampled_ids = sampled_df['instance_id'].tolist()
with open("mini_lite_instances.txt", "w") as f:
    for i in sampled_ids:
        f.write(f"{i}\n")

print("\nSaved representative subset instance_ids to mini_lite_instances.txt")