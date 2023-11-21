import pygame, sys
pygame.init()

# DEFINIR COLORES
black =(0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

ventana=(600,800)

# CREAR VENTANA
screen=pygame.display.set_mode(ventana)

while True:
    for event in pygame.event.get():
        # print(event)---->se pueden ver los eventos dentro de la ventana
        if event.type==pygame.QUIT:
            sys.exit()

    #VERIFICAR QUE LA TECLA Q ESTÉ PRESIONADA
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        sys.exit()

    #Color de fondo
    screen.fill(black)
    ###-----zona de dibujo
    pygame.draw.line(screen, green, [0,100], [100,100], 5)



    ###-----zona de dibujo
    #actualizar pantalla
    pygame.display.flip()
