CELL_SIZE = 50
WIN_WIDTH = 1200
WIN_HEIGHT = 800
FPS = 60

TEXT_COLOR = (0,255,255)
#permet d'aligner comme il faut sur une grille invisible le serpent et le fruit, pour éviter qu'ils soient décalés lorsqu'ils se superposent
def align_elements(x, y, cell_size):
    aligned_x = (x // cell_size) * cell_size
    aligned_y = (y // cell_size) * cell_size
    return aligned_x, aligned_y

