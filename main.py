def on_button_pressed_a():
    music.play_melody("C5 B A G F E D C ", 250)
    music.stop_all_sounds()
    music.play_melody("C5 B A A B C5 B A ", 122)
    music.stop_all_sounds()
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.A, on_button_pressed_a)
