var fadeSpeed = 400;
var animation, show_log;
var validator = new daFormValidation({
    debug: false,
    requiredSelector: 'input.required, select.required, textarea.required',
    useDefaultActions: {
        on_field_error: false
    }
});
validator.addFieldType('igree', '', '', false, 1, 1, '', '', false, true);

show_log = true;

validator.resetLanguageStrings({
    email: [
        'Укажите e-mail, например, mail@example.com',
        'Не корректный e-mail, адрес должен быть в виде mail@example.com',
        'Слишком короткое значение, адрес должен быть в виде mail@example.com',
        'Слишком длинное значение, адрес должен быть в виде mail@example.com'
    ]
});




function defineGoal(goals, request){
    if(show_log){
        console.info('defineGoal started with goals string "' + goals + '" and data:');
        console.log(request);
    }
    var parts = goals.split('|');
    for(var i = 0; i < parts.length; i++){
        var goal = parts[i].split(':');
        if(goal[0] == 'default')
            return goal[1];
        var condition = goal[0].split('=');
        if(typeof request[condition[0]] != 'undefined' && request[condition[0]] == condition[1] && goal[1])
            return goal[1];
    }
}

function sendGoal(form_data){
    if(show_log){
        console.info('sendGoal started with data:');
        console.log(form_data);
    }
    var form_config = form_data.config;
    // отправка в yandex метрику
    if(typeof daFormConfig != 'undefined' && daFormConfig.ym_counter_id && typeof window[daFormConfig.ym_counter_id] != 'undefined' && typeof form_config.goal_yandex != 'undefined' && form_config.goal_yandex){
        var yaGoal = form_config.goal_yandex;
        if(form_config.goal_yandex.indexOf(':') > (-1))
            yaGoal = defineGoal(form_config.goal_yandex, form_data.request);
            
        if(yaGoal){
            if(show_log)
                console.warn('Send yandex goal: ' + yaGoal);
            window[daFormConfig.ym_counter_id].reachGoal(yaGoal);
        }
    }
        
    // отправка в google analytics
    if(typeof ga != 'undefined' && typeof form_config.goal_google != 'undefined' && form_config.goal_google){
        var gGoal = form_config.goal_google;
        if(form_config.goal_google.indexOf(':') > (-1))
            gGoal = defineGoal(form_config.goal_google, form_data.request);
            
        if(gGoal){
            if(show_log)
                console.warn('Send google goal: ' + gGoal);
            ga('send', 'event', 'Формы', gGoal);
            // category
        }
    }
        
    if(typeof ga != 'undefined' && typeof form_config.goal_gtm != 'undefined' && form_config.goal_gtm){
        var ga_tag = form_config.goal_gtm.split(':');
        if(show_log){
            console.info('Send goal to GTM:' + ga_tag[0] + ', ' + ga_tag[1]);
        }
        if(ga_tag.length > 1){
            ga('send', 'event', 'Формы', ga_tag[0], ga_tag[1]);
            // category 
        }
    }
    
    // calltouch
    if(typeof window.ct_goal != 'undefined' && typeof form_config.goal_calltouch != 'undefined' && form_config.goal_calltouch){
        var ctGoal = form_config.goal_calltouch;
        if(form_config.goal_calltouch.indexOf(':') > (-1))
            ctGoal = defineGoal(form_config.goal_calltouch, form_data.request);
        
        if(ctGoal){
            if(show_log)
                console.warn('Send calltouch goal: ' + ctGoal);
            window.ct_goal(ctGoal);
        }
    }
    
	return true;
}

function startLoadingAnimation() {
    $.fancybox.close();
    
    $.fancybox.open($('#loading'), {
        scrolling: 'no',
        minHeight: '5',
        afterLoad: function() {
            setTimeout(function() {
                document.querySelector('progress').value = 100;
            }, 0);
            setTimeout(function() {
                $.fancybox.close($('#loading'));
                document.querySelector('progress').value = 0;
            }, 2000);
        },
        padding: 0,
        modal: true,
        helpers: {
            overlay: {
                locked: false
            }
        }
    });
}

function stopLoadingAnimation() {
    clearInterval(animation);
}

// function sendDataToCalltuchAPI(subject_calltouch, $form) {
//     if (!subject_calltouch)
//         return;
//     var ct_site_id = '25129';
//     var fio = '';
//     if ($form.find('input[name="name"]').length > 0) {
//         fio = $form.find('input[name="name"]').val();
//     }
//     if ($form.find('input[name="fio"]').length > 0) {
//         fio = fio + $form.find('input[name="fio"]').val();
//     }
//     if (/тест/i.test(fio)) {
//         return;
//     }
//     var phone = '';
//     if ($form.find('input[name="phone"]').length > 0) {
//         phone = $form.find('input[name="phone"]').val();
//     }
// 	if ($form.find('input[name="phoneall"]').length > 0) {
//         phone = $form.find('input[name="phoneall"]').val();
//     }
//     phone = phone.replace(/[^0-9]/gim, '');
//     var mail = '';
//     if ($form.find('input[name="email"]').length > 0) {
//         mail = $form.find('input[name="email"]').val();
//     }
//     if ($form.find('input[name="newold"]:checked').length > 0) {
//         if ($form.find('input[name="newold"]:checked').val() == 'Я новый пациент') {
//             sub = sub + ' (новый пациент)';
//         }
//         if ($form.find('input[name="newold"]:checked').val() == 'У меня уже есть медицинская карта клиники') {
//             sub = sub + ' (есть мед карта)';
//             fio = $form.find('input[name="number_card"]').val();
//         }
//     }
//     var ct_data = {
//         fio: fio,
//         phoneNumber: phone,
//         email: mail,
//         subject: subject_calltouch,
//         comment: document.location.href,
//         sessionId: window.call_value
//     };
//     if (phone != '' || mail != '') {
//         jQuery.ajax({
//             url: 'https://api-node7.calltouch.ru/calls-service/RestAPI/requests/' + ct_site_id + '/register/',
//             dataType: 'json',
//             type: 'POST',
//             data: ct_data,
//             async: false
//         });
//     }
//     return;
// }

function bindStyler(){
    if(!typeof $.fn.styler == 'function')
        return;
    var inputs = $('#success').find('input,select');
    if(inputs.length > 0)
        inputs.styler();
    return true;
}