from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "mistralai/Mistral-7B-Instruct-v0.2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.float16, device_map="auto"
)

def completion(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7, do_sample=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

