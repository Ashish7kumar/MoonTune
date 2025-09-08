import requests
from Backend.src.serverless_code import MusicGenServer
from Backend.src.schemas import GenerateWithDescribedLyricsRequest,GenerateMusicResponseS3
from Backend.src import app

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

    response = requests.post(endpoint_url, json=payload)#type:ignore
    response.raise_for_status()
    result = GenerateMusicResponseS3(**response.json())

    print(
        f"Success: {result.s3_key} {result.cover_image_s3_key} {result.categories}")

