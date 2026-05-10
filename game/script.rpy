image bg bedroom = Fixed(
    Solid("#1b1c22"),
    Text("Bedroom (placeholder)", xalign=0.5, yalign=0.5, size=64, color="#ffffff"),
)

image bg kitchen = Fixed(
    Solid("#1c221b"),
    Text("Kitchen (placeholder)", xalign=0.5, yalign=0.5, size=64, color="#ffffff"),
)

init python:
    def play_audio_if_exists(filename, channel="sound", loop=False, fadein=0.0):
        if filename and renpy.loadable(filename):
            renpy.music.play(filename, channel=channel, loop=loop, fadein=fadein)

    def stop_audio(channel="sound", fadeout=0.0):
        renpy.music.stop(channel=channel, fadeout=fadeout)


label splashscreen:
    scene black
    with fade

    centered "{size=40}Disclaimer{/size}\n\nThis is an early prototype.\nSome content may be incomplete or subject to change."

    pause
    return


label start:
    scene black
    with Fade(0.25, 0.0, 0.75)

    $ play_audio_if_exists("audio/nature_ambience.ogg", channel="music", loop=True, fadein=1.0)
    $ play_audio_if_exists("audio/alarm.ogg", channel="sound")

    scene bg bedroom
    with fade

    "You wake up in your bedroom to the sound of your alarm going off."

    $ play_audio_if_exists("audio/bedsheets_rustle.ogg", channel="sound")
    "The bedsheets rustle as you shift, still half-lost in sleep."

    $ stop_audio(channel="sound", fadeout=0.5)
    "After lying in bed for a while, it’s time for you to get up and start your day."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    "You walk to the giant butterfly on the wall and reach out to touch it…"

    $ stop_audio(channel="sound", fadeout=0.25)
    "But your hand phases through it, the butterfly wasn’t real. They usually aren’t…"

    "You shift your attention to the mirror and look at yourself."

    menu:
        "How do you see yourself?"
        "Perfectly ordinary.":
            "For a moment, your reflection feels stable—almost believable."
        "Not quite you.":
            "Your reflection hesitates, a fraction out of sync, like it’s remembering how to be you."

    $ play_audio_if_exists("audio/footsteps.ogg", channel="sound")
    "You decide it’s time to go to the kitchen and have some breakfast."

    $ play_audio_if_exists("audio/door_open.ogg", channel="sound")
    scene bg kitchen
    with dissolve

    "Breakfast can wait. For now, the day begins."
    return
