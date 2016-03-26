## nltk
  
  from nltk.book import *
  text1.concordance('monstrous') =>搜索字符
  text2.similar('very') =>搜索相似字符
  text2.common_contexts(['very', 'monstrous']) =>搜索相似字符(列表传入)
  text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) =>离散图
  text3.generate() =>随机生成字符
  
  len(text3) =>标识符
  len(set(text)) =>类型
  len(text3) / len(set(text3)) =>文本词汇丰富度
  text3.count('smote') / len(text3) =>单词smote出现的次数, 百分比

####频率分布
  f = FreqDist(text1) => 创建给定样本的频率分布
  f.N() =>样本总数
  f.max() =>数值最大的样本
  f.tabulate() =>绘制频率分布表
  f.plot() =>绘制频率分布图
  
  
