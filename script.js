function redirectToLocation(location) {
  let mapURL;
  switch (location) {
    case 'Location1':
      mapURL = 'https://maps.app.goo.gl/6o65TRq424uW2HdP8';
      break;
    case 'Location2':
      mapURL = 'https://www.google.com/maps?q=location2';
      break;
    case 'Location3':
      mapURL = 'https://www.google.com/maps?q=location3';
      break;
    default:
      mapURL = '#';
  }
  window.open(mapURL, '_blank');
}
