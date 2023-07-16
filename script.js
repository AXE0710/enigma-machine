

var time = new Date()
var key = time.getSeconds()
function encryption() {

    let input = document.getElementById('input').value
    let out = ''
    for (let i = 0; i < input.length; i++) {
        let output = input.charCodeAt(i) + key

        output = String.fromCharCode(output)
        out += output
    }
    document.getElementById('output').textContent = out
}
function decryption() {
    let input = document.getElementById('input').value
    let out = ''
    for (let i = 0; i < input.length; i++) {
        let output = input.charCodeAt(i) - key

        output = String.fromCharCode(output)
        out += output
    }
    document.getElementById('output').textContent = out
}


