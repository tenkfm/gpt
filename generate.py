import os

# Specify the directory containing images
images_url = "https://tenkfm.github.io/gpt/images/"
image_folder = './images'
output_html = 'index.html'

# Get list of image files (jpg, png, gif, etc.)
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')
images = [f for f in os.listdir(image_folder) if f.lower().endswith(image_extensions)]

# Start creating the HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }
        .gallery img {
            margin: 10px;
            border: 2px solid #ccc;
            max-width: 300px;
            max-height: 300px;
        }
    </style>
</head>
<body>
    <div class="gallery">
'''

# Loop through all images and add them to the HTML content
for image in images:
    img_path = os.path.join(images_url, image)
    html_content += f'        <img src="{img_path}" alt="{image}">\n'

# Close the HTML tags
html_content += '''
    </div>
</body>
</html>
'''

# Write the HTML content to a file
with open(output_html, 'w') as f:
    f.write(html_content)

print(f"HTML page generated: {output_html}")

