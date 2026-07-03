document.addEventListener('DOMContentLoaded', function() {
    // ----------------------------------------------------
    // 1. Dark Mode / Theme Toggle
    // ----------------------------------------------------
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    
    // Check for saved theme preference, otherwise default to light
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            let theme = document.documentElement.getAttribute('data-theme');
            let newTheme = theme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'dark') {
            themeIcon.className = 'fa-solid fa-sun';
            themeToggle.classList.remove('btn-outline-success');
            themeToggle.classList.add('btn-outline-warning');
        } else {
            themeIcon.className = 'fa-solid fa-moon';
            themeToggle.classList.remove('btn-outline-warning');
            themeToggle.classList.add('btn-outline-success');
        }
    }

    // ----------------------------------------------------
    // 2. Client-Side Input Validation and Loading State
    // ----------------------------------------------------
    const predictForm = document.getElementById('predictForm');
    const submitBtn = document.getElementById('submitBtn');
    
    if (predictForm) {
        predictForm.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Numerical validation rules
            const rules = {
                'n': { min: 0, max: 150, name: 'Nitrogen (N)' },
                'p': { min: 0, max: 150, name: 'Phosphorous (P)' },
                'k': { min: 0, max: 210, name: 'Potassium (K)' },
                'temp': { min: -10, max: 60, name: 'Temperature' },
                'humidity': { min: 0, max: 100, name: 'Humidity' },
                'ph': { min: 0, max: 14, name: 'Soil pH' },
                'rainfall': { min: 0, max: 500, name: 'Rainfall' }
            };

            for (const [id, rule] of Object.entries(rules)) {
                const input = document.getElementById(id);
                if (!input) continue;

                const val = parseFloat(input.value);
                // Clear old invalid feedbacks if any
                input.classList.remove('is-invalid');
                let parentGroup = input.closest('.input-group');
                let existingFeedback = parentGroup.querySelector('.invalid-feedback');
                if (existingFeedback) {
                    existingFeedback.remove();
                }

                if (isNaN(val)) {
                    showValidationError(input, `Please enter a valid number for ${rule.name}.`);
                    isValid = false;
                } else if (val < rule.min || val > rule.max) {
                    showValidationError(input, `${rule.name} must be between ${rule.min} and ${rule.max}.`);
                    isValid = false;
                }
            }

            if (!isValid) {
                e.preventDefault();
                e.stopPropagation();
            } else {
                // Show loading spinner
                submitBtn.disabled = true;
                submitBtn.querySelector('.normal-state').classList.add('d-none');
                submitBtn.querySelector('.loading-state').classList.remove('d-none');
            }
        });
    }

    function showValidationError(input, message) {
        input.classList.add('is-invalid');
        const feedback = document.createElement('div');
        feedback.className = 'invalid-feedback d-block';
        feedback.innerText = message;
        input.closest('.input-group').appendChild(feedback);
    }

    // ----------------------------------------------------
    // 3. Load Prediction History
    // ----------------------------------------------------
    const historyTableBody = document.getElementById('historyTableBody');
    if (historyTableBody) {
        fetch('/history')
            .then(response => response.json())
            .then(data => {
                historyTableBody.innerHTML = '';
                if (data.length === 0) {
                    historyTableBody.innerHTML = `
                        <tr>
                            <td colspan="5" class="text-center text-muted">No predictions have been recorded yet.</td>
                        </tr>
                    `;
                    return;
                }
                data.forEach((row, index) => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <th scope="row">${index + 1}</th>
                        <td>
                            <span class="badge bg-success-subtle text-success me-1">N: ${row.n}</span>
                            <span class="badge bg-primary-subtle text-primary me-1">P: ${row.p}</span>
                            <span class="badge bg-warning-subtle text-warning">K: ${row.k}</span>
                        </td>
                        <td class="small text-muted">
                            Temp: ${row.temp}°C | Humid: ${row.humidity}% | pH: ${row.ph} | Rain: ${row.rainfall}mm
                        </td>
                        <td><strong>${row.prediction}</strong></td>
                        <td><span class="badge bg-secondary">${row.confidence}</span></td>
                    `;
                    historyTableBody.appendChild(tr);
                });
            })
            .catch(err => {
                console.error("Error loading prediction history:", err);
                historyTableBody.innerHTML = `
                    <tr>
                        <td colspan="5" class="text-center text-danger">Failed to load prediction history.</td>
                    </tr>
                `;
            });
    }
});
