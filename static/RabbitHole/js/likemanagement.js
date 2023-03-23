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

const posts = document.getElementById("posts")
const replies = document.getElementById("replies")
const confirmDeleteBtn = document.getElementById("confirm-delete")

if (posts){
  posts.addEventListener("click", function(e){
    const parent = e.target.parentElement
    console.log("got it")
    if(parent.classList.contains("delete-post")){
      console.log("went")
      confirmDeleteBtn.setAttribute("href",`/delete_post/${parent.dataset.postId}`)
    }
  })
}

if(replies){
  replies.addEventListener("click", function(e){
    const parent = e.target.parentElement
    if(parent.classList.contains("delete-reply")){
      confirmDeleteBtn.setAttribute("href",`/delete_reply/${parent.dataset.replyId}`)
    }
  })
}