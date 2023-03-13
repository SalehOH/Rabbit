const joinBtn = document.getElementById("join")
const members = document.getElementById("members")
const nav = document.getElementById("nav")

const userEle = 
`
<li>
    <a href="/u/${members.dataset.curuser}">${members.dataset.curuser}</a>
</li>
`
const createPostEle = 
`       
  <a href="/${joinBtn.dataset.roomname}/create-post/">Create a Post</a>
        
`
if(joinBtn){
  joinBtn.addEventListener("click", ()=> {
        console.log("clicked")
        joinRoom(joinBtn.dataset.roomname, joinBtn.dataset.userid);
        nav.insertAdjacentHTML("afterbegin", createPostEle);
        console.log("hey")
    })
}

async function joinRoom(roomName, userId) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${roomName}/${userId}/join/`, {
      method: "GET",
      headers: {"Content-Type": "application/json"},
    });
    if (response.ok) {
      joinBtn.remove();
      members.insertAdjacentHTML("beforeend", userEle);
    } else {
        throw new Error("Error while joining the room");
    }
  } catch (error) {
    console.error(error);
  }
}
