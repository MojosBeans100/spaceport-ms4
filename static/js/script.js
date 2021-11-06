

function tabform(element) {
    var current = element

    var parent_div = element.parentNode
    parent_div_id = parent_div.id

    next_div = parent_div.nextElementSibling

    next_div_id = next_div.id
   
    document.getElementById(parent_div_id).style.zIndex = -1
    document.getElementById(next_div_id).style.zIndex = 1
}


function tabback(element) {
    var current = element

    var parent_div = element.parentNode
    parent_div_id = parent_div.id

    form_element = parent_div.parentNode.length

    prev_div = parent_div.previousElementSibling
    prev_div_id = prev_div.id

    document.getElementById(parent_div_id).style.zIndex = -1
    document.getElementById(prev_div_id).style.zIndex = 1
}

function dropdown_choice() {

    form = document.getElementById("center-div3")
    console.log(form)
    
    if (document.getElementById("select3").value == "geojson") {

        if (form.children.length == 4) {
            form.children[3].remove()
        }

        // geojson_text = document.createElement("iframe")
        // geojson_text.setAttribute("src", "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d2197.960217004689!2d-3.5910141384353667!3d56.57174951941223!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2suk!4v1620980495144!5m2!1sen!2suk");
        // geojson_text.style.width = "640px";
        // geojson_text.style.height = "480px";
        // form.appendChild(geojson_text)
        
    }

    else if (document.getElementById("select3").value == "draw-on-map") {

        if (form.length == 4) {
            form.children[3].remove()
        }

        geojson_map = document.createElement("input")
        geojson_map.id = "geojson_map"
        geojson_map.placeholder ="Placeholder for map"
        form.appendChild(geojson_map)
    }
    
}