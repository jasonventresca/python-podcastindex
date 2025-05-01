import logging

import podcastindex

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def write_results_to_random_file(results):
    import json
    import random
    import os.path

    # Generate random number between 1 and 1000, formatted as 4 digits
    n = random.randint(1, 1000)
    filename = f"randomEpisodes-{n:04d}.json"

    # Write results to file
    data_dir = os.path.expanduser("~/dev/podcast-sharing-app/backend-api/sample-data")
    with open(os.path.join(data_dir, filename), 'w') as f:
        json.dump(results, f, indent=4)

    return filename

def test_random_episodes():
    config = podcastindex.get_config_from_env()
    index = podcastindex.init(config)

    results = index.randomEpisodes(max=1_000, lang="en")
    write_results_to_random_file(results)
    return

    # Basic test
    results = index.randomEpisodes(max=1)
    assert len(results["episodes"]) == 1, "Expected exactly one episode."

    # Test that changing the `max` parameter impacts the number of episodes returned
    results = index.randomEpisodes(max=3)
    assert len(results["episodes"]) == 3, "Expected exactly three episodes."
