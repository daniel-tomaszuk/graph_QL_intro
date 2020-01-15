
function prepareSatellite(dataResponse, dataContent, satelliteURL) {
    return $('<img />')
        .attr('class', 'pop')
        .attr('class', 'satellite')
        .attr('id', 'SatId_' + dataResponse.noradId)
        .attr('src', satelliteURL)
        .attr('alt', 'Sat ' + dataResponse.name)
        .attr('data-toggle', 'popover')
        .attr('data-trigger', 'focus')
        .attr('data-html', true)
        .attr('title', dataResponse.name)
        .attr('data-content', dataContent)
        .css('display', 'none')
        .css('width', "2%")
        .css('height', "4%")
        .css('position', 'absolute')
        .css('top', '0px')
        .css('left', '0px');
}
