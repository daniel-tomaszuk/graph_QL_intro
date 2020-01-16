
function makeRequest(method, url, positionQuery) {
    if (positionQuery) {
        url = url + '?query=' + positionQuery
    }
    return axios({
        method: method,
        url: url,
        headers: {
          'Content-Type': 'application/json',
        },
        timeoutSeconds: 5,
      }).then(function (response) {
        console.log('Successful data fetch.');
        return response.data
      }).catch(function (error) {
        console.log('Error has occurred');
        console.log(error)
      })
}
