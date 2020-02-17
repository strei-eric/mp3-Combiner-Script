import os
from subprocess import Popen
from collections import defaultdict

# Sort all the mp3 files into a dictionary of lists.
episode_lists = defaultdict(list)
for filename in os.listdir():
    if ".mp3" in filename and "_" in filename:
        filelist = filename.split("_")
        filelist.pop()
        episode_lists["_".join(filelist)].append(filename)

# Iterate through the dictionary and call a process to combine each episode.
process_list = []
for episode in episode_lists:
    process_list.append(Popen("mp3cat.exe -q -f -o " + episode + ".mp3 " + " ".join(episode_lists[episode])))

# Wait for every process to finish running.
for process in process_list:
    process.communicate()

# Delete all the old files.
for episode in episode_lists:
    for part in episode_lists[episode]:
        os.remove(part)