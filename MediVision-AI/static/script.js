function analyze() {
    let fileInput = document.getElementById("image");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please upload an image");
        return;
    }

    let formData = new FormData();
    formData.append("image", file);

    fetch("/analyze", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
    })
    .catch(error => {
        document.getElementById("result").innerText = "❌ Error occurred";
    });
}
