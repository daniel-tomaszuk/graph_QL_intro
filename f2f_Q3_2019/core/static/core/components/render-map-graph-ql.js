function renderGraphQl(graphAPIURL) {

    const positionQuery = getPositionQuery();
    // get data points from BE - draw trajectories for them
    makeRequest('get', graphAPIURL, positionQuery).then(function (response) {
        if (response.data.allPositions.edges.length) {
            const mapDiv = document.querySelector('#box');
            const positionInfo = mapDiv.getBoundingClientRect();
            const color = '#' + (Math.random() * 0xFFFFFF << 0).toString(16);
            var point_list = [];
            const mostRecentNode = response.data.allPositions.edges[0].node;
            const dataContent = "Longi: " + (mostRecentNode.longitude).toFixed(2) +
                '<br>' +
                "Lati: " + (mostRecentNode.latitude).toFixed(2);

            let satIcon = prepareSatellite(mostRecentNode.satellite, dataContent, satelliteURL);

            // put the most actual satellite position on map
            // count where to put the most actual satellite position
            xPx = scaleX(mostRecentNode.longitude, positionInfo.width);
            yPx = scaleY(mostRecentNode.latitude, positionInfo.height);

            satIcon = positionSatellite(satIcon, xPx, yPx);
            $(satIcon).appendTo($(mapDiv));

            // main loop for data points
            for (var l = 1; l < response.data.allPositions.edges.length; l++) {
                var node = response.data.allPositions.edges[l].node;
                var previous_node = response.data.allPositions.edges[l - 1].node;

                var xPx = scaleX(node.longitude, positionInfo.width);
                var yPx = scaleY(node.latitude, positionInfo.height);

                var xPx_prev = scaleX(previous_node.longitude, positionInfo.width);
                var yPx_prev = scaleY(previous_node.latitude, positionInfo.height);

                // find history objects for satellite with name i-th unique name
                var point = mapDivPoint(color, xPx, yPx);
                var point_prev = mapDivPoint(color, xPx_prev, yPx_prev);

                $(mapDiv).append($(point));
                $(mapDiv).append($(point_prev));

                // count distance between two points
                var dist = Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
                // draw line if the distance is close enough
                if (dist < 100) {
                    mapDiv.appendChild(createLine(x1, y1, x2, y2, color));
                }
            }
            addPopovers();
        } else {
            console.log('No data points received.');
        }
    });
}
