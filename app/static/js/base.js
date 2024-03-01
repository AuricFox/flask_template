// Get references to the divider and the columns
var divider = document.getElementById("divider");
var leftColumn = document.getElementById("schema");
var rightColumn = document.getElementById("terminal");

// Variables to keep track of mouse movement
var isDragging = false;
var startWidth, startMouseX, startDividerX;

// Minimum and maximum width percentages for the left column
var minLeftColumnWidthPercent = 30;
var maxLeftColumnWidthPercent = 70;

// Event listener for mouse down on the divider
divider.addEventListener("mousedown", function (event) {
    isDragging = true;
    startWidth = leftColumn.offsetWidth;
    startMouseX = event.clientX;
    startDividerX = divider.getBoundingClientRect().left;

    // Prevent text selection while dragging
    event.preventDefault();
});

// Event listener for mouse move
document.addEventListener("mousemove", function (event) {
    if (isDragging) {
        
        var deltaX = event.clientX - startMouseX;                       // Calculate the change in mouse position
        var newDividerX = startDividerX + deltaX;                       // Calculate the new position of the divider
        var newWidth = (newDividerX / document.body.offsetWidth) * 100; // Calculate the new width of the left column

        // Apply size restrictions
        if (newWidth >= minLeftColumnWidthPercent && newWidth <= maxLeftColumnWidthPercent) {
            leftColumn.style.width = newWidth + "%";
            rightColumn.style.width = (100 - newWidth) + "%";
        }
    }
});

// Event listener for mouse up
document.addEventListener("mouseup", function (event) {
    isDragging = false;
});
