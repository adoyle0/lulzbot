import torch
from transformers.models.t5.tokenization_t5 import T5Tokenizer 
from transformers.models.t5.modeling_t5 import T5ForConditionalGeneration

device = torch.device("cuda")
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl").cuda()

run = True
while run:
    input_text = input('>> ')
    if input_text in 'q':
        run = False
        break
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids)
    print(tokenizer.decode(outputs[0]))
