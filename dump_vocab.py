from make_vocab import make_vocab

vocab = make_vocab('./pdfs_txts')

with open("vocab_architectures_dissers.txt", "w") as f:
    f.write("<br>".join(vocab))