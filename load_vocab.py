def load_vocab(filename):
    with open(filename, "r") as f:
        data = f.read()
    vocab = data.split("<br>")
    return vocab

#load_vocab("./vocab_architectures_dissers.txt")
