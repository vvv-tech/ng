import torch
import torch.nn as nn
from torch.nn import functional as F

torch.manual_seed(17)

class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets):
        logits = self.token_embedding_table(idx) # (dim (B) batch_size, (T) block_size, (C) vocab_size)

        # making dim according to input format of pytorch
        B, T, C = logits.shape
        logits = logits.view(B*T, C)
        targets = targets.view(B*T)

        loss = F.cross_entropy(logits, targets)

        return logits, loss

