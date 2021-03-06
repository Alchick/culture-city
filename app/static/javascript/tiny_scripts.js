//COMMENTS FUNCTIONS
function send_comment(form, person) {
    var date = $(form).serialize();
    art_id = $('input[name=art_id]').val();
    val = document.getElementById('counter');
    if (person == 'admin') {
        rating = getCheckedRadio(); 
        date = date + '&' + 'rating' + '=' + rating;}
    //отправляю POST запрос и получаю ответ
    $.ajax({
        type:'post',//тип запроса: get,post либо head
        url:'set_comment.html',//url адрес файла обработчика
        data:date,//параметры запроса
        success:function(data){//возвращаемый результат от сервера
                var message = JSON.parse(JSON.stringify(data));
                $('#result').css('color',message['color']);
                $('#result').css('display','block');
                $('#result').html(message['message_words']);
                $('#result').fadeOut(5000);
                get_comment(art_id, 0, person);
                
              },
        error:function(){
            message = "<p>Произошла ошибка при отправке данных. Попробуйте снова или напишите нам</p>";
            $('#result').css('color','red');
            $('#result').css('display','block');
            $('#result').html(message);
            $('#result').fadeOut(5000);
        }
    });
}

function add_comment(data, person){
//     var comments = document.getElementById(object_id);
     var comments_place = document.getElementById(person+'_comments');
     comments_place.innerHTML = '';
     for (var i = 0; i<data.length; i++){
        var comment = document.createElement('div');
        comment.className = 'comment';
        if (person == 'user') {
            comment.innerHTML = "<p><span class='comment_field'>Имя пользователя</span>: " + data[i][0] + "</p>" +
        "<p><span class='comment_field'>Комментарий</span>: " + data[i][2] + "</p>"+
        "<p><span class='comment_field'>Добавлен</span>: " + moment.utc(data[i][1]).local().fromNow() + "</p><br>";
        }
        else{
            comment.innerHTML = "<p><span class='comment_field'>Имя пользователя</span>: " + data[i][3] + "</p>" +
        "<p><span class='comment_field'>Комментарий</span>: " + data[i][2] + "</p>"+
        "<p><span class='comment_field'>Добавлен</span>: " + moment.utc(data[i][1]).local().fromNow() + "</p>" + 
        "<p><span class='comment_field'>Рейтинг</span>: " + data[i][0] + "</p><br>";
        }
        comments_place.appendChild(comment);
     }
}

function get_comment(article_id, current_iter, person){
    i = i + current_iter;
    var next_page = document.querySelector('#'+person+'_next_button');
    var previous_page = document.querySelector('#'+person+'_previous_button');
    $.ajax({    
    type:'GET',
    url:'get_comment',
    data:{id:article_id,iter:i, person:person},
    success:function(data){
        add_comment(data[person+'_comments'], person);
        if (data[person+'_length'] <= 3){
            next_page.style.display = "none"}

        else{next_page.style.display = "inline"}

        if (i < 2){
            previous_page.style.display = 'none'}
            //document.getElementById('previous_page').style.display = 'none'}
            else{previous_page.style.display = 'inline'};
        
    }
   });
}

setTimeout(function(){
    $('.flash-message').fadeOut('fast')}, 5000);

function doClear(element) {
    if (element.value == element.defaultValue) { element.value = "" };
}

function doDefault(element) { 
    if (element.value == "") { element.value = element.defaultValue } 
}

function counterr(id) {
    document.getElementById(id).value=parseInt(document.getElementById(id).value) + 1;
    if (document.getElementById(id).value == 11){
        document.getElementById(id).value = 0;
    }
};


function submitForm(obj) {
    obj.form.submit()
    obj.form.reset();
    return false;
}

function time_format(data){
    document.write(moment.utc(data).local().format('YYYY-MM-DD HH:mm:ss'));
}

function time_fromNow(data){
    document.write(moment.utc(data).local().fromNow());
}


//light current main menu link
function shineLinks(id){
  try{
    var el=document.getElementById(id).getElementsByTagName('a');
    var url=document.location.href;
    for(var i=0;i<el.length; i++){
      if (url==el[i].href){
        el[i].className = 'active_menu';
        };
      };
    }
  catch(e){}
};

function getCheckedRadio(){
    var rating = null;
    var radioButtons = document.getElementsByName("articleRating");
    for (var i = 0; i < radioButtons.length; i ++){
        if (radioButtons[i].checked){
            rating = radioButtons[i].value;
        }
    }
    return rating;
}
