function toggleDark() {
    document.body.classList.toggle("dark");
}

/* Fullscreen on open (mobile) */
function goFullScreen() {
    let el = document.documentElement;
    if (el.requestFullscreen) {
        el.requestFullscreen();
    }
}

/* Auto trigger fullscreen (user interaction needed on most browsers) */
document.addEventListener("click", () => {
    goFullScreen();
}, { once: true });