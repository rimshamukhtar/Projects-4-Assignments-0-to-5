# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 30

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser (Tkinter Version)")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='lightgray')
        self.canvas.pack()

        self.cells = []  # Store cell references
        self.create_grid()

        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        """Create blue grid cells with black borders"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill='blue', outline='black'
                )
                self.cells.append(cell)

    def create_eraser(self, event):
        """Create eraser on mouse click"""
        if self.eraser is None:
            x, y = event.x, event.y
            self.eraser = self.canvas.create_rectangle(
                x, y, x + ERASER_SIZE, y + ERASER_SIZE,
                fill='pink', outline='black'
            )

    def move_eraser(self, event):
        """Move eraser with mouse and erase touched cells"""
        if self.eraser is not None:
            # Move eraser to new position
            x, y = event.x, event.y
            self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

            # Check for overlaps and erase cells
            overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
            for obj in overlapping:
                if obj in self.cells:
                    self.canvas.itemconfig(obj, fill='white')


def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
