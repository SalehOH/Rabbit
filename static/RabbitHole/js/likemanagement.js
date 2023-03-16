function likepost(postId) {
  var request = new XMLHttpRequest();
  request.open('GET', '/like_post/' + postId + '/');
  request.onload = function() {
    if (request.status === 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('likes-' + postId).innerHTML = data.likes;
      if (data.result == null){
        document.getElementById(postId+"like").classList.remove("btn-success");
      }else{
        document.getElementById(postId+"like").classList.add("btn-success");
        document.getElementById(postId+"dislike").classList.remove("btn-danger");
      }
    } else {
      console.log('Error: ' + request.status);
    }
  };
  request.send();
}

function dislikepost(postId) {
  var request = new XMLHttpRequest();
  request.open('GET', '/dislike_post/' + postId + '/');
  request.onload = function() {
    if (request.status === 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('likes-' + postId).innerHTML = data.likes;
      if (data.result == null){
        document.getElementById(postId+"dislike").classList.remove("btn-danger");
      }else{
        document.getElementById(postId+"dislike").classList.add("btn-danger");
        document.getElementById(postId+"like").classList.remove("btn-success");
      }
    } else {
      console.log('Error: ' + request.status);
    }
  };
  request.send();
}

function likereply(replyID) {
  var request = new XMLHttpRequest();
  request.open('GET', '/like_reply/' + replyID + '/');
  request.onload = function() {
    if (request.status === 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('likes-' + replyID).innerHTML = data.likes;
      if (data.result == null){
        document.getElementById(replyID+"like").classList.remove("btn-success");
      }else{
        document.getElementById(replyID+"like").classList.add("btn-success");
        document.getElementById(replyID+"dislike").classList.remove("btn-danger");
      }
    } else {
      console.log('Error: ' + request.status);
    }
  };
  request.send();
}

function dislikereply(replyID) {
  var request = new XMLHttpRequest();
  request.open('GET', '/dislike_reply/' + replyID + '/');
  request.onload = function() {
    if (request.status === 200) {
      var data = JSON.parse(request.responseText);
      document.getElementById('likes-' + replyID).innerHTML = data.likes;
      if (data.result == null){
        document.getElementById(replyID+"dislike").classList.remove("btn-danger");
      }else{
        document.getElementById(replyID+"dislike").classList.add("btn-danger");
        document.getElementById(replyID+"like").classList.remove("btn-success");
      }
    } else {
      console.log('Error: ' + request.status);
    }
  };
  request.send();
}