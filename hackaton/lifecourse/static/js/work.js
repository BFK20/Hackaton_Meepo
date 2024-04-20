

function setf(event){

    var created = document.createElement('form');
    alert("123")
    const largeHTMLContent = '
            {% csrf_token  %}
            <label for="fname">Название факультета:</label>
            <input type="text" id="fname" name = "fname" required>
            <button type="submit">Add Fac</button>
        '
    created.innerHTML = largeHTMLContent

    d = document.getElementById("formf");
    d.appendChild(created)
    alert("321")



}