from ossapi import Ossapi, GameMode
import json

# Client Stuff
# If you are using this for personal use then create your own ID and Secret
# You can do so here: https://osu.ppy.sh/home/account/edit#oauth
clientID = 36248
clientSecret = 'kwQ1Jf9vvoRo3DY0pYiGYAsu3ETK0HSLhyNfEXRj'
api = Ossapi(clientID, clientSecret)

def BeatMapFetcher(startingID, maximumID):
    beatmapID = startingID # Clarity
    while beatmapID < maximumID:
        beatmapID += 1 # So we don't get stuck in after a continue block

        # Check if the beatmap actually exists
        try:
            beatmapset = api.beatmapset(beatmapID)
        except:
            print(f"Could not find beatmap at {beatmapID}, continuing to next beatmap.")
            continue

        for beatmap in beatmapset.beatmaps:
            # I'll probably either implement other Game Mode functionality OR make them separate calculators
            if beatmap.mode != GameMode.OSU or beatmap.ranked.value != 1:
                continue

            CalculateMapType(beatmapset, beatmap)

        print(f"Beatmap #{beatmapID} Returns good, continuing to next beatmap.")

aimMaps = []
speedMaps = []
staminaMaps = []
hybridMaps = []
consistencyMaps = []
def CalculateMapType(mapset, beatmap):
    maxCombo = api.beatmap_attributes(beatmap.id).attributes.max_combo
    aimDifficulty = api.beatmap_attributes(beatmap.id).attributes.aim_difficulty
    speedDifficulty = api.beatmap_attributes(beatmap.id).attributes.speed_difficulty
    speedNoteCount = api.beatmap_attributes(beatmap.id).attributes.speed_note_count

    # SongTitle, DiffTitle, setID, diffID, starRating
    beatMapObj = {
        "songTitle": mapset.title,
        "difficultyTitle": beatmap.version,
        "setID": mapset.id,
        "difficultyID": beatmap.id,
        "difficulty": api.beatmap_attributes(beatmap.id).attributes.star_rating
    }

    if aimDifficulty > speedDifficulty + 0.5:
        print(f"Aim Map: {beatmap.version}")
        aimMaps.append(beatMapObj)
    elif speedNoteCount > maxCombo * 0.2:
        print(f"Stamina Map: {beatmap.version}")
        speedMaps.append(beatMapObj)
    elif speedDifficulty > aimDifficulty + 0.5 and speedNoteCount > maxCombo * 0.1:
        print(f"Speed Map: {beatmap.version}")
        speedMaps.append(beatMapObj)
    elif abs(aimDifficulty - speedDifficulty) < 0.5 and speedNoteCount > maxCombo * 0.1:
        print(f"Hybrid Map: {beatmap.version}")
        hybridMaps.append(beatMapObj)
    else:
        print(f"Consistency Map: {beatmap.version}")
        consistencyMaps.append(beatMapObj)

# Starting in ~April 2015 -- Ending in ~April 2025
BeatMapFetcher(300033, 2347113)
allBeatMaps = {
    "aimMaps": aimMaps, 
    "speedMaps": speedMaps, 
    "staminaMaps": staminaMaps, 
    "hybridMaps": hybridMaps, 
    "consistencyMaps": consistencyMaps
}

# Write beatmaps to file.
filename = "beatmaps.json"
with open(filename, 'w') as file:
    json.dump(allBeatMaps, file, indent = 4)