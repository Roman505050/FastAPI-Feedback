document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input[type="text"], input[type="email"], input[type="phone"]');
    
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            const label = input.parentElement.querySelector('label');
            if (input.value.trim() !== '') {
                label.classList.add('has-content');
            } else {
                label.classList.remove('has-content');
            }
        });
    });
});
