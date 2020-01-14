function positionSatellite(satellite, xPos, yPos) {
    return $(satellite)
        .css('left', xPos - 10 + 'px')
        .css('top', yPos - 20 + 'px')
        .css('display', '')
        .css('z-index', '10');
}
