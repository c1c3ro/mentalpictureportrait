function major() {
    document.getElementById("major").classList.toggle("show");
    closeAllOthers("major");
}

function cups() {
    document.getElementById("cups").classList.toggle("show");
    closeAllOthers("cups");
}

function swords() {
    document.getElementById("swords").classList.toggle("show");
    closeAllOthers("swords");
}

function wands() {
    document.getElementById("wands").classList.toggle("show");
    closeAllOthers("wands");
}

function pentacles() {
    document.getElementById("pentacles").classList.toggle("show");
    closeAllOthers("pentacles");
}

function closeAllOthers(active){
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show') && openDropdown.id != active) {
            openDropdown.classList.remove('show');
        }
    }
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}