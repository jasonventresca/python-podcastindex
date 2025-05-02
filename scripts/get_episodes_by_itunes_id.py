#! /usr/bin/env python

# Run with:
#   $ poetry env activate
#   $ python -m scripts.generate_random_episodes

import json
import random
import argparse

import podcastindex

def main(itunes_id):
    config = podcastindex.get_config_from_env()
    index = podcastindex.init(config)

    results = index.episodesByItunesId(
        itunesId=itunes_id,
        max_results=1,
    )
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("itunes_id", type=int)
    args = parser.parse_args()

    main(itunes_id=args.itunes_id)
