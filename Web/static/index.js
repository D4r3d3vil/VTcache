function scan(type){
    text = document.getElementById('textInp').value
    if(type == 'url') text = '?url=' + encodeURIComponent(text)
    console.log(text)
    fetch(`http://localhost:8000/${type}/${text}`)
}