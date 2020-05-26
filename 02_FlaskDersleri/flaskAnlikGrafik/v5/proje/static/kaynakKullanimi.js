$(document).ready(function () {
    const config = {
        type: 'pie',
        data: {
            labels: ['Kullanılan', 'Mevcut'],
            datasets: [{
                label: '# Ram Kullanımı',
                data: [],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(255, 206, 86, 0.2)',
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(255, 206, 86, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            cutoutPercentage: 40,
            responsive: false,
            title: {
                display: true,
                text: 'RAM'
            },
            legend: {
                display: false
            },
        }
    };
    
    const context = document.getElementById('ramKullanim').getContext("2d");
    const pieChart = new Chart(context, config);
    const source = new EventSource("/ram");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        config.data.datasets[0].data[0] = data['Kullanılan'];
        config.data.datasets[0].data[1] = data['Mevcut'];
        pieChart.update();
    }
});

// https://www.chartjs.org/docs/latest/developers/api.html

$(document).ready(function () {
    const config = {
        type: 'pie',
        data: {
            labels: ['Geçerli', 'Maks.'],
            datasets: [{
                label: '# CPU Kullanımı',
                data: [],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(255, 206, 86, 0.2)',
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(255, 206, 86, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            cutoutPercentage: 40,
            responsive: false,
            title: {
                display: true,
                text: 'CPU'
            },
            legend: {
                display: false
            },
        }
    };
    
    const context = document.getElementById('cpuKullanimi').getContext("2d");
    const pieChart = new Chart(context, config);
    const source = new EventSource("/cpu");
    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        config.data.datasets[0].data[0] = data['Geçerli'];
        config.data.datasets[0].data[1] = data['Maks.'];
        pieChart.update();
    }
});