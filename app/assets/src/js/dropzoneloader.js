import Dropzone from 'dropzone';
if (document.querySelectorAll(".xlsx-upload").length){
let myDropzone = new Dropzone(".xlsx-upload",{
    previewTemplate: document.querySelector('#preview-template').innerHTML,
    maxFiles: 1,
    maxfilesexceeded: function(file) {
        this.removeAllFiles();
        this.addFile(file);
    },
    accept: function(file, done) {
        document.querySelectorAll(".needsclick").forEach((selector)=>{
            selector.style.display = 'none'
        })
        done();
      },
    autoQueue: false
})
}