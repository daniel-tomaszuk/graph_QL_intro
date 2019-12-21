

function makeRequest(method, url, positionQuery) {
    const response = ''
    var urlParams = ''
    if (positionQuery) {
        url = url + '?query=' + positionQuery
    }
    return axios({
        method: method,
        url: url,
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(function (response) {
        console.log('Successful data fetch.')
        return response.data
      }).catch(function (error) {
        console.log(error)
        console.log('Error has occured: ' + error.statusTet)
        console.log(error.data)
      })
}
