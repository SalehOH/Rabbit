const joinBtn = document.getElementById("join")
const members = document.getElementById("members")
const nav = document.getElementById("nav")

let createPostEle = ``
if(joinBtn){
  createPostEle = 
  `<a class="nav-link" href="/${joinBtn.dataset.roomname}/create-post/">Create a Post</a> `
  
  joinBtn.addEventListener("click", ()=> {
        joinRoom(joinBtn.dataset.roomname, joinBtn.dataset.userid);
        nav.insertAdjacentHTML("afterbegin", createPostEle);
    })
}

async function joinRoom(roomName, userId) {
  try {
    const response = await fetch(`/${roomName}/${userId}/join/`, {
      method: "GET",
      headers: {"Content-Type": "application/json"},
    });
    if (response.ok) {
      joinBtn.remove();
      members.insertAdjacentHTML("beforeend", await get_user('admin'));
    } else {
        throw new Error("Error while joining the room");
    }
  } catch (error) {
    console.error(error);
  }
}

const get_user = async function(username){
  console.log(username)
  const response = await fetch(`/search/?q=${username}`);
  if (response.ok){
    const data = await response.json();
    console.log(data)
  }else{
    throw new Error(" something went wrong")
  }

  const userEle = 
    `
    <li class="list-group-item">
          <a class="nav-link" href="/u/${user.username}/">
              <img class="room-list-image" src="/images/${room.avatar.replace(/\\/g, "/")}" alt="${user.username}">
              <span class="mx-2">u/${user.username}</span>
          </a>
    </li>
  `;
  return userEle;
}