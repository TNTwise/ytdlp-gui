import argparse
import sys
import os

# other imports
import yt_dlp


class DownloadManager:
    def __init__(
        self,
        url: str,
        output: str,
        mediaType: str,
        resolutionHeight: int,
        getAvailableHeights: bool,
    ):
        super().__init__()
        self.videoContainers = ("mp4", "webm")
        self.audioContainers = ("mp3", "wav")
        self.mediaType = mediaType
        self.url = url
        self.output = output
        self.format = format
        self.resolutionHeight = resolutionHeight
        if getAvailableHeights:
            print(self.getData()[0])
            exit()
        self.download()

    def progress_hook(self, d):
        if d["status"] == "downloading":
            print(
                f"Downloading: {d['_percent_str']} at {d['_speed_str']} ETA: {d['_eta_str']}"
            )
        elif d["status"] == "finished":
            print("Download completed")

    def download(self):
        if self.mediaType.lower() == "video":
            ydl_opts = {
                "format": f"bestvideo[height<={self.resolutionHeight}]+bestaudio/best",
                "progress_hooks": [self.progress_hook],  # Hook for progress reporting
                "quiet": True,
                "no_warnings": True,
            }
        elif self.mediaType.lower() == "audio":
            ydl_opts = {
                "format": "bestaudio/best",
                "progress_hooks": [self.progress_hook],
                "postprocessors": [
                    {  # Convert audio to the desired format
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": self.audioContainers[
                            0
                        ],  # Desired audio codec (e.g., mp3, wav)
                        "preferredquality": "192",  # Desired quality (if applicable)
                    }
                ],
                "quiet": True,
                "no_warnings": True,
            }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
        except yt_dlp.utils.DownloadError:
            print("Cannot download with current settings.")

    def getData(self):
        """
        gets the resolutions and available extensions of the video, returns them as [resolutions,extensions]
        """
        youtubeVideoInfoDict = self.getInfoDictFromURL()
        resolutions = self.getContentFromInfoDict(youtubeVideoInfoDict, "height")
        extensions = self.getContentFromInfoDict(youtubeVideoInfoDict, "ext")
        return [resolutions, extensions]

    def getContentFromInfoDict(self, info_dict, content):
        formats = info_dict.get("formats", [])
        containers = set()
        for format in formats:
            container = format.get(content)  # Get the height of the format
            if container is not None:
                containers.add(container)
        containers = sorted(containers)
        containers.reverse()
        return list(map(str, containers))  # cast every item in here to string

    def getInfoDictFromURL(self) -> dict:
        print("Getting info from youtube video")
        with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
            info_dict = ydl.extract_info(self.url, download=False)
        return info_dict


class Backend:
    def __init__(self):
        args = self.handleArguments()
        dm = DownloadManager(
            url=args.url,
            output=args.output,
            mediaType=args.mediaType,
            resolutionHeight=args.resolutionHeight,
            getAvailableHeights=args.getAvailableHeights,
        )

    def handleArguments(self) -> argparse.ArgumentParser:
        """_summary_

        Args:
            args (_type_): _description_

        """
        parser = argparse.ArgumentParser(
            description="Download videos from youtube",
        )

        parser.add_argument(
            "-u",
            "--url",
            help="url",
            type=str,
            required=True,
        )
        parser.add_argument(
            "-o",
            "--output",
            default=None,
            help="output path to video",
            type=str,
        )
        parser.add_argument(
            "-m",
            "--mediaType",
            default="Video",
            help="Media type (Video or Audio)",
            type=str,
        )
        parser.add_argument(
            "-r",
            "--resolutionHeight",
            default=1080,
            help="This is the max resolution it will download at, and if the video does not support the resolution, it will choose the next highest resolution.",
            type=int,
        )
        parser.add_argument(
            "--getAvailableHeights",
            help="Prints out the available heights of the video",
            action="store_true",
        )

        return parser.parse_args()


if __name__ == "__main__":
    Backend()
