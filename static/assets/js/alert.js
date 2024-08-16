document.addEventListener("DOMContentLoaded", function() {
    const offerContainer = document.getElementById('offerContainer');
    const iconContainer = document.getElementById('iconContainer');
    const closeBtn = document.getElementById('closeBtn');

    // Show offer container with animation on page load
    setTimeout(() => {
        offerContainer.classList.add('visible');
    }, 500);

    closeBtn.addEventListener('click', function() {
        offerContainer.classList.remove('visible');
        setTimeout(() => {
            offerContainer.classList.add('hidden');
            iconContainer.classList.remove('hidden');
        }, 500);
    });

    iconContainer.addEventListener('click', function() {
        iconContainer.classList.add('hidden');
        offerContainer.classList.remove('hidden');
        setTimeout(() => {
            offerContainer.classList.add('visible');
        }, 100);
    });
});
