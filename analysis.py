def convert_audio_features_to_descriptions(audio_features):
    descriptions = {}

    # Acousticness
    if audio_features['acousticness'] < 0.05:
        descriptions['acousticness'] = "The music is highly non-acoustic, characterized by minimal reverberation or natural sound."
    elif audio_features['acousticness'] < 0.2:
        descriptions['acousticness'] = "The music is predominantly non-acoustic, with minimal natural instrument sounds."
    elif audio_features['acousticness'] < 0.5:
        descriptions['acousticness'] = "The music is partially acoustic, featuring a blend of electronic and natural instrument sounds."
    elif audio_features['acousticness'] < 0.8:
        descriptions['acousticness'] = "The music is predominantly acoustic, with prominent natural instrument sounds and reverberations."
    else:
        descriptions['acousticness'] = "The music is highly acoustic, dominated by natural instrument sounds and reverberations."

    # Danceability
    if audio_features['danceability'] < 0.2:
        descriptions['danceability'] = "The music has very low danceability, with a slow tempo and minimal rhythmic elements."
    elif audio_features['danceability'] < 0.4:
        descriptions['danceability'] = "The music has low danceability, with a slower tempo and fewer rhythmic elements suitable for dancing."
    elif audio_features['danceability'] < 0.6:
        descriptions['danceability'] = "The music is moderately danceable, featuring a balanced mix of rhythm and melody conducive to dancing."
    elif audio_features['danceability'] < 0.8:
        descriptions['danceability'] = "The music is highly danceable, with a fast tempo and prominent rhythmic elements ideal for dancing."
    else:
        descriptions['danceability'] = "The music has very high danceability, with an extremely fast tempo and intense rhythmic elements perfect for dancing."

    # Energy
    if audio_features['energy'] < 0.2:
        descriptions['energy'] = "The music has very low energy, characterized by subdued dynamics and a relaxed atmosphere."
    elif audio_features['energy'] < 0.4:
        descriptions['energy'] = "The music has low energy, characterized by calm passages and moderate dynamics."
    elif audio_features['energy'] < 0.6:
        descriptions['energy'] = "The music has moderate energy, featuring a balanced mix of calm and energetic passages."
    elif audio_features['energy'] < 0.8:
        descriptions['energy'] = "The music has high energy, with intense dynamics and a lively, upbeat feel."
    else:
        descriptions['energy'] = "The music has very high energy, with explosive dynamics and an overwhelmingly intense atmosphere."

    # Instrumentalness
    if audio_features['instrumentalness'] < 0.05:
        descriptions['instrumentalness'] = "The music is highly vocal, with minimal or no instrumental accompaniment."
    elif audio_features['instrumentalness'] < 0.2:
        descriptions['instrumentalness'] = "The music is predominantly vocal, with minimal instrumental accompaniment."
    elif audio_features['instrumentalness'] < 0.5:
        descriptions['instrumentalness'] = "The music is partially instrumental, featuring a blend of vocal and instrumental elements."
    elif audio_features['instrumentalness'] < 0.8:
        descriptions['instrumentalness'] = "The music is predominantly instrumental, with vocals playing a minor or absent role."
    else:
        descriptions['instrumentalness'] = "The music is highly instrumental, with minimal or no vocal elements."

    # Liveness
    if audio_features['liveness'] < 0.05:
        descriptions['liveness'] = "The music sounds like a studio recording, lacking the ambiance and spontaneity of a live performance."
    elif audio_features['liveness'] < 0.2:
        descriptions['liveness'] = "The music has low liveness, suggesting a studio recording with minimal live elements."
    elif audio_features['liveness'] < 0.5:
        descriptions['liveness'] = "The music has moderate liveness, suggesting a live performance but with some studio enhancements."
    elif audio_features['liveness'] < 0.8:
        descriptions['liveness'] = "The music sounds like a live recording, capturing the energy and spontaneity of a live performance."
    else:
        descriptions['liveness'] = "The music has very high liveness, with an immersive live atmosphere and audience interaction."

    # Loudness
    if audio_features['loudness'] < -15:
        descriptions['loudness'] = "The music is extremely soft, with barely audible volume levels."
    elif audio_features['loudness'] < -5:
        descriptions['loudness'] = "The music is soft, with low volume levels suitable for background listening."
    elif audio_features['loudness'] < 0:
        descriptions['loudness'] = "The music has moderate volume levels, suitable for general listening enjoyment."
    elif audio_features['loudness'] < 5:
        descriptions['loudness'] = "The music is loud, with high volume levels that may be suitable for energetic listening or parties."
    else:
        descriptions['loudness'] = "The music is extremely loud, with deafening volume levels that may cause discomfort."

    # Speechiness
    if audio_features['speechiness'] < 0.1:
        descriptions['speechiness'] = "The music is purely instrumental, with no vocal content."
    elif audio_features['speechiness'] < 0.3:
        descriptions['speechiness'] = "The music is mostly instrumental, with minimal vocal content."
    elif audio_features['speechiness'] < 0.5:
        descriptions['speechiness'] = "The music features a balanced mix of instrumental and vocal elements."
    elif audio_features['speechiness'] < 0.7:
        descriptions['speechiness'] = "The music is mostly vocal, with instrumental elements playing a supporting role."
    else:
        descriptions['speechiness'] = "The music is highly vocal, with spoken or sung lyrics dominating the composition."

    # Tempo
    if audio_features['tempo'] < 80:
        descriptions['tempo'] = "The music has an extremely slow tempo, characterized by lethargic rhythms and prolonged pauses."
    elif audio_features['tempo'] < 100:
        descriptions['tempo'] = "The music has a slow tempo, characterized by relaxed rhythms and leisurely pacing."
    elif audio_features['tempo'] < 120:
        descriptions['tempo'] = "The music has a moderate tempo, featuring a steady rhythm and balanced pacing."
    elif audio_features['tempo'] < 140:
        descriptions['tempo'] = "The music has a fast tempo, with lively rhythms and energetic pacing."
    else:
        descriptions['tempo'] = "The music has an extremely fast tempo, with frenetic rhythms and rapid pacing."

    # Valence
    if audio_features['valence'] < 0.2:
        descriptions['valence'] = "The music evokes feelings of extreme sadness or melancholy, with deeply introspective melodies and mournful harmonies."
    elif audio_features['valence'] < 0.4:
        descriptions['valence'] = "The music evokes feelings of sadness or melancholy, with introspective melodies and subdued emotional tones."
    elif audio_features['valence'] < 0.6:
        descriptions['valence'] = "The music has a neutral or mixed emotional tone, featuring a balance of positive and negative feelings."
    elif audio_features['valence'] < 0.8:
        descriptions['valence'] = "The music evokes feelings of happiness or contentment, with uplifting melodies and positive emotional tones."
    else:
        descriptions['valence'] = "The music evokes feelings of extreme happiness or euphoria, with exuberant melodies and ecstatic harmonies."

    return descriptions

def describe_audio_features(features):
   
    # Extracting values
    energy = features.get('energy', 0.5)
    valence = features.get('valence', 0.5)
    tempo = features.get('tempo', 120)
    acousticness = features.get('acousticness', 0.5)
    danceability = features.get('danceability', 0.5)
    instrumentalness = features.get('instrumentalness', 0)
    liveness = features.get('liveness', 0.5)
    loudness = features.get('loudness', -60)
    speechiness = features.get('speechiness', 0.5)
    
    descriptions = []

    # Energy
    if energy > 0.75:
        descriptions.append("energetic and powerful")
    elif energy < 0.25:
        descriptions.append("mellow and soft")
    else:
        descriptions.append("a balance of energy")

    # Valence
    if valence > 0.75:
        descriptions.append("positive and cheerful")
    elif valence < 0.25:
        descriptions.append("darker and more introspective")
    else:
        descriptions.append("a mix of emotions")

    # Tempo
    if tempo > 120:
        descriptions.append("fast and upbeat")
    elif tempo < 80:
        descriptions.append("slow and calm")
    else:
        descriptions.append("moderate tempo")

    # Additional features
    if acousticness > 0.5:
        descriptions.append("acoustic and natural")
    if danceability > 0.75:
        descriptions.append("danceable and rhythmic")
    if instrumentalness > 0.5:
        descriptions.append("instrumentally rich")
    if liveness > 0.8:
        descriptions.append("live and vivid")
    if loudness > -5:
        descriptions.append("loud and bold")
    if speechiness > 0.66:
        descriptions.append("wordy and lyrical")
    
    return ", ".join(descriptions)




# Example usage:
'''
audio_features = {'acousticness': 0.3376678260869565, 'danceability': 0.7299130434782609, 'energy': 0.5933043478260869, 'instrumentalness': 0.009693364347826087, 'liveness': 0.17384782608695656, 'loudness': -8.122217391304346, 'speechiness': 0.1391739130434783, 'tempo': 112.84539130434783, 'valence': 0.6449565217391305}
descriptions = convert_audio_features_to_descriptions(audio_features)
for feature, description in descriptions.items():
    print(f"{feature.capitalize()}: {description}")
'''