class Rotations:
    def leftrotation(self, x):
        y = x.right
        x.right = y.left
        y.left = x