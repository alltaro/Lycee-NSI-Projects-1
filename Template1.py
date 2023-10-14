from PIL import Image, ImageDraw

# Crée une nouvelle image
img = Image.new('RGB', (300, 400), color = (255, 255, 255))
draw = ImageDraw.Draw(img)

# Dessine une tulipe basique
draw.ellipse((100, 100, 200, 300), fill=(255, 0, 0))
draw.polygon([(100, 150), (150, 50), (200, 150)], fill=(0, 255, 0))

# Sauvegarde l'image
img.save('tulipe.png')
