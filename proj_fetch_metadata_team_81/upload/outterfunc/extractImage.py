from upload.outterfunc.defaultMetadata import default_metadata
from .hachoir import extract_metadata_with_hachoir
from .pillow import extract_image_metadata_with_pillow


def extract_image_metadata(file_type, uploaded_file):
    image_metadata = []

    image_metadata += default_metadata(uploaded_file)

    """
        Hachoir package for extracting metadata does not extract
        metadata of all types of image so i used pillow so that images
        that not support in hachoir will be extracted with pillow package
    """
    # Check to make sure it's a video be we can Extract metadata with pillow
    if file_type != "video" and file_type != "audio":
        extracted_data = extract_image_metadata_with_pillow(
            uploaded_file)
        if extracted_data is not None:
            image_metadata += extracted_data

    # Extract metadata of video, audio and images with hachoir
    extracted_hachoir_data = extract_metadata_with_hachoir(
        uploaded_file)
    if extracted_hachoir_data is not None:
        image_metadata += extracted_hachoir_data

    return image_metadata
