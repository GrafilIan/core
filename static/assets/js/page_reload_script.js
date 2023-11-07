document.addEventListener("DOMContentLoaded", function () {
    // Get the loader element
    const loaderWrapper = document.getElementById("loader-wrapper");

    // Show the loader on page load
    loaderWrapper.style.display = "flex";

    // Add an event listener to hide the loader when the page is fully loaded
    window.addEventListener("load", function () {
        loaderWrapper.style.display = "none";
    });
});
