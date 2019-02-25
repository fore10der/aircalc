import Noty from 'noty';

Noty.overrideDefaults({
    type: 'success',
    layout: 'bottomRight',
    closeWith: ['button'],
    timeout: 6000
});

let $reportForm = $('.report_form')

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

const request_report = () => {
    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url: "/report/",
        type: "POST",
        data: {
            report_name: $('#id_report_name').val(),
            date_start: $('#id_report_date_start').val(),
            date_end: $('#id_report_date_end').val()
        },
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            $('#id_report_name').val('');
            $('#id_report_date_start').val('');
            $('#id_report_date_end').val('');
            $('.report-form').toggleClass('report-form_status_pending');
            new Noty({
                text: `The request for the formation of a report named ${json.report_name}.pdf in the interval from ${json.date_start} to ${json.date_end} was accepted.<br> You will be notified when it is generated.`
            }).show();
        }
    })
}

$(document).ready(()=>{
    $reportForm.on('submit', function(event){
        event.preventDefault();
        $('.report-form').toggleClass('report-form_status_pending')  // sanity check
        request_report()
    });
})