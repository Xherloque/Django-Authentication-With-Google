// Example: Show a confirmation message on logout
document.addEventListener("DOMContentLoaded", () => {
    const logoutLink = document.querySelector('a[href*="logout"]');
    if (logoutLink) {
        logoutLink.addEventListener("click", (e) => {
            if (!confirm("Are you sure you want to logout?")) {
                e.preventDefault();
            }
        });
    }
});
