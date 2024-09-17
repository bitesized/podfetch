import feedparser
import json
import structures
import re
import os

# Create new Podcast object
url = "https://feeds.redcircle.com/e30b9f10-8c86-432e-9fa0-ba287fb94e7f"

parsed = feedparser.parse(url)

podcast = structures.Podcast(parsed.feed.title, parsed.feed.description, url)

# Populate Podcast's episodes list
episodes = parsed.entries
episodes.reverse()

for episode in episodes:
    new_episode = structures.Episode(episode.title, episode.description, episode.link)
    podcast.add_episode(new_episode)

# Make subscription's json
podcast_json = json.dumps(podcast.to_dict(), indent=4)

safe_title = re.sub(r'[^\w\s-]', '', podcast.title.lower()).replace(' ', '_')

subscription_dir = os.path.expanduser("~/.podfetch/subscriptions")
os.makedirs(subscription_dir, exist_ok=True)

json_file_path = os.path.join(subscription_dir, f"{safe_title}.json")

with open(json_file_path, "w") as json_file:
    json_file.write(podcast_json)

