import sys
import sdl2
import sdl2.ext

def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello PySDL2", size=(800, 600))
    window.show()
    renderer = sdl2.ext.Renderer(window)
    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        renderer.clear(sdl2.ext.Color(0, 0, 0))
        renderer.present()
        window.refresh()
    return 0

if __name__ == "__main__":
    sys.exit(run())

