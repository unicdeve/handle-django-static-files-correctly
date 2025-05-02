# Handling Django Static Files and User Uploaded Files

This project demonstrates how to efficiently handle Django static files and user
uploaded files in a web application. It shows how to:

- Serve website files (like CSS and JavaScript) quickly and efficiently
- Handle user-uploaded images
- Optimize images for web use by converting them to WebP format
- Store images securely in the cloud

## What's Special About This Project?

This demo showcases modern best practices for handling images in web
applications:

1. **Fast Website Loading**: Uses WhiteNoise to serve website files quickly
2. **Smart Image Processing**: Automatically converts uploaded images to WebP
   format, which:
   - Reduces file size significantly
   - Maintains high image quality
   - Improves website loading speed
3. **Secure Cloud Storage**: Stores images in Amazon S3, ensuring:
   - Reliable storage
   - Easy access
   - Scalability

## Learn More

For a detailed technical explanation of how this works, check out the blog post:
[Link to Blog Post](https://unicdev.hashnode.dev/django-assets-management-best-practices)

## Project Structure

The demo is organized into three main parts:

- User model: avatar images resized and converted to WebP format before being
  stored in S3
- Category model: category images resized and converted to WebP format before
  being stored in S3
- Product model: product images resized and converted to WebP format before
  being stored in S3

This structure makes it easy to understand how different parts of a web
application work together to handle images efficiently.
