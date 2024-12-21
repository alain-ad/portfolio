document.addEventListener('DOMContentLoaded', () => {
    // ----------- Variables globales -----------
    const header = document.querySelector('.header');
    const nav = document.querySelector('.nav');

    // ----------- Animation des éléments du header -----------
    function animateHeaderElements() {
        const elements = [
            header.querySelector('h1'),
            header.querySelector('h2'),
            header.querySelector('p'),
            header.querySelector('.cta-button')
        ];

        elements.forEach((el, index) => {
            if (el) {
                el.style.opacity = '0';
                el.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    el.style.transition = 'all 0.8s ease';
                    el.style.opacity = '1';
                    el.style.transform = 'translateY(0)';
                }, 200 * index);
            }
        });
    }

    // ----------- Navigation -----------
    // Smooth scroll pour les liens de navigation
    function initSmoothScroll() {
        document.querySelectorAll('.nav a').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                const navHeight = nav.offsetHeight;

                window.scrollTo({
                    top: targetSection.offsetTop - navHeight,
                    behavior: 'smooth'
                });
            });
        });
    }

    // ----------- Animations des sections -----------
    // Animation des compétences et technologies
    function initSkillsAnimation() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px'
        });

        // Observer les éléments de compétences
        document.querySelectorAll('#about ul li').forEach(item => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(20px)';
            observer.observe(item);
        });
    }

    // ----------- Bouton CTA -----------
    function initCTAButton() {
        const cta = document.querySelector('.cta-button');
        if (cta) {
            cta.addEventListener('mouseenter', () => {
                cta.style.transform = 'translateY(-5px)';
                cta.style.boxShadow = '0 8px 15px rgba(59, 130, 246, 0.2)';
            });

            cta.addEventListener('mouseleave', () => {
                cta.style.transform = 'translateY(0)';
                cta.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
            });
        }
    }

    // ----------- Liens sociaux -----------
    function initSocialLinks() {
        const socialLinks = document.querySelectorAll('#contact ul li a');
        socialLinks.forEach(link => {
            link.addEventListener('mouseenter', function() {
                this.style.transform = 'scale(1.1)';
            });

            link.addEventListener('mouseleave', function() {
                this.style.transform = 'scale(1)';
            });
        });
    }

    // ----------- Styles dynamiques -----------
    const styles = `
        .visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
            transition: all 0.6s ease-out;
        }

        #about ul li {
            transition: all 0.3s ease-in-out;
        }

        #contact ul li a {
            transition: all 0.3s ease;
            display: inline-block;
        }
    `;

    const styleSheet = document.createElement('style');
    styleSheet.textContent = styles;
    document.head.appendChild(styleSheet);

    // ----------- Initialisation -----------
    animateHeaderElements();
    initSmoothScroll();
    initSkillsAnimation();
    initCTAButton();
    initSocialLinks();
});