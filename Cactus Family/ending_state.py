import game_framework
import title_state
from pico2d import *
import Cactus_Family

name = "EndingState"
image = None
ending_bgm = None


def enter():
    global image, ending_bgm
    image = load_image('image_file\\ending.png')
    ending_bgm = load_music('sound_effect\\ending_bgm.mp3')
    ending_bgm.set_volume(64)
    ending_bgm.repeat_play()


def exit():
    global image, ending_bgm
    ending_bgm.pause()
    del image


def update():
    pass


def draw():
    clear_canvas()
    image.draw(450, 400)
    Cactus_Family.game_stage.print_score()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def pause(): pass


def resume(): pass
