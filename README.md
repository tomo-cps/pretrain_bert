# [Huggingface Transformers] Wiki-40Bデータセットを使ってゼロから日本語BERTの事前学習モデルを構築する

## 0. requirements.txt
```./
pip install -r requirements.txt
```

## 1. データのダウンロード
```./
python dl_data.py
```

まずは，wiki40b/jaのtestに格納されているデータセットをダウンロードし，そのデー\\
タ対して後にデータの分割をする．
- 学習がうまくできるようであれば，データセットを拡大する方針

## 2. 前処理
- ./dataに移動して，wiki_40b_train.txtがダウンロードできているか確認し，以下のコマンドを実行
```./data
chmod u+x preprocess.sh
```
```./data
./preprocess.sh wiki_40b_train.txt
```
- 行末の空白は除去、空白のみの行は削除
- "。” の後が"」"、")“、"）”,“]"だった場合、"。"の後で改行
- "。"で始まる行は削除

=> 前処理後の名前は同じものを使用しているため，更新されている

## 3. データの分割
まずは，wiki_40b_train.txtのそれぞれ1万行を学習データと検証データにする．
```./data
python create_10000.py
```
- train_data.txt と valid_data.txt が生成される

## 4. 事前学習の実行
```./
python my_pretrain.py
```
- ./log直下にlossとepochのグラフが格納される


<img src="/log/output.png" width="70%">
