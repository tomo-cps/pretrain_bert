import numpy as np

# 句読点に、改行コードを追加
filename = './wiki_40b_train.txt'

with open(filename, 'r') as f:
    train_lines = []
    valid_lines = []
    for i, line in enumerate(f):
        if i < 10000:
            train_lines.append(line)
        elif i < 20000:
            valid_lines.append(line)
        else:
            break

with open('./train_data.txt', 'w') as f:
    f.writelines(train_lines)

with open('./valid_data.txt', 'w') as f:
    f.writelines(valid_lines)
