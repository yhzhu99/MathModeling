# 导入依赖库
import json
import codecs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 加载数据集
train_filename='train.json'
train_content = pd.read_json(codecs.open(train_filename, mode='r', encoding='utf-8'))

test_filename = 'test.json'
test_content = pd.read_json(codecs.open(test_filename, mode='r', encoding='utf-8'))

categories=np.unique(train_content['cuisine'])
print("一共包含 {} 种菜品，分别是:\n{}".format(len(categories),categories))

### 将特征与目标变量分别赋值
train_ingredients = train_content['ingredients']
train_targets = train_content['cuisine']

## 统计意大利菜系中佐料出现次数，并赋值到italian_ingredients字典中
list_italian = train_content.loc[train_content['cuisine'].isin(['italian'])]['ingredients'].reset_index(drop=True)
n = []
for j in range(len(list_italian)):
    n += list_italian[j]
italian_ingredients = pd.Series(n).value_counts().to_dict()

plt.style.use(u'ggplot')
fig = pd.DataFrame(italian_ingredients, index=[0]).transpose()[0].sort_values(ascending=False, inplace=False)[:10].plot(kind='barh')
fig.invert_yaxis()
fig = fig.get_figure()
fig.tight_layout()

import re
from nltk.stem import WordNetLemmatizer
import numpy as np
def text_clean(ingredients):
    #去除单词的标点符号，只保留 a..z A...Z的单词字符
    ingredients= np.array(ingredients).tolist()
    print("菜品佐料：\n{}".format(ingredients[9]))
    ingredients=[[re.sub('[^A-Za-z]', ' ', word) for word in component]for component in ingredients]
    print("去除标点符号之后的结果：\n{}".format(ingredients[9]))

    # 去除单词的单复数，时态，只保留单词的词干
    lemma=WordNetLemmatizer()
    ingredients=[" ".join([ " ".join([lemma.lemmatize(w) for w in words.split(" ")]) for words in component])  for component in ingredients]
    print("去除时态和单复数之后的结果：\n{}".format(ingredients[9]))
    return ingredients

print("\n处理训练集...")
train_ingredients = text_clean(train_content['ingredients'])
print("\n处理测试集...")
test_ingredients = text_clean(test_content['ingredients'])
from sklearn.feature_extraction.text import TfidfVectorizer
# 将佐料转换成特征向量

# 处理 训练集
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 1),
                analyzer='word', max_df=.57, binary=False,
                token_pattern=r"\w+",sublinear_tf=False)
train_tfidf = vectorizer.fit_transform(train_ingredients).todense()

## 处理 测试集
test_tfidf = vectorizer.transform(test_ingredients)
train_targets=np.array(train_content['cuisine']).tolist()
train_targets[:10]


### 划分出验证集
from sklearn.model_selection import train_test_split
X_train , X_valid , y_train, y_valid = train_test_split(train_tfidf, train_targets, test_size = 0.2, random_state=0)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

## 建立逻辑回归模型
parameters = {'C':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
classifier = LogisticRegression()
grid = GridSearchCV(classifier, parameters)

grid = grid.fit(X_train, y_train)

from sklearn.metrics import accuracy_score ## 计算模型的准确率

valid_predict = grid.predict(X_valid)
valid_score=accuracy_score(y_valid,valid_predict)

print("验证集上的得分为：{}".format(valid_score))