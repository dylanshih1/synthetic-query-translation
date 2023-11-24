#!/usr/bin/env python3
"""
Trying one or more strategies to convert normal english to search queries 
"""

from __future__ import annotations
import argparse
import logging
from pathlib import Path
from depparser import DependencyParser
from postagger import POSTagger
from utils import CustomAction

log = logging.getLogger(Path(__file__).stem)  # For usage, see findsim.py in earlier assignment.

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description=__doc__)

    # required input file 
    parser.add_argument(
        "input", type=Path, help="Path to file containing input sentences"
    )

    # this is how to add an optional argument
    # add action=CustomAction for features 
    # TODO: prune not implemented yet
    parser.add_argument(
        "-p",
        "--prune",
        type=int,
        help="Remove top __% most frequent words",
        action=CustomAction
    )

    # strategies for filtering by word type 
    # ADJ, ADP, ADV, AUX, CCONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X
    parser.add_argument(
        '-dl',
        '--denylist', 
        nargs='+', 
        help='List of word types to remove from sentences. See https://universaldependencies.org/u/pos/ for possible types',
        action=CustomAction
    )
    parser.add_argument(
        '-al',
        '--allowlist', 
        nargs='+', 
        help='List of word types to keep in sentences. See https://universaldependencies.org/u/pos/ for possible types',
        action=CustomAction
    )
    parser.add_argument(
        '-dp',
        '--depparser', 
        action='store_true',
        help='Keep only syntactic heads (words that other words depend on). See https://stanfordnlp.github.io/stanza/depparse.html',
    )

    # optionally specify output file name 
    parser.add_argument(
        '-o',
        '--output', 
        type=Path,
        help='Specify file name for output sentences',
    )

    # verbosity of logging is controlled by the -v and -q flags
    parser.set_defaults(logging_level=logging.INFO)
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v", "--verbose", dest="logging_level", action="store_const", const=logging.DEBUG
    )
    verbosity.add_argument(
        "-q", "--quiet",   dest="logging_level", action="store_const", const=logging.WARNING
    )
    return parser.parse_args()
    
def store_sentences(input) -> list[str]:
    # read in sentences and store as list
    sentences: list[str] = []
    with open(input) as f:
        for sentence in f.readlines():
            sentence = sentence.strip()
            if sentence != "":  # skip blank lines
                # analyze the sentence
                log.debug(f"Reading sentence: {sentence}")
                sentences.append(sentence)
    return sentences

def main():
    # Parse the command-line arguments
    args = parse_args()
    logging.basicConfig(level=args.logging_level) 
    sentences: list[str]

    # read in sentences and store as list
    sentences = store_sentences(args.input)

    # dependency parser must run on initial sentences 
    if args.depparser: 
        tagger = DependencyParser(sentences)
        tagger.keep_heads()
        sentences = tagger.get_sentences()

    # iterate through parsed arguments in user specified order 
    if 'ordered_args' in args:
        for k,v in args.ordered_args:
            log.debug('This arg is %s %s' % (k, v))
            # ignore input / logging level args  
            if k == 'verbose' or k == 'quiet' or k == 'input' or v == None: 
                continue
            if k == 'denylist': 
                tagger = POSTagger(sentences)
                tagger.remove_types(v)
                sentences = tagger.get_sentences()
            if k == 'allowlist': 
                tagger = POSTagger(sentences)
                tagger.keep_types(v)
                sentences = tagger.get_sentences()

        # TODO: implement each strategy
        # TODO: import each strategy as class 
        # e.g. 
        #   if k == 'prune': 
        #      prune(v)
        # NOTE: take in list[str], return list[str]
        # NOTE: modify sentences in place of reassign; whichever is easier
    
    if args.output != None: 
        # write to output file if specified
        f = open(args.output, "w")
        f.write('\n'.join(sentences))
        f.close()
    else: 
        # else print to console 
        for sentence in sentences: 
            print(sentence)
    
if __name__ == "__main__":
    main()