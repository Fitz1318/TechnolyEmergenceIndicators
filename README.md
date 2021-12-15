# Unsupervised Keyphrase Extraction
This is code for EMNLP 2021 paper: [Unsupervised Keyphrase Extraction by Jointly Modeling Local and Global Context](https://arxiv.org/abs/2109.07293).


## requirements
- transformers
- nltk
- pytorch
- tqdm

## Runing
Step 1: obtain embeddings of candidate phrases and the whole document.
```shell
python get_embedding.py --file_path [data_path] --file_name [file_name] --model_name [pretrained model name/path]
```

Step 2: extract keyphrases
```shell
python src/ranker.py [data_path] [model_name]
```



