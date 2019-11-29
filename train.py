import gpt_2_simple as gpt2
from datetime import datetime

gpt2.download_gpt2(model_name="1558M")

file_name = "delimited.txt"

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              model_name='1558M',
              steps=500000,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=100,
              save_every=500
              )
