import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B").cuda()

run = True
while run:
    input_text = input('>> ')
    if input_text in 'q':
        run = False
        break
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to("cuda")

    outputs = model.generate(input_ids)
    print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])
