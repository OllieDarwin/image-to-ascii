from PIL import Image

characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."[::-1]

def convert (path, file_type, output_file, scale):
    scale = int(scale)
    output = open(output_file, "a+")
    
    img = Image.open(f"{path}.{file_type}")
    img = img.convert('L')
    width, height = img.size
    
    img = img.resize((width//scale, height//scale))
    width, height = img.size

    grid = []
    for i in range(height):
        grid.append(["0"] * width)

    pixels = img.load()

    for y in range(height):
        for x in range(width):
            grid[y][x] = characters[int((pixels[x,y]/255)*len(characters))-1]

    ascii_art = open(output_file, "w")
    for row in grid:
        ascii_art.write("".join(row)+"\n")

    ascii_art.close()
    
if __name__ == "__main__":
    convert("monalisa", "jpg", "monalisa.txt", 5)
