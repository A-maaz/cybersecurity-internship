// PhishAware Dashboard & Chart.js Visualizations

document.addEventListener('DOMContentLoaded', () => {
    initCharts();
    initEventLogFilter();
});

function initCharts() {
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            renderFunnelChart(data.funnel);
            renderOutcomesChart(data.outcomes);
            renderDepartmentChart(data.departments);
        })
        .catch(err => {
            console.warn('Metrics API load note:', err);
        });
}

// 1. Interaction Funnel Chart
function renderFunnelChart(funnelData) {
    const ctx = document.getElementById('funnelChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: funnelData.labels,
            datasets: [{
                label: 'Telemetry Count',
                data: funnelData.data,
                backgroundColor: [
                    'rgba(59, 130, 246, 0.7)',   // Sent (Blue)
                    'rgba(0, 210, 255, 0.7)',   // Opened (Cyan)
                    'rgba(16, 185, 129, 0.7)',  // Reported (Emerald)
                    'rgba(239, 68, 68, 0.7)',   // Clicked (Crimson)
                    'rgba(139, 92, 246, 0.7)'   // Trained (Purple)
                ],
                borderColor: [
                    '#3b82f6',
                    '#00d2ff',
                    '#10b981',
                    '#ef4444',
                    '#8b5cf6'
                ],
                borderWidth: 1.5,
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#0f172a',
                    titleColor: '#f8fafc',
                    bodyColor: '#94a3b8',
                    borderColor: '#1e293b',
                    borderWidth: 1
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8', font: { size: 11 } }
                },
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8', stepSize: 2 }
                }
            }
        }
    });
}

// 2. Simulation Outcome Distribution (Donut Chart)
function renderOutcomesChart(outcomesData) {
    const ctx = document.getElementById('outcomesChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: outcomesData.labels,
            datasets: [{
                data: outcomesData.data,
                backgroundColor: [
                    '#10b981', // Reported
                    '#ef4444', // Clicked
                    '#f59e0b', // Opened No Action
                    '#334155'  // Unopened
                ],
                borderColor: '#131c2e',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { color: '#cbd5e1', font: { size: 12 }, padding: 12 }
                },
                tooltip: {
                    backgroundColor: '#0f172a',
                    titleColor: '#f8fafc',
                    bodyColor: '#94a3b8',
                    borderColor: '#1e293b',
                    borderWidth: 1
                }
            },
            cutout: '68%'
        }
    });
}

// 3. Department Risk Breakdown
function renderDepartmentChart(deptData) {
    const ctx = document.getElementById('departmentChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: deptData.labels,
            datasets: [
                {
                    label: 'Reported Phishing (Vigilant)',
                    data: deptData.reported,
                    backgroundColor: 'rgba(16, 185, 129, 0.8)',
                    borderColor: '#10b981',
                    borderWidth: 1,
                    borderRadius: 4
                },
                {
                    label: 'Clicked Link (Vulnerable)',
                    data: deptData.clicked,
                    backgroundColor: 'rgba(239, 68, 68, 0.8)',
                    borderColor: '#ef4444',
                    borderWidth: 1,
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: { color: '#cbd5e1', font: { size: 11 } }
                }
            },
            scales: {
                x: {
                    stacked: false,
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8', font: { size: 11 } }
                },
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8', stepSize: 1 }
                }
            }
        }
    });
}

// Event Log Filter
function initEventLogFilter() {
    const filterInput = document.getElementById('eventLogFilter');
    if (!filterInput) return;

    filterInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const rows = document.querySelectorAll('#eventsTableBody tr');
        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    });
}
