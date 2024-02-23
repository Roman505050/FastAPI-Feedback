document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', handleSubmit);

    const closeErrorBtn = document.querySelector('.close-error');
    closeErrorBtn.addEventListener('click', function() {
        const modal = document.getElementById('modal-error');
        modal.style.display = 'none';
    });

    const closeSuccessBtn = document.querySelector('.close-success');
    closeSuccessBtn.addEventListener('click', function() {
        const modal = document.getElementById('modal-success');
        modal.style.display = 'none';
    });
});


function handleSubmit(event) {
    event.preventDefault();

    const formData = getFormData();
    sendData(formData);
}

function getFormData() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    return {
        name: name,
        email: email,
        phone: phone,
        message: message
    };
}

function sendData(data) {
    const url = 'api/v1/form/submit';
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch(url, options)
        .then(handleResponse)
        .then(showSuccessMessage)
        .catch(handleError);
}

function handleResponse(response) {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

function showSuccessMessage(data) {
    const modal = document.getElementById('modal-success');
    modal.style.display = 'block';
}

function showErrorMessage() {
    const modal = document.getElementById('modal-error');
    modal.style.display = 'block';
}

function handleError(error) {
    console.error('Error:', error);
    showErrorMessage();
}