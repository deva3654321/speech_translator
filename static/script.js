async function uploadAudio() {

    let file =
        document.getElementById("audioFile")
        .files[0];

    let formData = new FormData();

    formData.append(
        "audio",
        file
    );

    let response =
        await fetch(
            "/speech_to_text",
            {
                method:"POST",
                body:formData
            }
        );

    let data =
        await response.json();

    document.getElementById(
        "speechResult"
    ).value = data.text;
}


async function convertText(){

    let text =
        document.getElementById(
            "inputText"
        ).value;

    let lang =
        document.getElementById(
            "language"
        ).value;

    let formData =
        new FormData();

    formData.append(
        "text",
        text
    );

    formData.append(
        "lang",
        lang
    );

    let response =
        await fetch(
            "/text_to_speech",
            {
                method:"POST",
                body:formData
            }
        );

    let blob =
        await response.blob();

    let url =
        URL.createObjectURL(blob);

    document.getElementById(
        "audioPlayer"
    ).src = url;
}