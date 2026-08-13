function copyPassword(inputId) {
    console.log(alert("Welcome to Nova Password Generator!"))

    const passwordField = document.getElementById(inputId);

    navigator.clipboard.writeText(passwordField.value);

    alert("Password copied to clipboard!");
}