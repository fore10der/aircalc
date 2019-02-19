import Dropzone from 'dropzone';

const dropzoneId = "#fileupload";
const dropzoneSelector = document.querySelector(dropzoneId);

$(document).ready(()=>{
    if (document.querySelector(dropzoneId)!==null){
    const myDropzone = new Dropzone(dropzoneId, {
        url: "/upload/",
        previewTemplate: "<div></div>",
        paramName: "file",
        maxFiles: 1,
        clickable: document.querySelector(`${dropzoneId} button`),
        init: function () {
            this.on("success", function (file, response) {
              console.log(response.status)
              if (response.status == 'OK'){
                if (dropzoneSelector.classList.contains('upload-fail'))
                  dropzoneSelector.classList.remove('upload-fail');
                dropzoneSelector.classList.add('upload-success');
                this.disable()
              }
              else {
                document.querySelector(`${dropzoneId} button span`).innerHTML = 'Try to load another'
                dropzoneSelector.classList.add('upload-fail');
              }
            });
            this.on("maxfilesexceeded", function(file) {
              this.removeAllFiles();
              this.addFile(file);
            });
          }
    });
    document.querySelector(`${dropzoneId} button`).addEventListener('click',(e)=>{
      e.preventDefault()
    })
}
})