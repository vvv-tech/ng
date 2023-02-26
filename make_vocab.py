from glob import glob
import os

def make_vocab(txts_dir):
    """
    Function for creating characters vocab from text dir
    """
    texts_combined = ""
    txts_dir = os.path.join(txts_dir, "*")
    txts_filenames = glob(txts_dir)

    for txt_filename in txts_filenames:
        with open(txt_filename, "r", errors="ignore") as f:
            full_text = f.read()
        texts_combined += full_text
    vocab = sorted(list(set(texts_combined)))
    vocab_size = len(vocab)
    print("Vocab size is ", vocab_size)
    print("Vocab is \"", vocab, "\"")
    return vocab

make_vocab("./pdfs_txts/")
