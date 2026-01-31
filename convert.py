from PIL import Image

# 读取原始 512x512 图片
img = Image.open("mushroom.png").convert("RGBA")

# 生成 32x32
img_32 = img.resize((32, 32), Image.LANCZOS)
img_32.save("mushroom_32x32.png")

# 生成 192x192
img_192 = img.resize((192, 192), Image.LANCZOS)
img_192.save("mushroom_192x192.png")

print("Icons generated: 32x32 and 192x192")
