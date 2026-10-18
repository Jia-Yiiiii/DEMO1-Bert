#  DEMO1-Bert: 基于 BERT 的今日头条新闻文本分类模型


> 本项目基于 `bert-base-chinese` 预训练模型，构建了一套完整的中文新闻文本分类流水线，涵盖数据加载、模型训练、效果评估及单句预测等核心功能。训练过程全程使用 **SwanLab** 进行可视化记录与监控。

⚠️ **关于模型权重**：由于 `best_model.pth` 文件体积较大，未上传至本仓库。请在训练完成后，通过 `savemodel()` 函数自动保存至本地查看。

---


---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 模型下载及训练

```bash
python modeldownload.py
```
下载好模型后，运行训练脚本：

```bash
python trainer.py
```

### 3. 单句预测

运行预测脚本，可自定义输入文本进行实时推理：

```bash
python predict.py
```

---

## 数据集说明

本项目采用 **今日头条新闻标题分类数据集**。

- **数据来源**：今日头条客户端
- **采集时间**：2018年5月
- **项目地址**：[toutiao-text-classfication-dataset](https://github.com/aceimnorstuvwxz/toutiao-text-classfication-dataset)
- **分类类别**：15 个新闻类别

### 数据集划分

| 数据文件 | 样本数量 | 用途 |
| :--- | :--- | :--- |
| `train_3k.txt` | 3,000 | 训练集 |
| `dev_1k.txt` | 1,000 | 验证集 |
| `test_1k.txt` | 1,064 | 测试集 |

---

## 模型实验指标

### 实验过程可视化
<img width="488" height="446" alt="image" src="https://github.com/user-attachments/assets/d0477373-8684-4371-a7bf-0d495292b13a" />
<img width="951" height="443" alt="image" src="https://github.com/user-attachments/assets/74d37ee0-6457-40c3-8107-c749904b31c8" />
<img width="947" height="456" alt="image" src="https://github.com/user-attachments/assets/aab5a687-85dc-4e77-8330-ba9e0dbb15a2" />


### 分类评估报告
<img width="707" height="547" alt="0596237445eaae764a9e7bdf975d3e21" src="https://github.com/user-attachments/assets/9dd89195-1cc8-416c-8989-9cd83ef80104" />


### 模型效果分析

在本次 BERT 文本分类模型的测试集评估中，模型整体表现优异，具备较强的泛化能力：

- **整体性能**：加权平均 **F1 分数达到 0.8389**，**准确率为 0.8383**。
- **优势类别**：在 `news_car` (F1=0.9353)、`news_culture` (F1=0.9161) 和 `news_sports` (F1=0.9016) 等类别上识别效果突出，特征提取精准。
- **待优化类别**：`stock` (F1=0.6207)、`news_finance` (F1=0.6667) 和 `news_story` (F1=0.7692) 表现相对较弱。这主要归因于小样本分布不均或类别间存在语义模糊，后续可通过数据增强或对比学习进一步优化。

---

## 单句预测演示

运行 `predict.py` 即可体验模型推理能力：
![Uploading image.png…]()


---

##  项目结构

```text
DEMO1-Bert/
├── data/                    # 数据集文件夹
│   ├── train_3k.txt         # 训练集数据
│   ├── dev_1k.txt           # 验证集数据
│   ├── test_1k.txt          # 测试集数据
│   └── label_map.json       # 标签映射文件
├── configs/                 #  配置文件目录
│   └── Bert_Config_exp1.json
├── model.py                 # 模型结构定义
├── predict.py               # 单句预测脚本
├── trainer.py               # 模型训练脚本
├── modeldownload.py         # 模型下载工具
├── utils.py                 #  通用工具函数
├── data_process.py          # 数据处理脚本
├── requirements.txt         # 依赖包列表
└── README.md                # 项目说明文档
