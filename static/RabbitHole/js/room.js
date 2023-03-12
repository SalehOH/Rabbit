const joinButton = document.getElementById("join")
const members = document.getElementById("members")
const userEle = `
<li>
    <a href="u/${members.dataset.curuser}">${members.dataset.curuser}</a>
</li>`

if(joinButton){
    joinButton.addEventListener("click", ()=> {
        console.log("clicked")
        joinRoom(joinButton.dataset.roomname, joinButton.dataset.userid)
    })
}

async function joinRoom(roomName, userId) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${roomName}/${userId}/join/`, {
      method: "GET",
      headers: {"Content-Type": "application/json"},
    });
    if (response.ok) {
      joinButton.remove();
      members.insertAdjacentHTML("beforeend", userEle);
    } else {
        throw new Error("Error while joining the room");
    }
  } catch (error) {
    console.error(error);
  }
}
