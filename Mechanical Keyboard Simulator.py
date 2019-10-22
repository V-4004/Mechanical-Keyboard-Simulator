import pygame

# icon source - needpix.com - url - https://www.needpix.com/photo/download/20462/uppercase-symbol-icon-free-vector-graphics-free-pictures-free-photos-free-images-royalty-free

pygame.mixer.pre_init(22050, -16, 1, 256)
pygame.mixer.init()
pygame.init()

icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('MECHANICAL KEYBOARD SIMULATOR')
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

myFont = pygame.font.Font('fonts\FiraMono-Regular.otf', 200)
myFont1 = pygame.font.Font('fonts\Gotham-Light.otf', 25)
color = (255, 255, 255)

D1 = pygame.mixer.Sound("sounds\D (1).wav")

U1 = pygame.mixer.Sound(r"sounds\U (1).wav")

BSPD1 = pygame.mixer.Sound("sounds\BSPD (1).wav")

BSPU1 = pygame.mixer.Sound("sounds\BSPU (1).wav")

ED1 = pygame.mixer.Sound("sounds\ED (1).wav")

EU1 = pygame.mixer.Sound("sounds\EU (1).wav")
            
SD1 = pygame.mixer.Sound("sounds\SD.wav")

SU1 = pygame.mixer.Sound("sounds\SU.wav")


x = "" 
tx = 1360

f= open("Here is your text.txt","w")

while True:
    screen.fill((69,69,69))
    text = myFont.render(x, 1, color)
    screen.blit(text, (tx,300))
    watermark = myFont1.render('Made by VRaj..', 1, color)
    screen.blit(watermark, (1150, 720))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();

        # this write all the remaining text 
            f.write(x)
            f.close()

        # This prevents the too large width or height error by cutting short the string and appending the removed value to our file
        if len(x) >= 50:
            f.write(x[:-12])
            x = x[-12:]
            tx = -80

        mod = False
        smallKey = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SD1.play()
                smallKey = False
            if event.key == pygame.K_RETURN or event.key == pygame.K_CAPSLOCK:
                ED1.play()
                smallKey = False
            if event.key == pygame.K_TAB:
                ED1.play()
                smallKey = False
                mod = True
                x += '   '
                tx -= 240
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                BSPD1.play()
                smallKey = False
            if event.key == pygame.K_BACKSPACE:
                BSPD1.play()
                smallKey = False
                mod = True
                if x != '':
                    x = x[:-1]
                    tx += 240
                else:
                    tx += 120

            if event.key == pygame.K_BACKSLASH:
                BSPD1.play()
                smallKey = False

            if event.key == pygame.K_DELETE:
                x = ''
                tx = 1360
                f.truncate(0)
                
            if smallKey == True: # nullifies the effect of (tx) when a non-character key is pressed
                D1.play()
            if event.unicode != '':
                tx -= 120
                
            if mod == False:  # does not allow modifier or non-character key to get registered
                x += event.unicode # appends the pressed character to the x variable

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                SU1.play()
            if event.key == pygame.K_RETURN or event.key == pygame.K_CAPSLOCK:
                EU1.play()
            if event.key == pygame.K_TAB:
                EU1.play()
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                BSPU1.play()
            if event.key == pygame.K_BACKSPACE:
                BSPU1.play()
            if smallKey == True: 
                U1.play()

        pygame.display.update()

                