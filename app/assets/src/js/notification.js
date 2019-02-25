import Noty from 'noty';
let socket_url = 'ws://' + window.location.host + '/notify/'
Noty.overrideDefaults({
    type: 'success',
    layout: 'bottomRight',
    closeWith: ['button'],
    timeout: 3000
});

$(document).ready(()=>{
    if (location.pathname == '/upload/' || location.pathname == '/report/'){
    let socket = new WebSocket(socket_url);
    socket.onmessage = function(event){
        let message = JSON.parse(event.data)
        switch (message.type) {
        case 'load.success':
            new Noty({
                text: `File ${message.content} was loaded successfully`
            }).show();
            break;
        case 'report.success':
            new Noty({
                text: `Report ${message.content.filename} was successfully created. <br> You can download it by <a target="_blank" rel="noopener noreferrer" style="color:white;text-decoration:underline;" href="${message.content.download_link}">this link</a>`,
                timeout: false
            }).show();
            break;
        default:
            break;
    }
    }
}
})