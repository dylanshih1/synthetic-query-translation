#!/usr/bin/env python3
"""
Trying one or more strategies to convert normal english to search queries 
"""

from __future__ import annotations
import argparse
import logging
from pathlib import Path

log = logging.getLogger(Path(__file__).stem)  # For usage, see findsim.py in earlier assignment.

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description=__doc__)

    # required input file 
    parser.add_argument(
        "input", type=Path, help="Path to file containing input sentences"
    )

    # this is how to add an optional argument
    # TODO: prune not implemented yet
    parser.add_argument(
        "-p",
        "--prune",
        type=int,
        help="Remove top __% most frequent words",
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

    # iterate through parsed arguments in user specified order 
    for k,v in args.__dict__.items():
        log.debug('This arg is %s %s' % (k, v))
        # ignore input / logging level args  
        if k == 'verbose' or k == 'quiet' or k == 'input': 
            continue
        # TODO: implement each strategy
        # TODO: import each strategy as class 
        # e.g. 
        #   if k == 'prune': 
        #      prune(v)
        # NOTE: take in list[str], return list[str]
        # NOTE: modify sentences in place of reassign; whichever is easier
    
    # print out modified sentences
    for sentence in sentences: 
        print(sentence)

if __name__ == "__main__":
    main()