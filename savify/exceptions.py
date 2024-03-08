class SavifyError(Exception):
    def __init__(self, message='Savify ran into an error!'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class FFmpegNotInstalledError(SavifyError):
    def __init__(self, message='FFmpeg must be installed to use Savify! [https://ffmpeg.org/download.html]'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class SpotifyApiCredentialsNotSetError(SavifyError):
    def __init__(self, message='the API credentials this app needs are no longer valid, if you see this message this app will no longer work.'
                '\ntalk to nath for a new version.'
                 ):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class UrlNotSupportedError(SavifyError):
    def __init__(self, url, message='The URL entered is invalid, make sure it is a valid spotify PUBLIC playlist.'):
        self.url = url
        self.message = f'{message} [{self.url}]'
        super().__init__(self.message)

    def __str__(self):
        return self.message


class YoutubeDlExtractionError(SavifyError):
    def __init__(self, message='YoutubeDl failed to download the song!'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InternetConnectionError(SavifyError):
    def __init__(self, message='Connection timed out, check you have a stable internet connection!'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
