var container = document.getElementById('{CONTAINER}');
container.innerHTML = container.innerHTML + '{CONTENT}';
rows = getElementsByClassName("table-id");
var totalNumbeOfRows = container.rows.length;
for (var i = 1; i <= totalNumbeOfRows; i++)
    rows[i - 1].innerHTML = i;