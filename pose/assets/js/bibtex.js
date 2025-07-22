const sections = [
    {id: "journals", filename: "journal_papers.bib"},
    {id: "bookchapters", filename: null},
    {id: "conferences", filename: "conferences_proceedings.bib"},
    {id: "educational-papers",  filename: null},
    {id: "posters", filename: "posters.bib"},
    {id: "technical-reports", filename: null},
    {id: "thesis", filename: null}
];

function load_citations(filename) {
    let xhr = new XMLHttpRequest();
    let url = "https://globalcomputing.group/assets/" + filename;
    xhr.open("GET", url);
    xhr.responseType = "text";
    xhr.send();
    console.debug("Fetching external content '" + xhr.url + '; alt. text will be presented if resource is unreachable');
    if (xhr.status !== 200)
        return null;

    let result = [];
    let regexp = /(@inproceedings|@article)/gi;
    let match = regexp.exec(xhr.response);
    while (match != null) {
        result.push(xhr.response.substring(match.index, regexp.lastIndex));
        match = regexp.exec(xhr.response);
    }
    return result;
}

function create_container(bibtex) {
    code = document.createElement("code");
    code.class = "tex bibtex";
    code.innerText = bibtex;
    pre = document.createElement("pre");
    pre.appendChild(code);
    result = document.createElement("div");
    result.class = "papercite_bibtex";
    result.appendChild(pre);
    return result;
}

document.addEventListener("load", function() {
    timeline = document.getElementsByClassName("scrollable-timeline")[0];
    console.debug("bibtex content loader assumes there is only 1 element with class 'scrollable-timeline'");

    let section_i = -1, section = null, citations = [], citation_i;
    let div_children = timeline.getElementsByTagName("div");
    let year_sections = timeline.getElementsByClassName("tl-section with-thumb");
    for (let div_i = 0; div_i < div_children.length; div_i++) {
        if (div_children[div_i].id === sections[section_i + 1].id) {
            section_i++;
            section = sections[section_i];
            citations = (section.filename == null ? null : load_citations(section.filename));
            citation_i = 0;
        }
        else if (citations != null && year_sections.contains(div_children[div_i])) {
            div_children[div_i].getElementsByClassName("tl-item pub-item with-thumb").forEach(function(item) {
               let wrapper = item.getElementsByClassName("content-wrapper")[0];
               let container = create_container(citations[citation_i++]);
               wrapper.append(container);
            });
        }
    }
});