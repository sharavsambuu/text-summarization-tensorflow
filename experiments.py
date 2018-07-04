from utils import *

#train_article_path = "sumdata/train/train.article.txt"
#train_title_path = "sumdata/train/train.title.txt"
#valid_article_path = "sumdata/train/valid.article.filter.txt"
#valid_title_path = "sumdata/train/valid.title.filter.txt"



print("Loading dictionary...")
word_dict, reversed_dict, article_max_len, summary_max_len = build_dict("train", True)

print("Loading validation dataset...")
valid_x, valid_y = build_dataset("train", word_dict, article_max_len, summary_max_len, True)
valid_x_len = list(map(lambda x: len([y for y in x if y != 0]), valid_x))
