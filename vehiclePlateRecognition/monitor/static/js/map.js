var map;
        var bounds;
        //constroi um id
        var id = makeUUID(); 
        

        let monitorSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/monitor/?group=monitor&name='
            + id
            + '/'
        );

        //inicia um agente
        function startAgent(tag_slug) {
            var camera = cameras.get(tag_slug);
            if (camera != undefined) {
                var xhr = new XMLHttpRequest();
                xhr.open("GET", "agent/" + tag_slug + "/start/", true);
                xhr.send();
            }
        }

        //para um agente
        function stopAgent(tag_slug) {
            var camera = cameras.get(tag_slug);
            if (camera != undefined) {
                var answer = confirm("Voc\xEA deseja desativar o agente da c\xE2mera " + (camera.controlpoint.cameras.indexOf(camera) + 1) + " do ponto de controle '" + camera.controlpoint.name + "'?");
                if (answer) {
                    monitorSocket.send(JSON.stringify({
                        'event': 'stop-request',
                        'message': tag_slug
                    }))
                }
            }
        }

        //mostra a taxa de processamento
        function askAgentProcessinRate(tag_slug) {
            var camera = cameras.get(tag_slug);
            if (camera != undefined) {
                monitorSocket.send(JSON.stringify({
                    'event': 'ask-processing-rate',
                    'message': tag_slug,
                    'target': id
                }))
            }
        }

        //abre a janela de stream da camera
        function openRTSPWindow(controlpoint_id) {
            window.open("rtsp-panel/" + controlpoint_id + "/" + id, "rtsp-panel", "toolbar=0,fullscreen=0,menubar=0,location=0");
        }

        //cria a caixa de informação do ponto de controle
        function controlpointInfoContent(controlpoint) {
            var content = "<div>" +
                "<div><b>" + controlpoint.name + "</b><br>" + controlpoint.address + "</div>" +
                "<div>" +
                "<p>Latitude: " + controlpoint.latitude + "<br>Longitude: " + controlpoint.longitude + "</p>" +
                "<p><i>Agente(s)</i>";

            if (controlpoint.cameras.length != 0) {
                $.each(controlpoint.cameras, function(index, camera) {
                    content += "<br>&ensp;" + (index + 1) + ". " + camera.direction;
                    content += " <img src='" + ICONS.status[camera.status].icon + "' width='16' height='16'>";
                    switch (camera.status) {
                        case STATUS_AGENT_ON_CAMERA_OFF:
                        case STATUS_AGENT_ON_CAMERA_ON:
                            content += " <a href=\"javascript:stopAgent('" + camera.tag_slug + "')\">desativar</a>";
                            content += " (<a href=\"javascript:askAgentProcessinRate('" + camera.tag_slug + "')\">fps</a>)";
                            break;
                        case STATUS_AGENT_OFF:
                            content += " <a href=\"javascript:startAgent('" + camera.tag_slug + "')\">ativar</a>";
                            break;
                    }
                });
                content += "</p><button onclick=\"openRTSPWindow(" + controlpoint.id + ")\">Abrir painel</button>";    
            }
            else {
                content += "<br>Nenhum agente cadastrado</p>";
            }

            content += "</div></div>";    
            
            return content;
        }

        //altera o status da camera
        function updateControlPoint(controlpoint) {
            var status = STATUS_UNKNOWN
            $.each(controlpoint.cameras, function(_, camera) {
                status = Math.min(status, camera.status);
            });
            controlpoint.marker.setIcon(ICONS.status[status].icon);
            controlpoint.marker.info.setContent(controlpointInfoContent(controlpoint));
        }

        function sleep(milliseconds) {
            const date = Date.now();
            let currentDate = null;
            do {
                currentDate = Date.now();
            } while (currentDate - date < milliseconds);
        }

        //inicializa o mapa
        function initMap() {
            //cria o mapa
            map = new google.maps.Map(document.getElementById("map-canvas"), {
                center: new google.maps.LatLng(-22.5138892, -44.0937475),
                zoom: 13,
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                mapTypeControl: false,
                streetViewControl: false
            });
            
            bounds = new google.maps.LatLngBounds();
            
            //marca no mapa o campus Valonguinho
            $.getJSON("../static/data/city_valon.json", function(data) {
                $.each(data["campi"].polygons, function(_, path) {
                    var polygon = new google.maps.Polygon({
                        paths: path,
                        strokeColor: '#87CEEB',
                        strokeOpacity: 1.00,
                        strokeWeight: 1,
                        fillColor: '#9BE2FF',
                        fillOpacity: 0.20,
                        map: map
                    });
                });
            });

            //marca no mapa o campus Praia Vermelha
            $.getJSON("../static/data/city_praia.json", function(data) {
                $.each(data["campi"].polygons, function(_, path) {
                    var polygon = new google.maps.Polygon({
                        paths: path,
                        strokeColor: '#87CEEB',
                        strokeOpacity: 1.00,
                        strokeWeight: 1,
                        fillColor: '#9BE2FF',
                        fillOpacity: 0.20,
                        map: map
                    });
                });
            });

            //marca no mapa o campus Gragoatá
            $.getJSON("../static/data/city_grag.json", function(data) {
                $.each(data["campi"].polygons, function(_, path) {
                    var polygon = new google.maps.Polygon({
                        paths: path,
                        strokeColor: '#87CEEB',
                        strokeOpacity: 1.00,
                        strokeWeight: 1,
                        fillColor: '#9BE2FF',
                        fillOpacity: 0.20,
                        map: map
                    });
                });
            });

            //marca no mapa o campus HUAP
            $.getJSON("../static/data/city_HUAP.json", function(data) {
                $.each(data["campi"].polygons, function(_, path) {
                    var polygon = new google.maps.Polygon({
                        paths: path,
                        strokeColor: '#87CEEB',
                        strokeOpacity: 1.00,
                        strokeWeight: 1,
                        fillColor: '#9BE2FF',
                        fillOpacity: 0.20,
                        map: map
                    });
                });
            });
            
            //coloca os pontos de controle no mapa
            for (var [_, controlpoint] of controlpoints) {
                var marker = new google.maps.Marker({
                    title: controlpoint.name,
                    position: new google.maps.LatLng(controlpoint.latitude, controlpoint.longitude),
                    icon: ICONS.status[controlpoint.cameras.length == 0 ? STATUS_UNKNOWN : STATUS_AGENT_OFF].icon,
                    info: new google.maps.InfoWindow({content: controlpointInfoContent(controlpoint), maxWidth: 350}),
                    map: map,
                });
                
                marker.addListener("click", function() {
                    this.info.open(map, this);
                });
                
                controlpoint.marker = marker;
                
                bounds.extend(marker.position);
            }
            
            //monta o map com as informações (junta tudo)
            map.fitBounds(bounds);
            
            monitorSocket.onmessage = function(e) {
                var data = JSON.parse(e.data);

                payload = data["payload"];
                console.log(payload)

                let event = payload.event; 

                switch (event) {
                    case "agent-connect":
                        status = 'conectado'

                    case "agent-update":
                        var camera = cameras.get(payload.who); 
                        if (camera != undefined) {
                            if (payload.message == 1) {
                                camera.status = STATUS_AGENT_ON_CAMERA_ON;
                            }
                            else {
                                camera.status = STATUS_AGENT_ON_CAMERA_OFF;
                            }
                            updateControlPoint(camera.controlpoint);
                        } 
                        break;
                        
                    case "agent-disconnect":
                        var camera = cameras.get(payload.who);
                        if (camera != undefined) {
                            camera.status = STATUS_AGENT_OFF;
                            updateControlPoint(camera.controlpoint);
                            alert("Conex\xE3o interrompida entre o monitor e o agente da c\xE2mera " + (camera.controlpoint.cameras.indexOf(camera) + 1)
                                + " do ponto de controle '" + camera.controlpoint.name + "'.");
                        } 
                        break;
                        
                    case "agent-processing-rate":
                        if (payload.target == id) {
                            var camera = cameras.get(payload.who);
                            var processing_rate = payload.message;
                            if (camera != undefined) {
                                alert("O agente da c\xE2mera " + (camera.controlpoint.cameras.indexOf(camera) + 1)
                                    + " do ponto de controle '" + camera.controlpoint.name + "' reportou"
                                    + " processamento a " + processing_rate + " quadros por segundo.");
                            }
                        } 
                        break;
                        
                    case "inventory":
                        $.each(payload.agents, function(_, pair) {
                            var camera = cameras.get(pair[0]); 
                            if (camera != undefined) {
                                if (pair[1]) {
                                    camera.status = STATUS_AGENT_ON_CAMERA_ON;
                                }
                                else {
                                    camera.status = STATUS_AGENT_ON_CAMERA_OFF;
                                }
                                updateControlPoint(camera.controlpoint);
                            }
                        })
                        break;
                }
                

            };
            
            
            monitorSocket.onclose = function(event) {
                alert("A conex\xE3o com o servidor foi interrompida.")
            };
        }
