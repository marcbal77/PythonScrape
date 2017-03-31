# Exception to be included as necessary
""" Contains all the custom exceptions used. """

#Access Errors
class DirectoryAccessError(Exception):
    """ Exception to be raised when the directory can't be accessed. """
    pass

# Directory Errors
class DirectoryCreateError(Exception):
    """ Exception to be raised when the directory can't be created. """
    pass

# Download Errors
class ImageDownloadError(Exception):
    """ Exception to be raised when the image can't be downloaded. """
    status_code = 0

    def __init__(self, status_code=0):
        # Status code error initiation for when images can't be loaded
        super(ImageDownloadError, self).__init__()
        self.status_code = status_code
# Size Errors
class ImageSizeError(Exception):
    """ Exception to be raised when the image is over the file size. """
    image_size = 0

    def __init__(self, image_size):
        super(ImageSizeError, self).__init__()
        self.image_size = image_size

# Page loading errors
class PageLoadError(Exception):
    """ Exception to be raised when the page can't be loaded. """
    status_code = 0
        # Status_code error initiation for page load problems
    def __init__(self, status_code):
        super(PageLoadError, self).__init__()
        self.status_code = status_code
