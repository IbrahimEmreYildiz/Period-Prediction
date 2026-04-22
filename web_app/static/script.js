document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const btn = document.getElementById('predict-btn');
    const btnText = btn.querySelector('.btn-text');
    const loader = document.getElementById('loader');
    
    const resultContainer = document.getElementById('result-container');
    const resultValue = document.getElementById('prediction-result');
    const actualBox = document.getElementById('actual-box');
    const actualResult = document.getElementById('actual-result');
    const errorDisplay = document.getElementById('error-display');
    const errorValue = document.getElementById('error-value');

    // Show loading state
    btnText.style.opacity = '0';
    loader.style.display = 'block';
    btn.disabled = true;

    // Get input values
    const data = {
        pl_orbsmax: parseFloat(document.getElementById('pl_orbsmax').value),
        st_mass: parseFloat(document.getElementById('st_mass').value),
        pl_orbeccen: parseFloat(document.getElementById('pl_orbeccen').value),
        st_rad: parseFloat(document.getElementById('st_rad').value),
        pl_rade: parseFloat(document.getElementById('pl_rade').value)
    };

    const actualVal = parseFloat(document.getElementById('actual_value').value);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Prediction failed');
        }

        const result = await response.json();
        const prediction = result.prediction;

        // Update UI with result
        resultValue.textContent = prediction.toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 4
        });
        
        // Handle actual value comparison
        if (!isNaN(actualVal)) {
            actualResult.textContent = actualVal.toLocaleString(undefined, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 4
            });
            actualBox.classList.remove('hidden');
            
            // Calculate error percentage
            const diff = Math.abs(prediction - actualVal);
            const errorPercent = (diff / actualVal) * 100;
            errorValue.textContent = errorPercent.toFixed(2) + '%';
            errorDisplay.classList.remove('hidden');
        } else {
            actualBox.classList.add('hidden');
            errorDisplay.classList.add('hidden');
        }

        resultContainer.classList.remove('hidden');
        resultContainer.scrollIntoView({ behavior: 'smooth' });

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred during prediction: ' + error.message);
    } finally {
        // Reset button state
        btnText.style.opacity = '1';
        loader.style.display = 'none';
        btn.disabled = false;
    }
});

// Add some subtle input focus effects
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('focus', () => {
        input.parentElement.style.transform = 'translateX(5px)';
        input.parentElement.style.transition = 'transform 0.3s ease';
    });
    input.addEventListener('blur', () => {
        input.parentElement.style.transform = 'translateX(0)';
    });
});
