from modelscope import snapshot_download

model_dir = snapshot_download(
    "tiansz/bert-base-chinese",
    local_dir="./bert-model"
)
print(model_dir)
