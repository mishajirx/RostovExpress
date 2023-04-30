function myFunction(box_id, block_id) {
    // Get the checkbox
    console.log(box_id);
    console.log(block_id);

    let checkBox = document.getElementById(box_id);
    // Get the output text
    let block = document.getElementById(block_id);

    // If the checkbox is checked, display the output text
    if (checkBox.checked === true) {
        block.style.display = "block";
    } else {
        block.style.display = "none";
    }
}