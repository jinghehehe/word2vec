# 预处理wiki.bz2数据 ——> wiki.txt
# Author: Jing Feng
# Prompt： code in Python3 env


from __future__ import print_function
import logging
import time
import os
import six
import sys

from gensim.corpora import WikiCorpus
from optparse import OptionParser
from const import data_dir ,cache_dir

# 将zhwiki.xml.bz2 -> zhwiki.txt
def parse_corpus(input_file , output_file):
    space = ' '
    i = 0
    with open(output_file, 'w' , encoding='utf-8') as fout:
        wiki = WikiCorpus(input_file, lemmatize=False , dictionary= {})
        for text in wiki.get_texts():
            if six.PY3:
                #data = space.join(text)
                #output.write(str(data) + '\n')
                fout.write(space.join(text) + '\n')
            else:
                fout.write(space.join(text) + "\n")
            i += 1
            if i % 10000 == 0:
                logger.info('{t} *** {i} \t docs has been dealed'.
                        format(i = i, t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
    #logger.info("Finished Saved " + str(i) + " articles")

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
    logger.info("running %s" % ' '.join(sys.argv))
    #logger.info('running ' + program + ': parse the chinese corpus')

    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input_file',
    default= os.path.join(data_dir, 'zhwiki-20191120-pages-articles-multistream.xml.bz2'),
    help = 'input:Wiki corpus')
    parser.add_option('-o', '--output', dest='output_file',
    default=os.path.join(cache_dir, 'wiki.zh.txt'), help='output:Wiki corpus')

    (options, args) = parser.parse_args()
    input_file = options.input_file
    output_file = options.output_file

    try:
        start = time.time()
        parse_corpus(input_file, output_file)
       # logger.info('*** {i} \t docs has been dealed'.format(i=i))
        end = time.time()
        print('total spent times:%2.f' % (end-start)+ ' s')
    except Exception as err:
        logger.info(err)
    # check and process input arguments
    #if len(sys.argv) != 3:
    #    print("Using: python process_wiki.py enwiki.xxx.xml.bz2 wiki.en.text")
     #   sys.exit(1)
    #inp, outp = sys.argv[1:3]


