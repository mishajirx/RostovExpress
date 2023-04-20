function myFunction() {
    // Get the checkbox
    var checkBox = document.getElementById("myCheck");
    // Get the output text
    var courier_info = document.getElementById("courier_info");

    // If the checkbox is checked, display the output text
    if (checkBox.checked === true) {
        courier_info.style.display = "block";
    } else {
        courier_info.style.display = "none";
    }
}