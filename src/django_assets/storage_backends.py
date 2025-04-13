from storages.backends.s3 import S3Storage
from PIL import Image
import io
import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from typing import Tuple, Optional


class BaseWebPS3Storage(S3Storage):
    """Base storage class with common WebP conversion logic"""
    # Default settings that can be overridden by subclasses
    MAX_DIMENSIONS: Tuple[int, int] = (1920, 1080)  # (width, height)
    QUALITY: int = 80
    ALLOWED_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.webp')
    
    def _convert_to_webp(self, image: Image.Image, quality: Optional[int] = None) -> io.BytesIO:
        """Convert image to WebP format with specified quality"""
        # Convert to RGB if necessary (for PNG with transparency)
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            image = image.convert('RGB')
        
        webp_content = io.BytesIO()
        image.save(
            webp_content, 
            format='WEBP', 
            quality=quality or self.QUALITY
        )
        webp_content.seek(0)
        return webp_content

    def _resize_image(self, image: Image.Image) -> Image.Image:
        """Resize image if it exceeds maximum dimensions"""
        max_width, max_height = self.MAX_DIMENSIONS
        if image.width > max_width or image.height > max_height:
            image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return image
    
    def _process_image(self, name: str, content: io.BytesIO) -> Tuple[str, io.BytesIO]:
        """Process image by resizing and converting to WebP"""
        if not name.lower().endswith(self.ALLOWED_EXTENSIONS):
            return name, content
            
        try:
            image = Image.open(content)
            image = self._resize_image(image)
            content = self._convert_to_webp(image)
            name = f"{os.path.splitext(name)[0]}.webp"
        except Exception as e:
            print(f"Failed to process {self.__class__.__name__} image {name}: {str(e)}")
        
        return name, content
    
    def _save(self, name: str, content: io.BytesIO) -> str:
        """Save the file, processing it if it's an image"""
        name, content = self._process_image(name, content)
        print(f"Saving {name} to S3, {self.QUALITY}, {self.MAX_DIMENSIONS}")
        return super()._save(name, content)

class DefaultWebPS3Storage(BaseWebPS3Storage):
    """Default storage backend for all images"""
    MAX_DIMENSIONS = (1920, 1080)
    QUALITY = 75


class UserAvatarStorage(BaseWebPS3Storage):
    """Storage backend for user avatars"""
    MAX_DIMENSIONS = (240, 200)
    QUALITY = 85

class CategoryImageStorage(BaseWebPS3Storage):
    """Storage backend for category images"""
    MAX_DIMENSIONS = (400, 400)
    QUALITY = 80


class ProductImageStorage(BaseWebPS3Storage):
    """Storage backend for product images"""
    MAX_DIMENSIONS = (1024, 840)
    QUALITY = 75
    