# DEMO1-Bert
## 基于 BERT 的今日头条新闻文本分类模型

> 本项目基于 `bert-base-chinese` 预训练模型，完成15类中文新闻文本分类任务，搭建包含数据加载、模型训练、效果评估、单句预测的完整流水线，使用 SwanLab 对训练过程可视化记录。
> ⚠️ 说明：模型权重文件 `best_model.pth` 文件体积较大，未上传至仓库。训练时通过 `savemodel()` 函数保存以下文件：
> - `best_model.pth`：模型权重
> - `training_config.json`：训练参数配置
> - `data/label_id.txt`、`data/id_label.txt`：标签与ID双向映射文件
> - `tokenizer`：分词器文件

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

### 数据分析
<img width="1324" height="167" alt="数据样例" src="https://github.com/user-attachments/assets/705cac3e-63bb-4f29-8bd2-70ee0d8b7187" />

读取原始数据可见每条样本包含5个字段。数据预处理阶段，将**新闻标题**与**关键词**使用中文逗号拼接，作为模型输入文本，增强分类特征。

---

## 二、模型实验指标
<img width="526" height="300" alt="image" src="https://github.com/user-attachments/assets/9b2a6c15-be21-48b0-9797-c3b056d78aa6" />
<img width="1046" height="300" alt="image" src="https://github.com/user-attachments/assets/0ebd246b-0e75-48b5-999b-826f937eacf9" />
<img width="522" height="298" alt="image" src="https://github.com/user-attachments/assets/fb74085d-69ed-4f03-9040-0f654cc04b91" />
<img width="536" height="302" alt="image" src="https://github.com/user-attachments/assets/d66d09fc-2906-4ad2-bf5a-7f9888bb579c" />

### 分类报告
<img width="695" height="663" alt="b2302d07500611570c4034be663a1eb2" src="https://github.com/user-attachments/assets/0f7bfcc8-8d61-4279-8340-243d05685a01" />

### 模型效果分析
模型最佳验证集准确率 **85.8%**，测试集准确率 **84.96%**，测试集加权平均F1值为0.85。
- 效果较好类别：新闻汽车(F1=0.94)、新闻教育(F1=0.92)、新闻文化(F1=0.92)，文本特征区分度高。
- 效果较差类别：股票(F1=0.65)、新闻故事(F1=0.76)、新闻财经(F1=0.70)。股票与故事类别样本数量少，存在类别不均衡问题；财经与股票语义相近，容易混淆。




---

## 三、单句预测演示
<img width="330" height="79" alt="image" src="https://github.com/user-attachments/assets/f669e63f-f75f-4f9c-bd3d-7f7c0d7e4975" />

### 使用方式
运行 `Predict.py`，可自定义输入文本进行推理。

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
├── Predict.py               # 预测脚本
├── trainer.py               # 训练脚本
├── utils.py                 # 工具函数
├── requirements.txt         # 依赖
└── README.md                # 项目说明
