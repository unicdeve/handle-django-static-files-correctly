# Image Processing and Storage Demo - Technical Documentation

This project demonstrates the implementation of efficient image handling in
Django using WhiteNoise for static files and Amazon S3 for media storage, with
automatic WebP conversion.

## Technical Stack

- Django 5.2
- WhiteNoise 6.9.0 (for static files)
- django-storages 1.14.6 (for S3 integration)
- Pillow 11.2.1 (for image processing)
- boto3 1.37.33 (AWS SDK)
- python-dotenv 1.1.0 (for environment variables)

## Prerequisites

- Python 3.8+
- AWS Account with S3 bucket
- AWS Access Key and Secret Key

## Environment Setup

1. Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name
```

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

```
.
├── apps/
│   ├── account/      # User management
│   ├── category/     # Category management
│   └── product/      # Product management
├── django_assets/    # Project settings
├── requirements.txt  # Project dependencies
├── .env.example      # Environment variables example
├── .python-version   # Python version - managed by pyenv
├── staticfiles/      # Collected static files (development only)
```

## Key Features

### Static Files Handling

- WhiteNoise middleware for efficient static file serving
- Compressed and cached static files
- Manifest-based file versioning

### Media Files Processing

- Automatic WebP conversion of uploaded images
- Custom storage backend for S3 integration
- Image optimization before upload

### AWS S3 Integration

- Secure file storage in S3
- Custom storage backend implementation
- Environment-based configuration

## Development Workflow

1. Make changes to models in respective apps
2. Create and apply migrations
3. Test image upload functionality
4. Verify WebP conversion
5. Check S3 upload success

## Testing

To test the image processing:

1. Upload an image through the admin interface
2. Check the S3 bucket for the converted WebP file
3. Verify the image quality and file size reduction

## Production Deployment

For production:

1. Set `DEBUG=False` in environment variables
2. Configure proper `ALLOWED_HOSTS`
3. Use a production-grade database
4. Set up proper AWS IAM permissions
5. Configure proper static file serving

## Related Blog Post

For a detailed explanation of the implementation, check out the blog post:
[Link to Blog Post](https://hashnode.com/draft/67fbf4dcb76f2f86444f6fb3)
