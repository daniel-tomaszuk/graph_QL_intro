function addPopovers() {
    // popovers
    $(".pop").each(function() {
        $(this).on('mouseover', function(event){
            $(this).popover('show');
        });

        $(this).on('mouseout', function(){
            $(this).popover('hide');
        });

        $(this).on('hide.bs.popover', function(){
            $(document).off('click.popover');
        });
    });
}
