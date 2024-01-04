from PIL import Image, ImageEnhance
size = 128
loc=[]
grid=[]
new = Image.new("RGBA", (5*size,5*size))
for i in range(25):				#25 images, all named number.png
	loc.append(str(i+1)+".png")
for i in range(5):				#5 x 5 matrix
	for j in range(5):
		grid.append(size*i)
		grid.append(size*j)

for k in range(25):				#file must be in the same folder as the pictures
	img = Image.open(loc[k])
	new.paste(img, (grid[2*k],grid[2*k+1]))

new.show()
new.save("collage.png")				#safes collage in the same folder 
