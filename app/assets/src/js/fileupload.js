import Dropzone from 'dropzone';

const dropzoneId = "#fileupload"

$(document).ready(()=>{
    if (document.querySelector(dropzoneId)!==null){
    const myDropzone = new Dropzone(dropzoneId, {
        url: "/upload/",
        paramName: "file",
        maxFiles: 1,
        clickable: document.querySelector(`${dropzoneId} button`),
        init: function () {
            this.on("success", function (file, response) {
              console.log(response);
            });
            this.on("maxfilesexceeded", function(file) {
              this.removeAllFiles();
              this.addFile(file);
            });
            this.on("dragenter",function() {
              console.log("start");
            })
            this.on("dragleave",function() {
              console.log("end");
            })
          }
    });
    document.querySelector(`${dropzoneId} button`).addEventListener('click',(e)=>{
      e.preventDefault()
    })
}
})