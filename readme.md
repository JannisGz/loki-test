### Aufbau:
Das Log-Creator-Image beinhaltet eine Pythonanwendung, die in einstellbaren Abständen Log-Einträge generiert. 
Das Log-Level wird zufällig gewählt, error oder critical Meldungen sind jedoch seltener als "INFO" Log-Einträge, um einen normalen Ablauf zu simulieren.
Die Pythonanwendung befindet sich im Verzeichnis 'log-creator-python'. Mit dem Dockerfile im Hauptverzeichnis kann es erstellt werden. 
Im Verzeichnis 'manifests' liegen die benötigten Kubernetes-Manifeste. Um sie zu benutzen muss das gebaute Docker-Image in ein Repository hochgeladen werden und der Name im Deployment entsprechend angepasst werden.


### Vorbereitung:
- Docker aufsetzen
- Kubernetes aufsetzen (hier minikube + kubectl)
- Log-creator Image erstellen und in ein Repository laden
- Persistent Volume aufsetzen (siehe Manifest-Verzeichnis)
- Log-Creator-Deployment ausführen: kubectl apply -f log-creator-deployment.yaml 

### Loki-Stack mit Helm aufsetzen:
- helm repo add grafana https://grafana.github.io/helm-charts
- helm repo update
- helm upgrade --install loki grafana/loki-stack  --set grafana.enabled=true,loki.persistence.enabled=true,loki.persistence.storageClassName=standard,loki.persistence.size=5Gi
- Siehe auch loki-stack-values.yaml im Manifest-Verzeichnis


### Grafana-Dashboard einsehen:
- Dashboard starten: kubectl port-forward service/loki-grafana 3000:80 
- Passwort erhalten: kubectl get secret loki-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
- Über localhost:3000 kann nun auf das Dashboard zugegriffen werden (Zugangsdaten: admin und das gerade ermittelte Passwort)
- In der Seitenleiste "explore" auswählen und als Datasource Loki auswählen
- Über den "Log Browser" können Pods ausgewählt werden. Hier den/die gewünschten Log-Creator-Pods auswählen. Das Resultat sollte wie im angehängten Screenshot aussehen
- Live-Modus um aktuell erstellte Logs einzusehen

### Bewertung Grafana-Loki-Stack:
- Selbst bei 100 Einträgen/Sekunde gehen keine Log-Einträge verloren
- Filtern nach Stichwörtern, Labels, Zeit, Quelle, etc. einfach möglich
- Im Live-Modus wird nur 1/Sekunde aktualisiert
- Gleichzeitige Darstellung mehrere Log-Quellen möglich, Visualisierung dafür aber nicht ausgelegt

![alt text](https://github.com/jannisgz/loki-test/blob/main/screenshot.png?raw=true)

