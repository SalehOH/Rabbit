function increaseLikes(postId) {
  var request = new XMLHttpRequest();
  request.open('GET', '/like_post/' + postId + '/');
  request.onload = function() {
    if (request.status === 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('likes-' + postId).innerHTML = data.likes;
    } else {
      console.log('Error: ' + request.status);
    }
  };
  request.send();
}
