function renderRest(restAPIUrl, satelliteURL) {

    makeRequest('get', restAPIUrl, '').then(function (response) {
        const dataResponse = response[0];
        if (dataResponse.satellite_positions.length) {
            let mapDiv = $('#box');
            const positionInfo = document.querySelector('#box').getBoundingClientRect();
            const color = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
            const dataContent = "Longi: " + (dataResponse.satellite_positions[0].longitude).toFixed(2) +
                "<br>" + "Lati: " + (dataResponse.satellite_positions[0].latitude).toFixed(2)
            let satIcon = prepareSatellite(dataResponse, dataContent, satelliteURL);

            // put the most actual satellite position on map
            // count where to put the most actual satellite position
            xPx = scaleX(dataResponse.satellite_positions[0].longitude, positionInfo.width);
            yPx = scaleY(dataResponse.satellite_positions[0].latitude, positionInfo.height);
            satIcon = positionSatellite(satIcon, xPx, yPx);
            $(mapDiv).append($(satIcon));

            console.log(dataResponse.satellite_positions.length);
            // main loop for data points
            for (var l = 1; l < dataResponse.satellite_positions.length; l++) {
                var node = dataResponse.satellite_positions[l];
                var previous_node = dataResponse.satellite_positions[l - 1];

                var xPx = scaleX(node.longitude, positionInfo.width);
                var yPx = scaleY(node.latitude, positionInfo.height);

                var xPx_prev = scaleX(previous_node.longitude, positionInfo.width);
                var yPx_prev = scaleY(previous_node.latitude, positionInfo.height);

                var point = mapDivPoint(color, xPx, yPx);
                var point_prev = mapDivPoint(color, xPx_prev, yPx_prev);

                $(mapDiv).append($(point));
                $(mapDiv).append($(point_prev));

                // count distance between two points
                var dist = Math.sqrt(Math.pow((xPx_prev - xPx), 2) + Math.pow((yPx_prev - yPx), 2));
                // draw line if the distance is close enough
                if (dist < 100) {
                    $(mapDiv).append($(createLine(xPx_prev, yPx_prev, xPx, yPx, color)));
                }
            }
            addPopovers();

        }
    });
}
