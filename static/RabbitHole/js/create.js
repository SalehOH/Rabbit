const labels = document.querySelectorAll('label')
const choice = document.getElementById('choice')
const submitBtn = document.getElementById("submit-btn")
const mainDiv = document.getElementById("main")
const imageInput = document.querySelector('.imageF')
const textInput = document.querySelector('.textF')

const felids = {
    'image': {
        'label': '',
        'input': imageInput
    },
    'text': {
        'label': '',
        'input': textInput
    }
}
const svgs = {
    text: `<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-textarea-t" viewBox="0 0 16 16">
              <path d="M1.5 2.5A1.5 1.5 0 0 1 3 1h10a1.5 1.5 0 0 1 1.5 1.5v3.563a2 2 0 0 1 0 3.874V13.5A1.5 1.5 0 0 1 13 15H3a1.5 1.5 0 0 1-1.5-1.5V9.937a2 2 0 0 1 0-3.874V2.5zm1 3.563a2 2 0 0 1 0 3.874V13.5a.5.5 0 0 0 .5.5h10a.5.5 0 0 0 .5-.5V9.937a2 2 0 0 1 0-3.874V2.5A.5.5 0 0 0 13 2H3a.5.5 0 0 0-.5.5v3.563zM2 7a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm12 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
              <path d="M11.434 4H4.566L4.5 5.994h.386c.21-1.252.612-1.446 2.173-1.495l.343-.011v6.343c0 .537-.116.665-1.049.748V12h3.294v-.421c-.938-.083-1.054-.21-1.054-.748V4.488l.348.01c1.56.05 1.963.244 2.173 1.496h.386L11.434 4z"/>
            </svg>`,
    image: `<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-card-image" viewBox="0 0 16 16">
              <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
              <path d="M1.5 2A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-13zm13 1a.5.5 0 0 1 .5.5v6l-3.775-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12v.54A.505.505 0 0 1 1 12.5v-9a.5.5 0 0 1 .5-.5h13z"/>
            </svg>`
}
const checkName = function(ele){
    if(ele.innerHTML.includes('Image')){
        felids['image']['label'] = ele
    }else if (ele.innerHTML.includes('Content')){
        felids['text']['label'] = ele
    }
}

labels.forEach((l) => checkName(l))

const refactor = function(dict, except){
    let removed;
    for(const [key, value] of Object.entries(dict)){
        if(key == except){
            showFelid(value)
        }else{
            removeFelid(value)
            removed = key
        }
    }
    changeBtn(removed)
}
const showFelid = function(dict){
    for (const [_, value] of Object.entries(dict)){
        mainDiv.appendChild(value)
    }
}

const removeFelid = function(dict){
    for (const [_, value] of Object.entries(dict)){
        value.remove()
    }
}

const changeBtn  = function(name){
    const btn = `<span class="option" data-func='${name}' style=" margin-left: 50px; cursor: pointer;"> ${svgs[name]} </span>`
    choice.insertAdjacentHTML("beforeend", btn)
}

const removeChildren = function(parent){
    while (parent.lastChild) {
       if(parent.lastChild == submitBtn){
            return;
       }else{
        parent.removeChild(parent.lastChild);
       }
    }
}
for (const [key, value] of Object.entries(felids)){
    removeFelid(value)
}
const doChanges = function(ele) {
    removeChildren(choice)
    refactor(felids, ele.dataset.func)
    submitBtn.classList.remove('hidden')
}
choice.addEventListener('click', function(e){
    const span = e.target.parentElement;
    if(span.classList.contains("option") ){
        doChanges(span)
    }else if (span.parentElement.classList.contains("option")){
        doChanges(span.parentElement)
    }
})
