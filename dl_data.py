# データセットの取得
import tensorflow_datasets as tfds
# ds_train = tfds.load('wiki40b/ja', split='train')
# ds_valid = tfds.load('wiki40b/ja', split='validation')
ds_test = tfds.load('wiki40b/ja', split='test')

# データセットをテキスト形式で出力する関数
def create_txt(file_name, tf_data):
    start_paragraph = False

    # ファイルの書き込み
    with open(file_name, 'w') as f:
        for wiki in tf_data.as_numpy_iterator():
            for text in wiki['text'].decode().split('\n'):
                if start_paragraph:
                    text = text.replace('_NEWLINE_', '') # _NEWLINE_は削除
                    f.write(text + '\n')
                    start_paragraph = False
                if text == '_START_PARAGRAPH_': # _START_PARAGRAPH_のみ取得
                    start_paragraph = True

# データセットをテキスト形式で出力
create_txt('data/wiki_40b_train.txt', ds_test)
# create_txt('data/wiki_40b_valid.txt', ds_valid)
# create_txt('data/wiki_40b_test.txt', ds_test)