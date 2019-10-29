webiopi().ready( function()
{	// Initialize
	webiopi().callMacro( "MoveForward", [0] );
        
} );

function onCheckboxLed( led )
{
	if( 1 == led )
	{
		webiopi().callMacro( "ChangeLedActive", [1, document.getElementsByName("led1")[0].checked ? 1 : 0] );
		return;
	}
}

var title = ['<hr size="3" color="#000000">',
             '<B><center> Car Controller<br><br>'].join("");

var table = ['<table id="tbl" boarder=2>',
             '<tr><th>稼働状態</th><th>距離計測</th></tr>',
             '<tr><th>-</th><th>-</th></tr></table>'].join("");

var button = ['<hr size="3" color="#000000">',
              '<input type="button" value="前進" onclick="MoveCar(1)" style="width:80px;height:80px"><br>',
              '<input type="button" value="左折" onclick="MoveCar(2)" style="width:80px;height:80px">',
              '<input type="button" value="停止" onclick="MoveCar(5)" style="width:80px;height:80px;color:#ff0000">',
              '<input type="button" value="右折" onclick="MoveCar(3)" style="width:80px;height:80px"><br>',
              '<input type="button" value="後退" onclick="MoveCar(4)" style="width:80px;height:80px"><br>'
              ].join("");

function MoveCar(direct){

    if (1 == direct){
        var re = 0;
        webiopi().callMacro("MoveForward", direct, callBackMove); 

    }


function callBackMove(macro, direct, data){

    alert(direct);
    //document.getElementById("tbl").rows[1].cells[0].innerHTML= data;
    
    }

function GetGPIOValue(){

    webiopi().digitalRead(27, showRe);
    //"http://192.168.0.10:8000/GPIO/27/value";

    }

function showRe(gpio, data){
    document.getElementById("tbl").rows[1].cells[0].innerHTML= data;
}

function ShowButton(){

    var form = document.createElement('form');
    form.setAttribute("name","robot");
    form.setAttribute("method","post");
    form.setAttribute("target","hiddeniframe");
    
    form.innerHTML = title+table;
    form.style.display = "block";
    document.body.appendChild(form);

   // form.submit();
    
    }

function SetDirection(direct){

    webiopi().callMacro("ChangeLedActive", [1, direct] );
    return;

    
    }
window.onload = function(){

    
    ShowButton();
    
    
    };
