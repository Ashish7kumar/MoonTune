import modal
import requests
from serverless_code import MusicGenServer,app
from schemas import GenerateFromDescriptionRequest,GenerateWithCustomLyricsRequest,GenerateWithDescribedLyricsRequest,GenerateMusicResponseS3,GenerateMusicResponse
@app.local_entrypoint()
def main():
    server = MusicGenServer()
    endpoint_url = server.generate_with_described_lyrics.get_web_url()

    request_data = GenerateWithDescribedLyricsRequest(
        prompt="country, slow, 90BPM",
        described_lyrics="lyrics about indian summer",
        guidance_scale=15
    )
   
    payload = request_data.model_dump()

    response = requests.post(endpoint_url, json=payload)
    response.raise_for_status()
    result = GenerateMusicResponseS3(**response.json())

    print(
        f"Success: {result.s3_key} {result.cover_image_s3_key} {result.categories}")

