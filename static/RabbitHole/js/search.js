const searchResult = document.getElementById("search-result");
const searchInput = document.getElementById('search-bar');

searchInput.addEventListener('keyup', async () => {
    const query = searchInput.value;
    let results = '';
    if(query.length > 0) {
        
        const response = await fetch(`/search/?q=${query}`);
        const data = await response.json();

        const users = data.users;
        const rooms = data.rooms;

        users.forEach(user => {
            results += create_user_ele(user);
        });
        rooms.forEach(room => {
            results += create_room_ele(room);
        });
    }
    searchResult.innerHTML = results;
});

const create_room_ele = function(room){
room = `<li class="list-group-item">
            <a class="nav-link" href="/r/${room.name}">
                <img class="room-list-image" src="/images/${room.avatar.replace(/\\/g, "/")}" alt="${room.name}">
                <span class="mx-2">r/${room.name} </span>
            </a>
        </li>
`;
return room;
}
const create_user_ele = function(user){
user = `<li class="list-group-item">
            <a class="nav-link" href="u/${user.username}">
                <img class="room-list-image" src="/images/${user.avatar.replace(/\\/g, "/")}" alt="${user.username}">
                <span class="mx-2">u/${user.username}</span>
            </a>
        </li>
`;
return user;
}