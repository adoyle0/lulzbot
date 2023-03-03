from transformers.models.auto.modeling_auto import AutoModelForCausalLM
from transformers.models.auto.tokenization_auto import AutoTokenizer
import requests
import json

url = 'https://doordesk.net/chat'


def cartman_respond(user_message):
    message = {'Message': user_message}
    response = requests.post(url, json.dumps(message))
    return response.json().get('Cartman')


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained(
    "../cartman/train/cartman/models/output-medium-3ep")


def cartman_speak(input_text):
    input_ids = tokenizer(input_text + tokenizer.eos_token,
                          return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=200,
        num_beams=8,
        num_beam_groups=4,
        no_repeat_ngram_size=3,
        length_penalty=1.4,
        diversity_penalty=0,
        repetition_penalty=2.1,
        early_stopping=True,

        # do_sample = True,
        # top_k = 100,
        # top_p = 0.7,
        # temperature = 0.8,
    )
    return tokenizer.decode(outputs[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
