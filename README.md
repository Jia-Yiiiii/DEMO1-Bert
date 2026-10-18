# DEMO1-Bert
## 基于 BERT 的今日头条新闻文本分类模型

> 本项目基于 `bert-base-chinese` 预训练模型，完成15类中文新闻文本分类任务，搭建包含数据加载、模型训练、效果评估、单句预测的完整流水线，使用 SwanLab 对训练过程可视化记录。
> ⚠️ 说明：模型权重文件 `best_model.pth` 文件体积较大，未上传至仓库。训练时通过 `savemodel()` 函数保存相关文件，可运行后查看


---

## 一、数据集
数据集：今日头条新闻标题分类数据集
- 数据来源：今日头条客户端
- 采集时间：2018年5月
- 项目地址：[toutiao-text-classfication-dataset](https://github.com/aceimnorstuvwxz/toutiao-text-classfication-dataset)
- 分类类别：15个新闻类别

### 数据集划分
| 数据文件 | 样本数量 | 用途 |
| :--- | :--- | :--- |
| `train_3k.txt` | 3000 | 训练集 |
| `dev_1k.txt` | 1000 | 验证集 |
| `test_1k.txt` | 1064 | 测试集 |


---

## 二、模型实验指标
<img width="483" height="458" alt="image" src="https://github.com/user-attachments/assets/f9c43f3b-265a-4602-9186-f77c6eaf92ec" />
<img width="943" height="452" alt="image" src="https://github.com/user-attachments/assets/b612c070-623a-4510-af89-bcff7d23188b" />
<img width="937" height="457" alt="image" src="https://github.com/user-attachments/assets/5acef213-2222-4ab5-a7e3-887fab96251f" />


### 分类报告
<img width="707" height="547" alt="0596237445eaae764a9e7bdf975d3e21" src="https://github.com/user-attachments/assets/eb20a21d-0d69-4d36-a690-9ce8e85ac48b" />


### 模型效果分析
在本次 BERT 文本分类模型的测试集评估中，模型整体表现良好，加权平均 F1 分数达到 0.8389，准确率为 0.8383，表明模型具备较强的泛化能力。其中，news_car（F1=0.9353）、news_culture（F1=0.9161）和 news_sports（F1=0.9016）等类别识别效果突出，而 stock（F1=0.6207）、news_story（F1=0.7692）和 news_finance（F1=0.6667）等小样本或语义模糊类别表现相对较弱




---

## 三、单句预测演示

### 使用方式
运行 `predict.py`，可自定义输入文本进行推理。
<img width="342" height="55" alt="image" src="https://github.com/user-attachments/assets/6bdc7ce0-bf55-47bd-b640-a2883e533b6c" />

---

## 四、项目结构
```text
DEMO1-Bert/
├── data/                    # 数据集文件夹
│   ├── train_3k.txt         # 训练集
│   ├── dev_1k.txt           # 验证集
│   ├── test_1k.txt          # 测试集
│   └── label_map.json       # 标签映射文件
├── configs/                 # 配置文件目录
│   └── Bert_Config_exp1.json
├── model.py                 # 模型结构
├── predict.py               # 预测脚本
├── trainer.py               # 训练脚本
|──modeldownload.py          #模型下载
├── utils.py                 # 工具函数
├── requirements.txt         # 依赖
├── data_process.py          #数据处理
└── README.md                # 项目说明
