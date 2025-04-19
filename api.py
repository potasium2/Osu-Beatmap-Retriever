from ossapi import Ossapi

clientID = 36248
clientSecret = 'kwQ1Jf9vvoRo3DY0pYiGYAsu3ETK0HSLhyNfEXRj'
api = Ossapi(clientID, clientSecret)

beatmapID = api.beatmapset(347136).beatmaps[3].id

print(f"Aim Difficulty: {round(api.beatmap_attributes(beatmapID).attributes.aim_difficulty, 2)}")
print(f"Speed Difficulty: {round(api.beatmap_attributes(beatmapID).attributes.speed_difficulty, 2)}")

print(f"Note Count: {round(api.beatmap_attributes(beatmapID).attributes.max_combo, 2)}")
print(f"Speed Note Count: {round(api.beatmap_attributes(beatmapID).attributes.speed_note_count, 2)}")