const VideoPlayer = document.getElementById('video-player')
const PlayButton = document.getElementById('play-button')
const VideoButton = document.getElementById('video-button')
let videoState = false

VideoPlayer.addEventListener('click', playPause)

VideoPlayer.addEventListener('mouseenter', () => {
    if (videoState) {
        // console.log('video state', videoState)
        // console.log('mouse enter')
        PlayButton.style.display = 'block'
    }
})

VideoPlayer.addEventListener('mouseleave', () => {
    if (videoState) {
        // console.log('video state', videoState)
        // console.log('mouse leave')
        PlayButton.style.display = 'none'
    }
})

VideoPlayer.addEventListener('mousemove', () => {
    PlayButton.style.display = 'block'
})

VideoPlayer.addEventListener('play', () => {
    videoState = true
    VideoButton.className = "fas fa-pause-circle fa-4x"
    PlayButton.style.display = "none"
})

VideoPlayer.addEventListener('pause', () => {
    videoState = false
    VideoButton.className = "fas fa-play-circle fa-4x" 
    PlayButton.style.display = "block"
})

PlayButton.addEventListener('click', playPause)

PlayButton.addEventListener('mouseenter', function() {
    this.style.display = 'block'
})

function playPause() {
    if(VideoPlayer.paused) {
        VideoPlayer.play()
    }
    else {
        VideoPlayer.pause()
    }
}