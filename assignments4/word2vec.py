# -*- coding: utf-8 -*-
import logging
import multiprocessing
import codecs
from tqdm import tqdm

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':

    program = "train_word2vec_model.py"
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(program))

    infile = "/root/wikiextractor-master/zhwiki/AA/wiki_corpus00"
    vec_outfile1 = "wiki_zh_text_model1"
    vec_outfile2 = "wiki_zh_text_vector1"
    sentences = LineSentence(infile)

    model = Word2Vec(LineSentence(infile), size=100, window=5, min_count=5
                    # workers=multiprocessing.cpu_count(), iter=100
)
    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(vec_outfile1)
    model.wv.save_word2vec_format(vec_outfile2, binary=False)
