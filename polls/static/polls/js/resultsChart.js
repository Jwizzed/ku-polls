document.addEventListener("DOMContentLoaded", function() {
    var ctx = document.getElementById('resultsChart').getContext('2d');
    var labels = document.getElementById('resultsChart').dataset.labels.split(',');
    var votes = document.getElementById('resultsChart').dataset.votes.split(',').map(Number);

    var data = {
        labels: labels,
        datasets: [{
            data: votes,
            backgroundColor: [
                '#FF6384',
                '#36A2EB',
                '#FFCE56',
                '#4BC0C0',
                '#FF9F40',
                '#FFCD56',
                '#C45850'
            ]
        }]
    };

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Radar Chart Initialization
    var radarCtx = document.getElementById('radarChart').getContext('2d');
    var radarLabels = document.getElementById('radarChart').dataset.labels.split(',');
    var radarVotes = document.getElementById('radarChart').dataset.votes.split(',').map(Number);

    var radarData = {
        labels: radarLabels,
        datasets: [{
            label: 'Votes',
            data: radarVotes,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    };

    var myRadarChart = new Chart(radarCtx, {
        type: 'radar',
        data: radarData,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
});
