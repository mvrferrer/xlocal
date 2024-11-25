
// Elements
const gradientPreview = document.getElementById('gradient-preview');
const color1Input = document.getElementById('color1');
const color2Input = document.getElementById('color2');
const angleInput = document.getElementById('angle');
const angleValue = document.getElementById('angle-value');
const cssOutput = document.getElementById('css-output');
const copyCssButton = document.getElementById('copy-css');

// Update Gradient Preview
function updateGradient() {
    const color1 = color1Input.value;
    const color2 = color2Input.value;
    const angle = angleInput.value;

    // Generate CSS gradient code
    const gradientCss = `linear-gradient(${angle}deg, ${color1}, ${color2})`;
    
    // Update the preview and output
    gradientPreview.style.background = gradientCss;
    cssOutput.value = `background: ${gradientCss};`;
    angleValue.textContent = `${angle}°`;
}

// Copy CSS to Clipboard
function copyCss() {
    cssOutput.select();
    document.execCommand('copy');
    alert('CSS copied to clipboard!');
}

// Attach Event Listeners
color1Input.addEventListener('input', updateGradient);
color2Input.addEventListener('input', updateGradient);
angleInput.addEventListener('input', updateGradient);
copyCssButton.addEventListener('click', copyCss);

// Initialize Gradient
updateGradient();
