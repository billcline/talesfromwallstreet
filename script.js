// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Add 3D rotation effect to book on mouse move (Desktop only)
const bookContainer = document.querySelector('.book-container');
const heroSection = document.querySelector('.hero');

if (window.matchMedia("(min-width: 900px)").matches) {
    heroSection.addEventListener('mousemove', (e) => {
        const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
        const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
        bookContainer.style.transform = `rotateY(${-25 + xAxis}deg) rotateX(${5 + yAxis}deg)`;
    });

    // Reset on mouse leave
    heroSection.addEventListener('mouseleave', () => {
        bookContainer.style.transform = `rotateY(-25deg) rotateX(5deg)`;
    });
}

// Mobile Menu Toggle
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        mobileToggle.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            mobileToggle.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
}