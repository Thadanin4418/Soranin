import requests
import os

class FacebookReelsUploader:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v10.0/me/videos"

    def upload_video(self, video_path, title, description):
        with open(video_path, 'rb') as video_file:
            files = {
                'file': video_file,
                'access_token': self.access_token,
                'title': title,
                'description': description
            }
            response = requests.post(self.base_url, files=files)
            return response.json()

# Example Usage:
if __name__ == '__main__':
    uploader = FacebookReelsUploader('YOUR_ACCESS_TOKEN')
    response = uploader.upload_video('path/to/video.mp4', 'My Reel Title', 'My Reel Description')
    print(response)