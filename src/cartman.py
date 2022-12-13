from transformers.models.auto.tokenization_auto import AutoTokenizer
from transformers.models.auto.modeling_auto import AutoModelForCausalLM
import torch

#tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
#model = AutoModelForCausalLM.from_pretrained('../southpark/output-medium')

tokenizer = AutoTokenizer.from_pretrained('google/flan-t5-xxl')
model = AutoModelForCausalLM.from_pretrained('google/flan-t5-xxl')

def cartman_speak(user_message):
    new_user_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
    bot_output = new_user_input_ids
    bot_input_ids = torch.cat([new_user_input_ids, bot_output])
    bot_output = model.generate(
        bot_input_ids, max_length= 200,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=.8
    )

    return '{}'.format(tokenizer.decode(bot_output[:,bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
