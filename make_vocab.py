from glob import glob
import random
import os

random.seed(17)

def make_vocab(txts_dir):
    texts_combined = ""
    txts_dir = os.path.join(txts_dir, "*")
    txts_filenames = glob(txts_dir)
    # only need one tenth selected randomly
    needed_k = len(txts_filenames) // 10
    random.choices(txts_filenames, k=needed_k)

    for txt_filename in txts_filenames:
        with open(txt_filename, "r", errors="ignore") as f:
            full_text = f.read()
        texts_combined += full_text
    vocab = sorted(list(set(texts_combined)))
    vocab_size = len(vocab)
    print("Vocab size is ", vocab_size)
    print("Vocab is \"", vocab, "\"")
    return vocab

#make_vocab("./pdfs_txts/")
