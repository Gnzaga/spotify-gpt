from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import credentials
import spotify_access
import analysis
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=credentials.openai_api_key)
CORS(app)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data['prompt']
    headers = {
        'Authorization': 'Bearer ' + credentials.openai_api_key,
        'Content-Type': 'application/json',
    }
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    if response.status_code != 200:
        # Log the error response from OpenAI
        print(response.text)
        return jsonify({'error': 'Failed to generate image', 'details': response.text}), response.status_code
    
    image_data = response.json()
    return jsonify(image_data)

#takes song url and calls get_playlist_audio_features_and_top_genres, then formats this request and returns an image of the playlist vibes
@app.route('/generate-playlist-image', methods=['POST'])
def generate_playlist_image():
    data = request.get_json()
    url = data['url']
    sample_word = data['sample_word']

    
    # Assuming spotify_access is defined and works as expected
    feats_genres = spotify_access.get_playlist_audio_features_and_top_genres(url)
    #genres joined by and
    genres_list = feats_genres['top_genres']
    genres = ' and '.join(genres_list)
    features = analysis.describe_audio_features(feats_genres['audio_features'])
    prompt = f"Capture an atmosphere that feels {features}, influenced by the essence of {genres}. The scene is imbued with {sample_word} imagery.  The image reflects the energy and mood associated with the playlist's sound. The visual composition leans on concrete, abstract and symbolic representations to evoke the playlist's vibe and that align with the themes suggested by the user's sample words, all while steering clear of explicit text or words."
    #prompt = f"Envision a landscape that radiates the ambiance and characteristics of {features}, subtly influenced by the thematic undercurrents of {genres}. This scene prioritizes the abstract and the intangible, incorporating {sample_word} themes to craft an immersive experience. Aim to encapsulate the emotional and energetic essence of the playlist. The artwork should have abstract forms and symbolic expressions that convey the playlist's vibe, steering clear of explicit musical symbols or text, to evoke a sense of the intended atmosphere through imaginative and non-literal visual cues."

    print(prompt)


    
    
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        # Adjust according to the actual response structure
        # This assumes response.data contains the image info
        image_data = response.data[0].url  # Or however you access the generated image
        return jsonify({'image_url': image_data})
    except Exception as e:
        # Log the exception details
        print(str(e))
        # Return a generic error message or customize based on exception type
        return jsonify({'error': 'Failed to generate image', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
