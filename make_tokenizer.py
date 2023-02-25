from make_vocab import make_vocab

def make_encoder(vocab):
    """
    Function for creating function instance that takes char list and returns int list according to vocab
    """
    stoi = {char:i for i, char in enumerate(vocab)}
    return lambda str_: [stoi[letter] for letter in str_]

def make_decoder(vocab):
    """
    Function for creating function instance that takes int list and returns char list according to vocab
    """
    itos = {i:char for i, char in enumerate(vocab)}
    return lambda nums: [itos[num] for num in nums]


## test
#vocab = make_vocab('./pdfs_txts')
#encode = make_encoder(vocab)
#decode = make_decoder(vocab)

#print(encode("Привет, мир!"))
#print(decode([34,24,50,33,104,265]))
