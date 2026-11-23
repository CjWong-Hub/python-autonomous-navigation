# 2D UAV navigation simulator - Stage 1: static grid environment
# Shows an occupancy grid with obstacles, a start cell, a goal cell and a drone.
import pygame

CELL = 40
COLS = 20
ROWS = 15
WIDTH = COLS * CELL
HEIGHT = ROWS * CELL

BACKGROUND = (30, 30, 30)
GRID_COLOR = (60, 60, 60)
OBSTACLE_COLOR = (120, 120, 120)
START_COLOR = (50, 200, 50)
GOAL_COLOR = (230, 200, 50)
DRONE_COLOR = (80, 160, 255)

start = (2, 2)
goal = (17, 12)
obstacles = [(8, 3), (8, 4), (8, 5), (8, 6), (9, 6), (10, 6),
             (12, 9), (13, 9), (14, 9)]

def cell_center(col,row):
    return(col*CELL+CELL//2,row*CELL+CELL//2)

class Drone:
    def __init__ (self,col,row): 
        self.col=col
        self.row=row

    def draw(self,screen):
        center=cell_center(self.col,self.row) 
        pygame.draw.circle(screen,DRONE_COLOR,center,CELL//3) 

def draw_cell(screen,cell,color): 
    rect=pygame.Rect(cell[0]*CELL,cell[1]*CELL,CELL,CELL) 
    pygame.draw.rect(screen,color,rect)

def draw_grid(screen):
    for cols in range(COLS + 1):
        pygame.draw.line(screen, GRID_COLOR,(cols*CELL,0),(cols*CELL,HEIGHT))
    for rows in range(ROWS + 1):
        pygame.draw.line(screen, GRID_COLOR,(0,rows*CELL),(WIDTH,rows*CELL))

def draw_world(screen,drone): 
    screen.fill(BACKGROUND)
    for cell in obstacles:
        draw_cell(screen,cell,OBSTACLE_COLOR) 
    draw_cell(screen,start,START_COLOR)
    draw_cell(screen,goal, GOAL_COLOR)
    draw_grid(screen)
    for drone in drones:
        drone.draw(screen)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UAV Simulator")
clock = pygame.time.Clock()

drones = [Drone(start[0], start[1])]

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_world(screen,drones)
    #draw_world(screen,drone2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()