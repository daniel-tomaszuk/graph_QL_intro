function scaleX(lati, xMax){
    /**
    * Scale geographical latitude into x [px] coordinate.
    * @param {number} lati - The latitude value in degrees.
    * @param {number} xMax - The max X dimension of world map image.
    */
    var xPx = (xMax / 360) * lati + 0.5 * xMax;
    return xPx
};

function scaleY(longi, yMax){
    /**
    * Scale geographical longitude into y [px] coordinate.
    * @param {number} longi - The longitude value in degrees.
    * @param {number} yMax - The max Y dimension of map image.
    */
    var yPx = -1 * (yMax / 180) * longi + 0.5 * yMax;
    return yPx;
};

function mapDivPoint(color, x, y){
    /**
    * Create point as mapDiv tag.
    * @param {string} size - size of the point. Same as in CSS.
    * @param {string} color - Color of the point. Same as in CSS.
    */
    var point = $('<mapDiv>');
    var size = '3px';

    $(point)
        .css('position', 'absolute')
        .css('width', size)
        .css('height', size)
        .css('background-color', color)
        .css('left', x + "px")
        .css('top', y +'px')
        .css('display', '');
    return $(point)
};

function createLineElement(x, y, length, angle, color){
    /**
    * Draws line element on the image.
    * @param {number} x - Absolute x position of the line beginning.
    * @param {number} y - Absolute y position of the line beginning.
    * @param {number} length - Length of the line.
    * @param {number} angle - Angle of the line.
    * @param {string} color - Color of the line.
    */
    var line = document.createElement('div');
    var styles = 'border: 1px solid;'
               + 'width: ' + length + 'px; '
               + 'height: 0px; '
               + '-moz-transform: rotate(' + angle + 'rad); '
               + '-webkit-transform: rotate(' + angle + 'rad); '
               + '-o-transform: rotate(' + angle + 'rad); '
               + '-ms-transform: rotate(' + angle + 'rad); '
               + 'position: absolute; '
               + 'top: ' + y + 'px; '
               + 'left: ' + x + 'px; '
               + 'color:' + color +';';
    line.setAttribute('style', styles);
    return line;
};

function createLine(x1, y1, x2, y2, color) {
    /**
    * Counts parameters required for line drawing.
    * https://stackoverflow.com/questions/4270485/drawing-lines-on-html-page
    * @param {number} x1 - Absolute x position of the line beginning.
    * @param {number} y1 - Absolute y position of the line beginning.
    * @param {number} x2 - Absolute x position of the line ending.
    * @param {number} y2 - Absolute y position of the line ending.
    * @param {string} color - Color of the line.
    */
    // a^2 + b^2 = c^2
    var a = x1 - x2;
    var b = y1 - y2;
    var c = Math.sqrt(a * a + b * b);
    // coordinate of the middle point in c line
    var sx = (x1 + x2) / 2;
    var sy = (y1 + y2) / 2;

    var x = sx - c / 2;
    var y = sy;

    var alpha = Math.PI - Math.atan2(-b, a);
    return createLineElement(x, y, c, alpha, color);
};
