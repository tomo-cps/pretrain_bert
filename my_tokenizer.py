from sentencepiece import SentencePieceTrainer

data_dir = "./data/"

SentencePieceTrainer.Train(
    '--input='+data_dir+'corpus/wiki_40b_train.txt, --model_prefix='+data_dir+'wiki40b_sentencepiece --character_coverage=0.9995 --vocab_size=32000 --pad_id=3 --add_dummy_prefix=False'
)