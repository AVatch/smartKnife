var video   = document.getElementById("video-stream");
                var canvas  = document.getElementById("canvas");
                var ctx     = canvas.getContext('2d');

                function start() {
                    navigator.webkitGetUserMedia({video:true}, gotStream, function() {}); 
                }

                function gotStream(stream) {
                    video.src = webkitURL.createObjectURL(stream);
                }

                timer = setInterval(
                    function () {
                        ctx.drawImage(video, 0, 0, 320, 240);
                    }, 1000 / 30); //30 fpsc

                document.querySelector('#pause-button').addEventListener('click', function (e) {
                        video.pause();
                    }, false);

                
                $('#canvas').click(function(e) {
                    var pos = findPos(this);
                    var x = e.pageX - pos.x;
                    var y = e.pageY - pos.y;
                    var coord = "x=" + x + ", y=" + y;
                    //var c = this.getContext('2d');
                    var p = ctx.getImageData(x, y, 1, 1).data;
                    var rgb = "(RGB):" + p[0] + ", " + p[1] + ", " + p[2]; 
                    var hex = "#" + ("000000" + rgbToHex(p[0], p[1], p[2])).slice(-6);
                    $('#history').html(coord + "<br>" + hex + "<br>" + rgb);
                    
                    var div = document.getElementById('history');
                    div.style.backgroundColor = hex;

                    //Open a new window and pass
                    if(p[0]>150){
                        //open window with tomato
                        window.location = '{% url "result" itemToSearch="Tomato" %}';
                    }else{
                        //open window with potato
                        window.location = '{% url "result" itemToSearch="Potato" %}';
                        //Dajaxice.load(call_back, {"itemToSearch":"Potato"})

                    }
                });
                
                function call_back(html){
                    $('#result').empty().html(html);
                }

                /*get coordinates of click inside canvas*/
                function findPos(obj) {
                    var curleft = 0, curtop = 0;
                    if (obj.offsetParent) {
                        do {
                            curleft += obj.offsetLeft;
                            curtop += obj.offsetTop;
                        } while (obj = obj.offsetParent);
                        return { x: curleft, y: curtop };
                    }
                    return undefined;
                }

                /*convert RGB to Hex*/
                function rgbToHex(r, g, b) {
                    if (r > 255 || g > 255 || b > 255)
                        throw "Invalid color component";
                    return ((r << 16) | (g << 8) | b).toString(16);
                }

                //Hide the video feed, only display the canvas
                function initializePage(){
                    document.getElementById('video').style.display="none";
                }
                window.onload = initializePage;