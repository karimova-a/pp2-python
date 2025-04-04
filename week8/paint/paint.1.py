import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'  # Default drawing color
    points = []
    drawing = False
    drawing_start = None
    drawing_rect = False
    color_choose = ['blue', 'red', 'green', 'yellow', 'white']
    color_index = 0
    
    start_rect = None  # Starting position of rectangle drawing
    drawing_rectangle = False  # Flag for rectangle drawing
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Change color mode on key press
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_e:
                    mode = 'eraser'  # Switch to eraser mode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click starts drawing
                    if mode == 'eraser':  # Eraser mode: erase where clicked
                        erase_point(screen, event.pos)
                    else:
                        drawing_start = event.pos  # Store the start position for rectangle or circle
                        points.append((event.pos, mode, radius))  # Add point for pen mode
                elif event.button == 3:  # Right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing_start and mode != 'eraser':  # Continue drawing if the start point is set
                    # Add point while drawing in pen mode
                    if mode != 'eraser':
                        points.append((event.pos, mode, radius))
                        points = points[-256:]

        screen.fill((0, 0, 0))  # Fill the screen with black

        # Draw based on the current mode
        if mode == 'eraser':
            pass  # Eraser mode handled by mousemotion (erase as we move)
        else:
            # Draw all points (pen mode)
            for start, color, rad in points:
                pygame.draw.circle(screen, get_color(color), start, rad)
            
            # Draw shapes if we are in rectangle or circle mode
            if drawing_start:
                if mode == 'rectangle':
                    draw_rectangle(screen, drawing_start, pygame.mouse.get_pos(), mode)
                elif mode == 'circle':
                    draw_circle(screen, drawing_start, pygame.mouse.get_pos(), mode)

        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    """Return the RGB value for a color mode."""
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'yellow':
        return (255, 255, 0)
    elif mode == 'white':
        return (255, 255, 255)
    elif mode == 'eraser':
        return (0, 0, 0)  # Use black for eraser
    return (255, 255, 255)  # Default to white

def draw_rectangle(screen, start, end, color_mode):
    """Draw a rectangle based on the start and end points."""
    color = get_color(color_mode)
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    pygame.draw.rect(screen, color, (start[0], start[1], width, height), 2)  # Draw with outline

def draw_circle(screen, start, end, color_mode):
    """Draw a circle based on the start and end points (distance = radius)."""
    color = get_color(color_mode)
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))  # Calculate the radius
    pygame.draw.circle(screen, color, start, radius, 2)  # Draw circle with outline

def erase_point(screen, position):
    """Erase part of the drawing by drawing over it with black."""
    pygame.draw.circle(screen, (0, 0, 0), position, 15)  # Erase with radius 15

main()


