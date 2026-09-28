# DEMO1-Bert

基于 BERT 的今日头条新闻文本分类模型

---

## 项目介绍

本项目使用 bert-base-chinese 预训练模型，对 15 类中文新闻文本进行自动分类，实现了从数据加载、模型训练、模型评估到单句预测的完整流程，并通过 SwanLab 可视化实验过程。



> 注：模型文件 `best_model.pth` 因体积较大未上传。
> ## 模型保存

训练时通过 `savemodel()` 保存以下文件：
- `best_model.pth` - 模型权重
- `training_config.json` - 训练参数
- `data/label_id.txt` 和 `data/id_label.txt` - 标签映射
- `tokenizer` - 分词

---

## 数据集

本项目使用今日头条新闻标题分类数据集。

- **数据来源**：今日头条客户端
- **采集时间**：2018 年 5 月
- **下载地址**：[toutiao-text-classfication-dataset](https://github.com/aceimnorstuvwxz/toutiao-text-classfication-dataset)
- **分类数量**：15 类

### 数据划分

| 数据文件 | 样本数量 | 用途 |
| ------- | -------- | ---- |
| `train_3k.txt` | 3,000 | 训练集 |
| `dev_1k.txt` | 1,000 | 验证集 |
| `test_1k.txt` | 1,064 | 测试集 |

---

## 数据分析

<img width="1324" height="167" alt="数据样例" src="https://github.com/user-attachments/assets/705cac3e-63bb-4f29-8bd2-70ee0d8b7187" />

通过读取数据前五行发现，数据的构成为五个部分。预处理时，将每条新闻的**标题**和**关键词**用中文逗号拼接，作为模型的输入文本，以辅助模型进行分类。

---

## 模型指标
<img width="526" height="300" alt="image" src="https://github.com/user-attachments/assets/9b2a6c15-be21-48b0-9797-c3b056d78aa6" />
<img width="1046" height="300" alt="image" src="https://github.com/user-attachments/assets/0ebd246b-0e75-48b5-999b-826f937eacf9" />
<img width="522" height="298" alt="image" src="https://github.com/user-attachments/assets/fb74085d-69ed-4f03-9040-0f654cc04b91" />
<img width="536" height="302" alt="image" src="https://github.com/user-attachments/assets/d66d09fc-2906-4ad2-bf5a-7f9888bb579c" />


### 整体分类报告

<img width="695" height="663" alt="b2302d07500611570c4034be663a1eb2" src="https://github.com/user-attachments/assets/0f7bfcc8-8d61-4279-8340-243d05685a01" />





### 表现分析

模型整体表现良好，验证集最佳准确率达到87.2%，测试集准确率为84.8%。从各类别F1分数来看，汽车、教育、体育等类别表现优秀，特征明显易于区分；故事和股票（表现最差。从混淆矩阵分析，主要问题集中在财经与股票相互混淆，故事与文化娱乐类边界模糊，总体而言，受限于训练数据量，部分语义相近的类别区分困难，后续可以通过补充标注数据或数据增强来进一步优化。

## 单句预测演示


<img width="330" height="79" alt="image" src="https://github.com/user-attachments/assets/f669e63f-f75f-4f9c-bd3d-7f7c0d7e4975" />

### 使用方式

运行 `Predict.py`，可自定义输入文本进行推理。

---

## 项目结构

```text
classify-bert-DEMO1/
├── DATA/                    # 数据集文件夹
│   ├── train_3k.txt         # 训练集
│   ├── dev_1k.txt           # 验证集
│   ├── test_1k.txt          # 测试集
│   └── label_map.json       # 标签映射文件
├── configs/                 # 配置文件目录
│   └── Bert_Config_exp1.json
├── model.py                 # 模型结构
├── Predict.py               # 预测脚本
├── trainer.py               # 训练脚本
├── utils.py                 # 工具函数
├── requirements.txt         # 依赖
└── README.md                # 项目说明
