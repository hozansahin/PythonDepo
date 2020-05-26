$(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Kullanılan RAM",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Gerçek Zamanlı Ram Kullanım Grafiği'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Zaman'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Kullanılan RAM'
                    }
                }]
            }
        }
    };

    const context = document.getElementById('ramKullanim').getContext('2d');

    const lineChart = new Chart(context, config);

    const source = new EventSource("/veri");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config.data.labels.length === 5) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        } // Maks. 5 Adet


        config.data.labels.push(data['Zaman']);
        config.data.datasets[0].data.push(data['Veri']);
        lineChart.update();
    }
}); 