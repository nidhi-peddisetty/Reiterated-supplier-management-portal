// index.js

// Example of DOM manipulation
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('button').addEventListener('click', function() {
        document.getElementById('message').innerText = 'Button clicked!';
    });
  });
  