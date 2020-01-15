function getTimePeriod() {
    let timePeriodString = $('.select-period:checked');
    if (timePeriodString.length){
        timePeriodString = timePeriodString[0].value;
        const choices = {
            today: `timestamp_Gte: "${moment().startOf('day').toISOString()}"`,
            yesterday: `timestamp_Gte: "${moment().startOf('day').subtract(1, 'days').toISOString()}", timestamp_Lte: "${moment().startOf('day').toISOString()}"`,
            thisWeek: `timestamp_Gte: "${moment().startOf('week').toISOString()}", timestamp_Lte: "${moment().endOf('week').toISOString()}"`,
            thisMonth: `timestamp_Gte: "${moment().startOf('month').toISOString()}", timestamp_Lte: "${moment().endOf('month').toISOString()}"`,
            all: '',

        };
        return choices[timePeriodString];
    }
    return ''
}
