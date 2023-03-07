input.onButtonPressed(Button.A, function () {
    music.playMelody("C5 B A G F E D C ", 250)
    music.stopAllSounds()
    music.playMelody("C5 B A A B C5 B A ", 122)
    music.stopAllSounds()
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Sad)
})
