function renderGraphQl(graphAPIURL) {

    const positionQuery = getPositionQuery();
    // get data points from BE - draw trajectories for them
      makeRequest('get', graphAPIURL, positionQuery).then(function (response){
        if (response.data.allPositions.edges.length)  {
            var mapDiv = document.querySelector('#box');
            var positionInfo = mapDiv.getBoundingClientRect();
            var color = '#' + (Math.random()*0xFFFFFF<<0).toString(16);
            var point_list = [];
            var satIcon = $('<img />');
            var mostRecentNode = response.data.allPositions.edges[0].node;
            var dataContent = "Longi: "+ (mostRecentNode.longitude).toFixed(2) +
                              '<br>' +
                              "Lati: " + (mostRecentNode.latitude).toFixed(2)

            $(satIcon).attr('class', 'pop');
            $(satIcon).attr('id', 'SatId_' + mostRecentNode.satellite.noradId);
            $(satIcon).attr('src', satelliteURL);
            $(satIcon).attr('alt', 'Sat ' + mostRecentNode.satellite.name);
            $(satIcon).attr('data-toggle', 'popover');
            $(satIcon).attr('data-trigger', 'focus');
            $(satIcon).attr('data-html', true);
            $(satIcon).attr('title', mostRecentNode.satellite.name);
            $(satIcon).attr('data-content', dataContent);
            $(satIcon).css('display','none');
            $(satIcon).css('width', "2%");
            $(satIcon).css('height', "4%");
            $(satIcon).css('position', 'absolute');
            $(satIcon).css('top', '0px');
            $(satIcon).css('left', '0px');

            // put the most actual satellite position on map
            // count where to put the most actual satellite position
            xPx = scaleX(mostRecentNode.longitude, positionInfo.width);
            yPx = scaleY(mostRecentNode.latitude, positionInfo.height);
            $(satIcon).css('left', xPx - 10 + "px");
            $(satIcon).css('top', yPx - 20 + "px");
            $(satIcon).css('display', '');
            $(satIcon).css('z-index', '10');
            $(satIcon).appendTo($(mapDiv));

            // main loop for data points
            for (var l = 0; l < response.data.allPositions.edges.length; l++){
              var node = response.data.allPositions.edges[l].node

              // find history objects for satellite with name i-th unique name
              var point = mapDivPoint(color, xPx, yPx);
              $(point).appendTo($('#box'));
              // count where to put past position icon
              var xPx = scaleX(node.longitude, positionInfo.width);
              var yPx = scaleY(node.latitude, positionInfo.height);
              // push history x and y coordinates in the coordinates list
              point_list.push([xPx, yPx]);
            }

            // draw lines between points
            for (var k = 0; k < parseInt((point_list.length)) - 1; k++){

                var x1 = parseInt(point_list[k][0])
                var y1 = parseInt(point_list[k][1])
                var x2 = parseInt(point_list[k+1][0])
                var y2 = parseInt(point_list[k+1][1])
                // count distance between two points
                var dist = Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
                // draw line if the distance is close enough
                if (dist < 100){
                    mapDiv.appendChild(createLine(x1, y1, x2, y2, color));
                }
            }
            addPopovers();
        } else {
            console.log('No data points received.');
        }
      });
}
