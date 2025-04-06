from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

a = "The weather is nice today"
b = "It’s a sunny and pleasant day"

emb_a = model.encode(a, convert_to_tensor=True)
emb_b = model.encode(b, convert_to_tensor=True)

similarity = util.cos_sim(emb_a, emb_b)
print(similarity)
