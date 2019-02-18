import Dropzone from 'dropzone';

const dropzoneId = "#fileupload"

$(document).ready(()=>{
    if (document.querySelector(dropzoneId)!==null){
    const myDropzone = new Dropzone(dropzoneId, {
        url: "/upload/",
        paramName: "file",
        init: function () {
            this.on("success", function (file, response) {
              console.log(response);
            });
          }
    });
}
})