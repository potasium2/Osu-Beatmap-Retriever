from ossapi import Ossapi

clientID = 36248
clientSecret = 'kwQ1Jf9vvoRo3DY0pYiGYAsu3ETK0HSLhyNfEXRj'
api = Ossapi(clientID, clientSecret)

# TODO:
# Loop through maps starting at like idk 2015-2017 or so
# Check if beatmap is ranked, if not then skip it
# If beatmap is ranked filter it based on the rules.txt
# Save all relevant data (Song Title, Difficulty Name, setID, difficultyID, Star Rating) to an object list
# Export that list as json data
# I'll quick test on like 25-50 maps depending on slow this is (I also may switch to an async structure we'll see)

# Starting Base:
beatmapID = api.beatmapset(347136).beatmaps[3].id

print(f"Aim Difficulty: {round(api.beatmap_attributes(beatmapID).attributes.aim_difficulty, 2)}")
print(f"Speed Difficulty: {round(api.beatmap_attributes(beatmapID).attributes.speed_difficulty, 2)}")

print(f"Note Count: {round(api.beatmap_attributes(beatmapID).attributes.max_combo, 2)}")
print(f"Speed Note Count: {round(api.beatmap_attributes(beatmapID).attributes.speed_note_count, 2)}")