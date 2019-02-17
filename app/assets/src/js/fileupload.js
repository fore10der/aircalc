import Dropzone from 'dropzone';

const $dragTemplate = $('.dropzone-template');

const myDropzone = new Dropzone("#fileupload", {
    autoProcessQueue: false,
    url: "/upload/",
    paramName: "file",
    init : function() {
        let myDropzone = this
    },
    accept: (file,done) => {
        console.log(document.querySelector('input[type=file]').files)
        console.log(myDropzone.files)
    }
    
});