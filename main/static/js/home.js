
document.addEventListener("DOMContentLoaded", function () {
    const confetti_button = document.querySelector(".highlight");
    confetti_button.addEventListener('mouseover', function (event) {
        const rect = confetti_button.getBoundingClientRect();
        const x = (rect.left + rect.right) / 2;
        const y = (rect.top + rect.bottom) / 2;
        // Configures the settings for the confetti effect.
        const confettiSettings = {
        particleCount: 60, // Defines the number of confetti particles.
        spread: 90,         // Sets the spread angle of the confetti.
        // Specifies the origin point for the confetti effect based on the button's location.
        origin: { x: x / window.innerWidth, y: y / window.innerHeight },
        colors: [
            '#2f76ab',
            '#2b3035',
            '#b7b7b7',
            '#000',
            '#21a0ff',
            '#cccccd'
          ],
        };

        confetti(confettiSettings);
    });
});