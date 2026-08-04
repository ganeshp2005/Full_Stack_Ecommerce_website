/* ============================================
   NexaTech Solutions - Interactive Features
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {
    // ============ Navbar Scroll Effect ============
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');

    function handleScroll() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Back to top button
        if (window.scrollY > 500) {
            backToTop.classList.add('show');
        } else {
            backToTop.classList.remove('show');
        }

        // Active nav link on scroll
        updateActiveNavLink();
    }

    window.addEventListener('scroll', handleScroll);

    // ============ Mobile Menu ============
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    hamburger.addEventListener('click', function () {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function () {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // ============ Active Nav Link ============
    const sections = document.querySelectorAll('section[id], header[id]');
    const navLinkElements = document.querySelectorAll('.nav-links a:not(.btn-nav)');

    function updateActiveNavLink() {
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinkElements.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + sectionId) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    // ============ Back to Top ============
    backToTop.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // ============ Hero Particles ============
    const particlesContainer = document.getElementById('particles');
    if (particlesContainer) {
        const particleCount = 20;
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            const size = Math.random() * 6 + 2;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 8 + 's';
            particle.style.animationDuration = (Math.random() * 4 + 6) + 's';
            particlesContainer.appendChild(particle);
        }
    }

    // ============ Scroll Reveal Animations ============
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(element => {
        revealObserver.observe(element);
    });

    // ============ Counter Animation for Stats ============
    const statNumbers = document.querySelectorAll('.stat-number');

    function animateCounter(element) {
        const targetText = element.textContent;
        const hasPlus = targetText.includes('+');
        const hasSlash = targetText.includes('/');
        const numericValue = parseInt(targetText.replace(/[^0-9]/g, ''), 10);

        if (isNaN(numericValue)) return;

        let current = 0;
        const increment = Math.ceil(numericValue / 60);
        const duration = 2000;
        const startTime = performance.now();

        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = 1 - Math.pow(1 - progress, 3);

            let displayValue = Math.floor(easedProgress * numericValue);
            let suffix = '';

            if (hasPlus) suffix = '+';
            if (hasSlash) suffix = '/';

            element.textContent = displayValue + suffix;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = targetText;
            }
        }

        requestAnimationFrame(updateCounter);
    }

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    statNumbers.forEach(number => {
        statsObserver.observe(number);
    });

    // ============ Testimonial Slider ============
    const track = document.getElementById('testimonialTrack');
    const slides = document.querySelectorAll('.testimonial-slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const sliderDots = document.getElementById('sliderDots');

    if (track && slides.length > 0) {
        let currentSlide = 0;
        let autoSlideInterval;

        // Create dots
        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.className = 'slider-dot' + (index === 0 ? ' active' : '');
            dot.addEventListener('click', function () {
                goToSlide(index);
                resetAutoSlide();
            });
            sliderDots.appendChild(dot);
        });

        const dots = document.querySelectorAll('.slider-dot');

        function goToSlide(index) {
            currentSlide = index;
            track.style.transform = 'translateX(-' + (currentSlide * 100) + '%)';
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === currentSlide);
            });
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            goToSlide(currentSlide);
        }

        function prevSlide() {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            goToSlide(currentSlide);
        }

        function resetAutoSlide() {
            clearInterval(autoSlideInterval);
            autoSlideInterval = setInterval(nextSlide, 5000);
        }

        nextBtn.addEventListener('click', function () {
            nextSlide();
            resetAutoSlide();
        });

        prevBtn.addEventListener('click', function () {
            prevSlide();
            resetAutoSlide();
        });

        // Touch swipe support
        let touchStartX = 0;
        let touchEndX = 0;

        track.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        track.addEventListener('touchend', function (e) {
            touchEndX = e.changedTouches[0].screenX;
            const threshold = 50;

            if (touchStartX - touchEndX > threshold) {
                nextSlide();
                resetAutoSlide();
            } else if (touchEndX - touchStartX > threshold) {
                prevSlide();
                resetAutoSlide();
            }
        }, { passive: true });

        // Start auto-slide
        autoSlideInterval = setInterval(nextSlide, 5000);
    }

    // ============ Contact Form Submission (sends to Django backend) ============
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !email || !subject || !message) {
                e.preventDefault();
                showFormMessage('Please fill in all fields.', 'error');
                return;
            }

            if (!isValidEmail(email)) {
                e.preventDefault();
                showFormMessage('Please enter a valid email address.', 'error');
                return;
            }

            // If validation passes, DO NOT prevent default -
            // the form submits normally to the server, which saves it to the database.
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;
        });
    }

    function isValidEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    function showFormMessage(message, type) {
        // Remove existing message
        const existingMessage = contactForm.querySelector('.form-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        const messageDiv = document.createElement('div');
        messageDiv.className = 'form-message ' + type;
        messageDiv.innerHTML = message;
        messageDiv.style.cssText = 'padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9rem; font-weight: 500; animation: slideIn 0.3s ease;';

        if (type === 'success') {
            messageDiv.style.background = 'rgba(0, 206, 201, 0.1)';
            messageDiv.style.border = '1px solid #00cec9';
            messageDiv.style.color = '#00b894';
        } else {
            messageDiv.style.background = 'rgba(255, 95, 87, 0.1)';
            messageDiv.style.border = '1px solid #ff5f57';
            messageDiv.style.color = '#d63031';
        }

        contactForm.insertBefore(messageDiv, contactForm.firstChild);

        setTimeout(function () {
            messageDiv.style.opacity = '0';
            messageDiv.style.transition = 'opacity 0.3s ease';
            setTimeout(function () {
                messageDiv.remove();
            }, 300);
        }, 5000);
    }

    // ============ Newsletter Form ============
    const newsletterForm = document.querySelector('.newsletter-form');

    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const emailInput = newsletterForm.querySelector('input[type="email"]');
            const email = emailInput.value.trim();

            if (email && isValidEmail(email)) {
                emailInput.value = '';
                emailInput.placeholder = 'Subscribed! 🎉';
                setTimeout(function () {
                    emailInput.placeholder = 'Your email address';
                }, 3000);
            }
        });
    }

    // ============ Smooth Scrolling for Anchor Links ============
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ============ Tilt Effect for Code Window ============
    const codeWindow = document.querySelector('.code-window');

    if (codeWindow) {
        codeWindow.addEventListener('mousemove', function (e) {
            if (window.innerWidth < 768) return;

            const rect = codeWindow.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateY = ((x - centerX) / centerX) * 8;
            const rotateX = ((y - centerY) / centerY) * -5;

            codeWindow.style.transform = 'rotateY(' + rotateY + 'deg) rotateX(' + rotateX + 'deg)';
        });

        codeWindow.addEventListener('mouseleave', function () {
            codeWindow.style.transform = 'rotateY(-8deg) rotateX(5deg)';
            codeWindow.style.transition = 'transform 0.5s ease';
            setTimeout(function () {
                codeWindow.style.transition = '';
            }, 500);
        });
    }

    // ============ Initial Scroll Check ============
    handleScroll();
    updateActiveNavLink();
});