import tkinter as tk
from PIL import Image, ImageTk

class BingoPositionDetector:
    def __init__(self, image_path):
        self.root = tk.Tk()
        self.root.title("Bingo Position Detector")

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.root, width=self.image.width, height=self.image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.canvas.bind("<Button-1>", self.on_click)

        self.positions = []

    def on_click(self, event):
        x, y = event.x, event.y
        print(f"Clicked at position: ({x}, {y})")
        self.positions.append((x, y))
        
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
        
        if len(self.positions) == 25:
            print("\nAll 25 positions:")
            for i, pos in enumerate(self.positions):
                print(f"Position {i+1}: {pos}")
            self.root.quit()

    def run(self):
        self.root.mainloop()

# Usage
detector = BingoPositionDetector("bingo-g.jpg")
detector.run()