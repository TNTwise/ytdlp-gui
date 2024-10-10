import argparse
import sys
import os

# other imports
import yt_dlp
import yt_dlp.version

thisdir = os.getcwd()

class DownloadManager:
    def __init__(
        self,
        url: str,
        output: str,
        mediaType: str,
        resolutionHeight: int,
        getAvailableHeights: bool,
        printVersion: bool,
    ):
        super().__init__()
        self.videoContainers = ("mp4", "webm")
        self.audioContainers = ("m4a", "wav")
        self.mediaType = mediaType
        self.url = url
        self.output = output
        self.format = format
        self.resolutionHeight = resolutionHeight
        self.getAvailableHeights = getAvailableHeights
        self.printVersion = printVersion

        self.inputValidation()
        self.download()
        self.moveFileToOutputFolder()
    def moveFileToOutputFolder(self):
        for file in os.listdir(thisdir):
            if self.title in file:
                print(os.path.join(self.output, file))
                os.rename(file, os.path.join(self.output, file))

    

    def inputValidation(self):
        res,ext,self.title = self.getData()
        
        if self.getAvailableHeights:
            print(res)
            exit()
        if self.printVersion:
            print(yt_dlp.version.__version__)
            exit()
        if self.url is None:
            print("Please provide a url")
            exit()
        

    def progress_hook(self, d):
        if d["status"] == "finished":
            print("\nDownload completed")

    def download(self):
        if self.mediaType.lower() == 'video':
            ydl_opts = {
                'format': f'bestvideo[height<={self.resolutionHeight}]',
                'progress_hooks': [self.progress_hook],  # Hook for progress reporting
                'quiet': True,
                'no_warnings': True,
            }
        elif self.mediaType.lower() == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'progress_hooks': [self.progress_hook],
                'postprocessors': [{  # Convert audio to the desired format
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': self.audioContainers[0],  # Desired audio codec (e.g., mp3, wav)
                }],
                'quiet': True,
                'no_warnings': True,
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
        title = youtubeVideoInfoDict["fulltitle"]
        return [resolutions, extensions, title]

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
            printVersion=args.version,
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
            default=None,
        )
        parser.add_argument(
            "-o",
            "--output",
            default=os.getcwd(),
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
        parser.add_argument(
            "-v",
            "--version",
            action="store_true",
            help="Prints the version of the program and exits",
        )
        return parser.parse_args()


if __name__ == "__main__":
    Backend()
