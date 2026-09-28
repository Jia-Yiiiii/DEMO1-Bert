import json
import torch
import random
import numpy as np
from sklearn.metrics import classification_report

def set_seed(seed=42):    
    random.seed(seed)    
    np.random.seed(seed)    
    torch.manual_seed(seed)    
    if torch.cuda.is_available():        
        torch.cuda.manual_seed_all(seed)     
    torch.backends.cudnn.deterministic = True    
    torch.backends.cudnn.benchmark = False  

class Metrics:    
    def __init__(self, id_label):        
        self.id_label = id_label        
        self.name_map = {            
            "news_story": "新闻故事",            
            "news_culture": "新闻文化",            
            "news_entertainment": "新闻娱乐",            
            "news_sports": "新闻体育",            
            "news_finance": "新闻财经",            
            "news_house": "新闻房产",            
            "news_car": "新闻汽车",            
            "news_edu": "新闻教育",            
            "news_tech": "新闻科技",            
            "news_military": "新闻军事",            
            "news_travel": "新闻旅游",            
            "news_world": "新闻国际",            
            "stock": "股票",            
            "news_agriculture": "新闻农业",            
            "news_game": "新闻游戏",        
        }     

    def accuracy(self, truths, preds):        
        correct = 0        
        for i in range(len(truths)):            
            if truths[i] == preds[i]:                
                correct += 1        
        return correct / len(truths)     

    def plot(self, truths, preds):        
        class_names = []        
        for i in range(len(self.id_label)):            
            en_name = self.id_label[i]            
            cn_name = self.name_map.get(en_name, en_name)            
            class_names.append(cn_name)         

        print("\n分类报告:")        
        print(classification_report(truths, preds, target_names=class_names))         

        f1s = []        
        for i in range(len(class_names)):            
            tp = 0            
            fp = 0            
            fn = 0            
            for j in range(len(truths)):                
                if truths[j] == i and preds[j] == i:                    
                    tp += 1                
                if truths[j] != i and preds[j] == i:                    
                    fp += 1                
                if truths[j] == i and preds[j] != i:                    
                    fn += 1             
            if tp + fp <= 0 or tp + fn <= 0:                
                f1 = 0            
            else:                
                p = tp / (tp + fp)                
                r = tp / (tp + fn)                
                f1 = 2 * p * r / (p + r)            
            f1s.append(f1)
