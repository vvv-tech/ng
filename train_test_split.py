import random

random.seed(17)

def train_test_split_fp(filepaths, test_ratio=0.1):
    k = len(filepaths)
    shuffled_filepaths = random.choices(filepaths, k=k)
    n = int(k * test_ratio)
    test_filepaths = shuffled_filepaths[:n]
    train_filepaths = shuffled_filepaths[n:]
    return (train_filepaths, test_filepaths)

#from glob import glob
#fileps = glob("pdfs_txts/*")
#train_filepaths, test_filepaths = train_test_split_fp(fileps)
#print(len(fileps), len(train_filepaths), len(test_filepaths))
