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
    const btn = `<span class="option" data-func='${name}' style=" border: 2px solid black; background: grey; margin-left: 50px; margin-top: 40px; padding: 2px 5px; cursor: pointer;"> change to ${name} </span>`
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

choice.addEventListener('click', function(e){
    const span = e.target.parentElement;
    if(span.classList.contains("option") ){
        removeChildren(choice)
        refactor(felids, span.dataset.func)
        submitBtn.classList.remove('hidden')
    }
})