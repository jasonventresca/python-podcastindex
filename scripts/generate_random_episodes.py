#! /usr/bin/env python

# Run with:
#   $ poetry env activate
#   $ python -m scripts.generate_random_episodes

import json
import random
import os.path

import podcastindex

def write_results_to_random_file(results):

    # Generate random number between 1 and 1000, formatted as 4 digits
    n = random.randint(1, 1000)
    filename = f"randomEpisodes-{n:04d}.json"

    # Write results to file
    data_dir = os.path.expanduser("~/dev/podcast-sharing-app/backend-api/sample-data")
    with open(os.path.join(data_dir, filename), 'w') as f:
        json.dump(results, f, indent=4)

    return filename

def main():
    config = podcastindex.get_config_from_env()
    index = podcastindex.init(config)

    results = index.randomEpisodes(max=1_000, lang="en")
    write_results_to_random_file(results)

if __name__ == "__main__":
    main()
