import torch
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cdist as scipy_cdist


torch_device='cuda' if torch.cuda.is_available() else 'cpu'
df=pd.read_csv('game_req.csv')
encoder = SentenceTransformer( 'paraphrase-MiniLM-L6-v2',device=torch_device)
plot_embeddings = encoder.encode(df.name.tolist(),device=torch_device)

def chat_gameR(text):
    game=text
    game_emb=encoder.encode([game],device=torch_device)
    similarities = 1 - scipy_cdist(game_emb,plot_embeddings,'cosine' )
    best_sim_idx = np.argmax(similarities[0])
    most_similar_title = df.loc[best_sim_idx,'name']
    most_similar_plot = df.loc[best_sim_idx].Requirement
    most_similar_title_sim = similarities[0]. max()
    # print(most_similar_title)
    # print('\n')
    # print(most_similar_plot)
    return most_similar_plot