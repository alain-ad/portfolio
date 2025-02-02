document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const htmlElement = document.documentElement;
    const bodyElement = document.body;

    // Vérifie la préférence de l'utilisateur stockée
    const storedTheme = localStorage.getItem('theme');
    const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (storedTheme) {
        htmlElement.classList.toggle('dark-mode', storedTheme === 'dark');
        bodyElement.classList.toggle('dark-mode', storedTheme === 'dark');
        darkModeToggle.checked = storedTheme === 'dark';
    } else if (prefersDarkMode) {
        htmlElement.classList.add('dark-mode');
        bodyElement.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }

    // Gère le changement de thème lorsqu'on clique sur le switch
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            htmlElement.classList.toggle('dark-mode');
            bodyElement.classList.toggle('dark-mode');
            const isDarkMode = htmlElement.classList.contains('dark-mode');
            localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
        });
    }
});
