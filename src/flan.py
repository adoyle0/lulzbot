import torch
from transformers.models.t5.tokenization_t5_fast import T5TokenizerFast 
from transformers.models.t5.modeling_t5 import T5ForConditionalGeneration

tokenizer = T5TokenizerFast.from_pretrained("google/flan-t5-xl")
device = torch.device('cuda')
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl")
model = model.to(device)

def flan_speak(user_message):
    input_ids = tokenizer(user_message, return_tensors='pt').input_ids.to('cuda')
    user_input_word_count = len(user_message.split(' '))

    if user_input_word_count * user_input_word_count > 100:
        min_tokens = 100
    else:
        min_tokens = user_input_word_count * 2

    bot_output = model.generate(
        input_ids, 
      # min_length               = min_tokens,
        max_new_tokens           = 350,
        num_beams                = 16,
        num_beam_groups          = 8,
        no_repeat_ngram_size     = 3,
        length_penalty           = 1.4,
        diversity_penalty        = 0.0,
        repetition_penalty       = 2.1,
        early_stopping           = True,

      # do_sample                = True,
      # top_k                    = 256,
      # top_p                    = 0.92,
      # temperature              = 0.4,
    )

    output = tokenizer.batch_decode(bot_output, skip_special_tokens=True)[0]
    return output[:2000]
