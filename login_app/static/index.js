var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

function toggleTheme() {
    var theme = document.getElementsByTagName('link')[0];

    if (theme.getAttribute('href') == 'light.css') {
        theme.setAttribute('href', 'dark.css');
    } else if (theme.getAttribute('href') == 'dark.css') {
        theme.setAttribute('href', 'light.css');
    }
}
// w3schools helped me with the above