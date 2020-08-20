const citations = []

function load_bibtex(filename) {
    var xhr = new XMLHttpRequest();
    url = "https://globalcomputing.group/assets/" + filename;
    xhr.open("GET", url);
    xhr.responseType = "text";
    xhr.send();
    console.debug("Fetching external content '" + xhr.url + '; alt. text will be presented if resource is unreachable');
    return (xhr.status == 200 ? xhr.response : "[citation not available]";
}

function create_container(filename, bibtex) {
    code = document.createElement("code");
    code.class = "tex bibtex";
    code.innerText = bibtex;
    pre = document.createElement("pre");
    pre.appendChild(code);
    result = document.createElement("div");
    result.class = "papercite_bibtex";
    result.id = "papercite_" + filename + "_block";
    result.appendChild(pre);
    return result;
}

function embed_bibtex(filename, parent) {
    bibtex = load_bibtex(filename);
    el = create_container(filename, bibtex);
    parent.appendChild(el);
}

document.addEventListener("load", function() {
    timeline = document.getElementsByClassName("scrollable-timeline")[0];
    console.debug("bibtex content loader assumes there is only 1 element with class 'scrollable-timeline'");

    var i = 0;
    timeline.getElementsByClassName("tl-section with-thumb").forEach(function(section) {
        section.getElementsByClassName("tl-item pub-item with-thumb").forEach(function(item) {
            wrapper = item.getElementsByClassName("content-wrapper")[0];
            console.debug("bibtex content embedder assumes there is only 1 child element with class 'content-wrapper' in each item element");
            if (filename = citations[i++])
                embed_bibtex(filename, wrapper);
        });
    });
});