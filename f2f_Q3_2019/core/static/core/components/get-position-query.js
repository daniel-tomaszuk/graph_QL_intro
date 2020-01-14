function getPositionQuery() {
  const timePeriod = getTimePeriod();
  return `{
    allPositions(
        satellite_Name_Icontains: "Station",
        ${timePeriod?timePeriod:''}
    ) {
      edges {
        node {
          satellite {
            name
            noradId
            satelliteAlias
          }
          longitude
          latitude
        }
      }
    }
  }`;
}
