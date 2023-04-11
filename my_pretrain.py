from transformers import BertConfig
from transformers import BertForMaskedLM
from transformers import LineByLineTextDataset
from transformers import DataCollatorForLanguageModeling
from transformers import AlbertTokenizer
from transformers import TrainingArguments
from transformers import Trainer
import matplotlib.pyplot as plt
import scienceplots
import matplotlib
matplotlib.get_cachedir()

plt.style.use(['science', 'ieee', 'no-latex'])
matplotlib.rc('font', family='times new roman')
# plt.style.use(['science','ieee','no-latex'])

data_dir = "./data/"

tokenizer = AlbertTokenizer.from_pretrained(data_dir+'wiki40b_sentencepiece.model', keep_accents=True)
config = BertConfig(vocab_size=32003, num_hidden_layers=12, intermediate_size=768, num_attention_heads=12)
model = BertForMaskedLM(config)

dataset = LineByLineTextDataset(
     tokenizer=tokenizer,
     file_path=data_dir + 'corpus/train_data.txt',
     block_size=256,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, 
    mlm=True,
    mlm_probability= 0.15
)

training_args = TrainingArguments(
    output_dir= data_dir + 'SousekiBERT/',
    overwrite_output_dir=True,
    num_train_epochs=1000,
    per_device_train_batch_size=32,
    save_steps=10000,
    save_total_limit=2,
    prediction_loss_only=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)

trainer.train()

epoch_lst = []
loss_lst = []
for log in trainer.state.log_history:
    try:
        loss_lst.append(log['loss'])
        epoch_lst.append(log['epoch'])
    except KeyError:
        pass


fig, ax = plt.subplots()
ax.plot(epoch_lst, loss_lst)
ax.set_xlabel('epoch')
ax.set_ylabel('loss')
plt.savefig("log/output.png")

trainer.save_model('wiki40b_BERT/')
