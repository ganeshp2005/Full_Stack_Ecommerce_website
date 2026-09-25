/* ============================================
   YourChoice - E-Commerce Interactive Features
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {
    // Auto-dismiss alert messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(function () {
                alert.remove();
            }, 500);
        }, 5000);
    });

    // Add to cart button animation
    const addCartButtons = document.querySelectorAll('.add-cart-btn, .add-cart-lg');
    addCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            if (button.disabled) return;
            button.style.transform = 'scale(0.95)';
            setTimeout(function () {
                button.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Smooth scroll for back to top buttons
    document.querySelectorAll('.back-top-btn, a[href="#top"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });

    // 3D Tilt animation effect on Product Cards
    const cards = document.querySelectorAll('.product-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        });
    });
});