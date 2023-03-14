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
function joinRoom(roomName, userId) {

    fetch(`http://127.0.0.1:8000/${roomName}/${userId}/join/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("Error while joinig the room");
      })
      .then((data) => {
        joinButton.remove();
        members.insertAdjacentHTML("beforeend", userEle);
      })
      .catch((error) => {
        joinButton.remove();
        members.insertAdjacentHTML("beforeend", userEle);
      });
}

