import torch
import numpy as np
import random

def set_seed(seed=42):
    """Function to set random seed for torch, numpy and random

    Args: seed [int]: random_seed
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
